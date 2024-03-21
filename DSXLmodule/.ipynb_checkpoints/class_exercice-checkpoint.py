import re
import os


def replace_variables(text, liste_variables):
    ''' 
    Exemple :
    liste_variables =  [ 'pourc:90' , 'nouvques:130' , 'Au:\dfrac{100}{9}' ]
    Le programme trouve dans text '\\var{pourc}{yyy}' , '\\var{nouvques}{yyy}', '\\var{Au}{yyy}' et 
    les remplace par '90', '130', '\dfrac{100}{9}'
    '''
    dico_var = {}
    for item in liste_variables :
        i = item.find(':')
        xxx = item[:i]
        zzz = item[i+1:]    
        dico_var[xxx] = zzz
       
    text_new = ''
    k_last = 0
    k = 0
    while k < len(text):
        #print('k=',k)
        var_start = text.find("\\var{", k)
        if var_start == -1:
            break
        k = var_start + 5  # Move past "\\var{" to the opening brace
        count_braces = 1
        k1 = k
        found = False
        while (k < len(text)) and not found :
            k=k+1
            if text[k] == '{':
                count_braces += 1
            elif text[k] == '}':
                count_braces -= 1

            if count_braces == 0:
                # On récupère le nom de la variable : 
                xxx = text[k1:k]
                #print('xxx = ',xxx)
                found = True
            # text[k] = '}'.
        found = False
        count_braces = 0
        # Position début de yyy :
        #print('k1=',k1,text[k1:])
        k1 = k+1
        # On cherche la position de la fin de \\var{xxx}{yyy} : 
        while (k < len(text)) and not found :
            k=k+1
            if text[k] == '{':
                count_braces += 1
            elif text[k] == '}':
                count_braces -= 1

            if count_braces == 0: # Cad k indique la position de '}'
                found = True
                # Ancienne valeur de la variable (dont on a plus besoin)
                yyy = text[k1+1:k]
                #print('yyy', yyy, k1+1,k)
                # On a la position du 1er caractère après la fin de \\var{xxx}{yyy}:
                text_new = text_new+text[k_last:var_start]+dico_var[xxx]
                k += 1
                k_last = k
    # Il faut encore compléter avec le reste du texte : 
    text_new = text_new+text[k_last:]
    return text_new 


## Exemple d'utilisation :
#texte_exemple = "Ceci est un exemple avec \\var{vitesse}{m/s} et \\var{temps}{s}."
#liste_variables = ["vitesse:30 km/h", "temps:120 s"]
#
#texte_modifie = replace_variables(texte_exemple, liste_variables)
#print(texte_modifie)  # Affiche "Ceci est un exemple avec 30 km/h et 120 s."

def replace_poids(text, points):
    # Cette fonction interne effectue le calcul et retourne le résultat
    def calculate(match):
        xx = float(match.group(1))  # Convertit xx en un nombre à virgule flottante
        result = xx * points / 100   # Effectue le calcul
        return '\points{'+str(result)+'}'          # Retourne le résultat sous forme de chaîne de caractères

    # La regex suivante trouve des motifs qui correspondent à \poids{xx}
    pattern = r'\\poids\{(\d+(?:\.\d+)?)\}'
    
    # Utilise sub avec la fonction calculate pour remplacer les motifs trouvés
    return re.sub(pattern, calculate, text)

## Exemple d'utilisation :
#texte_exemple = "Le total est de \\poids{150} kg."
#poids = 50  # Remplacez cette valeur par le poids réel que vous souhaitez utiliser#
#
#texte_modifie = replace_poids(texte_exemple, poids)
#print(texte_modifie)  # Affiche "Le total est de 75.0 kg." si poids est 50



def fonction_param_exercice_test() :

    dico_exercice = {
        'nom_exercice': 'exercice_test' ,
        'date_creation': '10/01/2024' ,
        'source': 'marcus' ,
        'liste_notions' :  [ 'Pythagore' , 'triangle rectangle' ] , 
        'liste_variables' :  [ 'a:3' , 'b:4' , 'h2:25' , 'm:-2' , 'p:1.5' ]
        }

    liste_liste_parametres = []
    for a in range(3,6) : 
        for b in range(3,a+1) :
            for m in range(-1,2) :
                for p in range(-2,3) : 
                    liste_liste_parametres.append(["a:"+str(a),"b:"+str(b),"h2:"+str(a**2+b**2),"m:"+str(m),"p:"+str(float(p/5))])
                    
                    
    return dico_exercice, liste_liste_parametres

# https://stackoverflow.com/questions/739882/iterating-over-object-instances-of-a-given-class-in-python

#class IterRegistry(type):
#    def __iter__(cls):
#        return iter(cls._registry)

#class Person(object):
#    __metaclass__ = IterRegistry
#    _registry = []

#    def __init__(self, name):
#        self._registry.append(self)
#        self.name = name
#>>> p = Person('John')
#>>> p2 = Person('Mary')
#>>> for personobject in Person:
#...     print personobject
#...
#<person.Person object at 0x70410>
#<person.Person object at 0x70250>


class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)
        

class Exercice(object):
    __metaclass__ = IterRegistry
    _registry = []    
    def __init__(self, dico_exercice, liste_liste_parametres,mode_test=False):
        self._registry.append(self)
        self.nom_exercice = dico_exercice["nom_exercice"]
        self.date_creation =  dico_exercice["date_creation"]
        self.source =  dico_exercice["source"]
        self.liste_notions =  dico_exercice["liste_notions"]
        self.liste_variables =  dico_exercice["liste_variables"]
        self.liste_liste_parametres = liste_liste_parametres
        if mode_test ==False :
            self.file_path = './DSXLmodule/text_exercices/'+self.nom_exercice+".tex"
        else :
            self.file_path = './latex_main_exercice_test.tex'

    def genere_code_latex(self, choix_param, points): 
        if len(self.liste_liste_parametres)>choix_param :
            liste_variables = self.liste_liste_parametres[choix_param]
        else :
            liste_variables = self.liste_variables 

        # On charge le fichier latex  à modifier : 
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                code_latex_in = file.read()
                
                code_latex_out =  replace_variables(code_latex_in, liste_variables)
                texte_modifie = replace_poids(code_latex_out, points)
                return texte_modifie
        return ""
    
# Ex_test = Exercice(fonction_param_exercice_test) 

def genere_latex_tous_parametres(Ex_xxx) : 
    # Lire le contenu du fichier d'en-tête LaTeX
    header_file_path = "./parametres_dsxl/Latex_head_dsxl_commandes.tex"
    
    with open(header_file_path, 'r') as file:
        header_content = file.read()
    final_content = header_content + "\n\\begin{document}\n"     
    for i in range(len(Ex_xxx.liste_liste_parametres)) :
        text_content = Ex_xxx.genere_code_latex(i,4)
        final_content = final_content+ "\n\n"+ text_content
        
    # Préparer le contenu final
    final_content =  final_content + "\n\\end{document}\n"
    output_file_path = "./dsxl_tex_exercice/latex_test_module_full/latex_test_module_full.tex"
    with open(output_file_path, 'w') as file:
        file.write(final_content)
        
#genere_latex_tous_parametres(Ex_001) 
#list_exercices_parametre_points = [(Ex_test,4,5),(Ex_test,2,5)]       
        
def genere_main_latex_list_exercices_points(list_exercices_parametre_points) : 
    # Lire le contenu du fichier d'en-tête LaTeX
    
    content = "\n\n"
    for Ex_xxx,param,points in list_exercices_parametre_points :
        text_content = Ex_xxx.genere_code_latex(param,points)
        content = content+ "\n\n"+ text_content
    return content
     
#print(genere_main_latex_list_exercices_points(list_exercices_parametre_points) )    



 
