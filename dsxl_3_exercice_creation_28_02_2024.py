import tkinter as tk
from tkinter import ttk
import os
from tkinter import font
import json
import pandas as pd
# Module pour traiter les expressions régulières 
import re
import sys
import numpy as np

#https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
from importlib import reload

from tkinter import messagebox

#sys.path.append('./DSXLmodule/')
#for path in sys.path:
#    print(path)
print(print(os.getcwd()))
# setting path
#sys.path.append('../parentdirectory')
sys.path.append('./DSXLmodule') 
# importing
#from DSXLmodule.class_exercice import * 
from DSXLmodule.list_function_param_exercices import * 

#Ex_001 = Exercice(list_of_fonction_param_exercices[0] )
#print(list_of_dico_exercices)
# print(Exercice._registry)
for exerciceobject in Exercice._registry:
    print (exerciceobject.liste_notions)

#---------------------------------------

#Créer la fenêtre principale
root = tk.Tk()
root.title("DSXL 3 : création exercices")

###############################################################################################
#                                   VARIABLES GLOBALES
###############################################################################################
# Définir la police désirée
desired_font = font.Font(family="Times", size=14,weight='bold')

# Variable global pour état de l'onglet "tab_dsxl_python_wrapper"
# Créer le dictionnaire avec les variables/paramètres de l'exercice 
dico_dsxl_python_wrapper = { "nom_exercice" : "exercice_XXX",
                                 "date_creation" : "jj/mm/aaaa",
                                 "source" : "annales apmep", 
                                 "liste_notions" : [], 
                                 "liste_variables" : [] }

str_liste_notions_choisies = ''
#Add fonts for all the widgets
root.option_add("*Font", "Times 14 bold")




#-------------------------Fonctions utiles ---------------------------------------------

# Cette fonction crée le text pour afficher la liste des notions choisies
def liste_notions_choisies_to_str(liste_notions_choisies) :
    ''' La procédure 'liste_notions_choisies_to_str' prend les chaines de caractère dans une liste et les concatène 
        en une seule chaine de caractère qui sera affichée dans un label. 
    '''
    str_liste_notions_choisies = ""
    for notion in liste_notions_choisies :
        str_liste_notions_choisies = str_liste_notions_choisies + notion+' : '
    return str_liste_notions_choisies

def find_substrings_var(text):
    ''' La fonction 'find_vfind_substrings_varariables(text)' cherche les chaines de la forme \var{.x.}{.y.} et 
    renvoit 
        1) la liste des variables lst_var = [ '.x.:.y.', etc...]
        2) un dictionnaire dico_var = { '.x.':'.y.', etc... } 
    Remarque : si la variable existe en plusieurs exemplaires, les autres entrées sont de lst_var sont de la forme  '*.x.:.y.'
    Elle est capable de gérer des entrées comme \\var{Au}{\dfrac{100}{9}}
    # Example usage:
    your_text = "Your input text with \\var{abc{def}}{123} and \\var{xyz}{456}.\
                    \n \\var{Au}{\dfrac{100}{9}} "
    result = find_substrings(your_text)
    print(result)
    '''
    result_list = []
    k = 0
    dico_var = {}
    while k < len(text):
        var_start = text.find("\\var{", k)

        if var_start == -1:
            break

        k = var_start + 5  # Move past "\\var{" to the opening brace
        count_braces = 1
        k1 = k

        while k < len(text):
            if text[k] == '{':
                count_braces += 1
            elif text[k] == '}':
                count_braces -= 1

            if count_braces == 0:
                xxx = text[k1:k]
                #print('xxx',xxx, k1, k)
                break

            k += 1

        #k = var_start + 5  # Reset k for yyy extraction
        k=k+1
        count_braces = 0
        k1 = k+1

        while k < len(text):
            if text[k] == '{':
                count_braces += 1
            elif text[k] == '}':
                count_braces -= 1

            if count_braces == 0:
                yyy = text[k1:k]
                #print('yyy', yyy, k1,k)
                break

            k += 1

        if xxx not in dico_var : 
            dico_var[xxx] = yyy
            result_list.append(f"{xxx}:{yyy}")
        else : 
            dico_var['*'+xxx] = yyy
            result_list.append(f"*{xxx}:{yyy}")

    return result_list,dico_var

## Example usage:
#your_text = "Your input text with \\var{abc{def}}{123} and \\var{xyz}{456}. \n \\var{Au}{\dfrac{100}{9}} "
#result,dico = find_substrings(your_text)
#print(result)




def ask_user(str_la_question):
    reponse = messagebox.askquestion("Question", str_la_question)
    if reponse == 'yes':
        print("L'utilisateur a choisi Oui.")
    else:
        print("L'utilisateur a choisi Non.")
    return reponse

################################# tabControl ##################################################

#Créer le contrôle d'onglets (Notebook)
tabControl = ttk.Notebook(root)

#reponse = ask_user("Voulez-vous procéder ?")
###############################################################################################
#                      TAB : tab_latex_wrapper                 
###############################################################################################
# -----------------Evènements liés à :  tab_latex_wrapper  
#
#   - frame_texts_latex_wrapper : qui contient deux zones de texte 
#            text_in_latex_wrapper    &   text_out_latex_wrapper
#

#   - frame_insert_buttons_latex_wrapper : qui contient 
#                les boutons : "%E>", "%E<", "%C>", "%C<", "\poids{} %en pourcentage","\\var{}{}" et "WRAP UP!"
#
def insert_button_latex_wrapper_text_in(text):
    text_in_latex_wrapper.insert(tk.INSERT, text)


def python_wrapper_load_variables() :
    global dico_dsxl_python_wrapper
    '''python_wrapper_load_variables() 
    1) charge le dictionnaire dico_dsxl_python_wrapper.json si il existe.
        a) Si ce fichier existe, alors le dico_dsxl_python_wrapper est chargé.
        b) Si ce fichier n'existe pas, alors la variable globale dico_dsxl_python_wrapper garde ses valeurs par défaut. 
    2) La liste liste_toutes_notions de toutes les notions est chargée dans le widget combo_box_liste_notions
    3) la liste des notions choisies est chargée dans le widget label_liste_notions_choisies_contenu
    4) Les labels entry_nom_exercice, entry_date_creation, entry_source sont chargés 
    
    Les variables dico_dsxl_python_wrapper, str_liste_notions_choisies sont retournées
    '''
    # charger le dictionnaire avec les variables/paramètres de l'exercice si il existe :                                
    file_path = "./dsxl_tex_exercice/dico_dsxl_python_wrapper.json"
    if os.path.exists(file_path) :
        with open(file_path, 'r') as file:         # Read dictionary json file
            dico_dsxl_python_wrapper = json.load(file) 
    else : 
        dico_dsxl_python_wrapper = { "nom_exercice" : "exercice_XXX",
                                 "date_creation" : "jj/mm/aaaa",
                                 "source" : "annales apmep", 
                                 "liste_notions" : [], 
                                 "liste_variables" : [] }
    # Charger la liste detoutes les notions : 
    pd_tableau_notions_niveaux = pd.read_csv('./parametres_dsxl/tableau_notions_niveaux.csv')
    liste_toutes_notions = list(pd_tableau_notions_niveaux["mots_cles"])
    # Attribuez la liste des valeurs à la propriété 'values' du Combobox
    combo_box_liste_notions['values'] = liste_toutes_notions
    liste_notions_choisies = dico_dsxl_python_wrapper["liste_notions"]
    # Afficher les notions choisies : 
    str_liste_notions_choisies = liste_notions_choisies_to_str(liste_notions_choisies)
    label_liste_notions_choisies["text"] = "Liste des notions choisie -> "
    label_liste_notions_choisies_contenu["text"] = str_liste_notions_choisies
    # Afficher le nom de l'exercice, la date de création et la source : 
    entry_nom_exercice.insert(0,dico_dsxl_python_wrapper["nom_exercice"])
    entry_date_creation.insert(0,dico_dsxl_python_wrapper["date_creation"])
    entry_source.insert(0,dico_dsxl_python_wrapper["source"])
    return dico_dsxl_python_wrapper, str_liste_notions_choisies   
    
    

def python_wrapper_save_variables() :
    ''' python_wrapper_save_variables() sauvegarde dico_dsxl_python_wrapper sur le disque dans :
        ./dsxl_tex_exercice/dico_dsxl_python_wrapper.json
    '''
    dico_dsxl_python_wrapper["nom_exercice"] =entry_nom_exercice.get()
    dico_dsxl_python_wrapper["date_creation"] =entry_date_creation.get()
    dico_dsxl_python_wrapper["source"] = entry_source.get()
    file_path = "./dsxl_tex_exercice/dico_dsxl_python_wrapper.json"                             
    # Pour sauvegarder ce dictionnaire dans un fichier JSON :
    with open(file_path, 'w') as fichier_json:
        json.dump(dico_dsxl_python_wrapper, fichier_json, indent=4)
        fichier_json.close()
        

            
# Fonction pour charger le contenu des fichiers dans : 
# -text_latex_wrapper_in
# -text_latex_wrapper_out
# -text_python_wrapper_in
# -text_python_wrapper_out
def load_file_to_text_wrappers():
    '''load_file_to_text_wrappers() charger le contenu des fichiers dans les widgets (zones text) :
       liste_fichiers_text_wrapper 
                = [["./dsxl_tex_exercice/dsxl_text_latex_wrapper_in.tex",text_in_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_latex_wrapper_out.tex",text_out_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex",text_in_python_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py",text_out_python_wrapper]]    '''
    
    for file_path,text_wrapper in liste_fichiers_text_wrapper :
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                text_wrapper.delete(1.0, tk.END)
                text_wrapper.insert(1.0, content)

def save_text_wrappers_to_files():
    '''save_text_wrappers_to_files() sauvegarde le contenu des widgets (zones text) dans les fichiers :
       liste_fichiers_text_wrapper 
                = [["./dsxl_tex_exercice/dsxl_text_latex_wrapper_in.tex",text_in_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_latex_wrapper_out.tex",text_out_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex",text_in_python_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py",text_out_python_wrapper]] 
    '''

    for file_path,text_wrapper in liste_fichiers_text_wrapper :
        content = text_wrapper.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
            
def save_text_wrappers_FULL_to_files(): 
    ''' save_text_wrappers_FULL_to_files()  sauvegarde le contenu des widgets (zones text) en ajoutant 
         head.tex, \begin{document} , \end{document} dans les fichiers pour en faire un fichier Latex compilable :
    Liste_fichiers_text_wrapper_full = \
                [["./dsxl_tex_exercice/latex_wrapper_in_full/dsxl_text_latex_wrapper_in.tex",text_in_latex_wrapper],
                 ["./dsxl_tex_exercice/latex_wrapper_out_full/dsxl_text_latex_wrapper_out.tex",text_out_latex_wrapper],
                 ["./dsxl_tex_exercice/python_wrapper_in_full/dsxl_text_python_wrapper_in.tex",text_in_python_wrapper]]
    '''
    # Lire le contenu du fichier d'en-tête LaTeX
    header_file_path = "./parametres_dsxl/Latex_head_dsxl_commandes.tex"
    with open(header_file_path, 'r') as file:
        header_content = file.read()
    for file_path,text_wrapper in Liste_fichiers_text_wrapper_full :        
        text_content = text_wrapper.get(1.0, tk.END)
        # Préparer le contenu final
        final_content = header_content + "\n\\begin{document}\n" + text_content + "\n\\end{document}\n"
        with open(file_path, 'w') as file:
            file.write(final_content)

            
# Commande button_wrap_latex 
def command_button_wrap_latex_copy_and_replace():
    '''command_button_wrap_latex_copy_and_replace() copie le texte de text_latex_wrapper_in à text_latex_wrapper_out et 
       effectue les remplacements :  
                replacements = {
                    "%E>": "\\enonce{ %début énoncé \n",
                    "%E<": "} % fin énoncé \n",
                    "%C>": "\\correction{ %début correction \n",
                    "%C<": "} % fin correction \n"       
    '''
    # Copier le texte de text_latex_wrapper_in à text_latex_wrapper_out
    text_content = text_in_latex_wrapper.get("1.0", tk.END)
    text_out_latex_wrapper.delete("1.0", tk.END)  # Effacer le contenu existant dans text_latex_wrapper_out
    text_out_latex_wrapper.insert("1.0", text_content)  # Insérer le contenu copié dans text_latex_wrapper_out

    # Effectuer les remplacements de chaînes de caractères
    replacements = {
        "%E>": "\\enonce{ %début énoncé \n",
        "%E<": "} % fin énoncé \n",
        "%C>": "\\correction{ %début correction \n",
        "%C<": "} % fin correction \n"
    }
    for old, new in replacements.items():
        text_content = text_content.replace(old, new)
    
    # Mettre à jour text_out_latex_wrapper avec le contenu remplacé
    text_out_latex_wrapper.delete("1.0", tk.END)
    text_out_latex_wrapper.insert("1.0", text_content)
    
    #Mettre à jour text_in_python_wrapper avec le contenu remplacé
    text_in_python_wrapper.delete("1.0", tk.END)
    text_in_python_wrapper.insert("1.0", text_content)
    lst_var,dico_var = find_substrings_var(text_content)
    # Attribuez la liste des valeurs à la propriété 'variables' du Combobox
    combo_box_liste_variables['values'] = lst_var
    dico_dsxl_python_wrapper["liste_variables"] =lst_var    
    save_text_wrappers_FULL_to_files()  
    

#========================== PARTIE GRAPHIQUE ======tab_latex_wrapper 
#Créer l'onglet "tab_dsxl_latex_wrapper"
tab_latex_wrapper = ttk.Frame(tabControl)
tabControl.add(tab_latex_wrapper, text='latex wrapper')
tabControl.pack(expand=True, fill="y")
# Documentation : tab_latex_wrapper  contient 
#
#   - frame_texts_latex_wrapper : qui contient deux zones de texte 
frame_texts_latex_wrapper = tk.Frame(tab_latex_wrapper)
frame_texts_latex_wrapper.pack(fill="both",expand = True,side = "top")
# Configurer les colonnes pour qu'elles s'adaptent à la largeur du frame
frame_texts_latex_wrapper.grid_columnconfigure(0, weight=1)
frame_texts_latex_wrapper.grid_columnconfigure(1, weight=1)
# Configurer la rangée pour qu'elle s'adapte en hauteur (la rangée au-dessus de bottom_frame)
frame_texts_latex_wrapper.grid_rowconfigure(0, weight=1)
#            text_in_latex_wrapper    &   text_out_latex_wrapper
text_in_latex_wrapper = tk.Text(frame_texts_latex_wrapper, height=10,font=desired_font)
text_in_latex_wrapper.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')  

text_out_latex_wrapper = tk.Text(frame_texts_latex_wrapper, height=10, font=desired_font)
text_out_latex_wrapper.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')


#
#   - frame_insert_buttons_latex_wrapper : qui contient 
#                les boutons : "%E>", "%E<", "%C>", "%C<", "\poids{} %en pourcentage","\\var{}{}" et "WRAP UP!"
#
labels_text = ["%E>", "%E<", "%C>", "%C<", "\poids{} %en pourcentage","\\var{}{}"]
frame_insert_buttons_latex_wrapper = tk.Frame(tab_latex_wrapper)
frame_insert_buttons_latex_wrapper.pack(fill="both")
# Définir les boutons pour inserer les commandes dans text_latex_wrapper_in 
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[0], command=lambda: insert_button_latex_wrapper_text_in(labels_text[0]))
button.pack(side='left', padx=5, pady=5, expand=True)
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[1], command=lambda: insert_button_latex_wrapper_text_in(labels_text[1]))
button.pack(side='left', padx=5, pady=5, expand=True)
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[2], command=lambda: insert_button_latex_wrapper_text_in(labels_text[2]))
button.pack(side='left', padx=5, pady=5, expand=True)
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[3], command=lambda: insert_button_latex_wrapper_text_in(labels_text[3]))
button.pack(side='left', padx=5, pady=5, expand=True)
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[4], command=lambda: insert_button_latex_wrapper_text_in(labels_text[4]))
button.pack(side='left', padx=5, pady=5, expand=True)
button = tk.Button(frame_insert_buttons_latex_wrapper, text=labels_text[5], command=lambda: insert_button_latex_wrapper_text_in(labels_text[5]))
button.pack(side='left', padx=5, pady=5, expand=True)
# Le bouton "wrapper" :
button_wrap_latex = tk.Button(frame_insert_buttons_latex_wrapper, text="WRAP UP!")
button_wrap_latex.pack(side='left', padx=5, pady=5, expand=True)
# Lier la fonction copy_and_replace à l'événement de clic sur le bouton
button_wrap_latex.config(command=command_button_wrap_latex_copy_and_replace)
#
#
#
#
#
#
#-----------------------------------------------------------------------------------------------

###############################################################################################
#                      TAB : tab_python_wrapper                 
###############################################################################################

# -----------------Evènements liés à :  tab_python_wrapper 
#
#   - frame1 : qui contient des entrée pour :
#           entry_nom_exercice, 
#           entry_date_creation, 
#           entry_source, 
#           combo_box_liste_notions
#           combo_box_liste_variables
#
#   - frame2 : qui contient deux zones de texte 
#            text_in_python_wrapper    &   text_out_python_wrapper
#

#   - frame3 qui contient : label_liste_notions_choisies_contenu, button_wrapper_python
#     
#
def save_text_python_wrapper_in_to_file() :
    # Copier le texte de text_python_wrapper_in 
    text_content = text_in_python_wrapper.get("1.0", tk.END)
    output_file_path = "./parametres_dsxl/dsxl_python_wrapper/"+dico_dsxl_python_wrapper["nom_exercice"]+".tex"
    with open(output_file_path, 'w') as file:
        file.write(text_content)

# Chaine de caractères pour liste :
def str_liste_vers_chaine_caractere(liste) :  
    print(liste)
    str_list = " [ "
    if len(liste)==0 :
        return ' [ ] '
    for i in range(len(liste)-1) :
        item = liste[i]
        str_list = str_list +"'"+item+"'"+' , '
    item = liste[-1]    
    str_list = str_list +"'"+item+"'"+' ]'
    return str_list

# creation commandes append à liste_liste_parametres :
def creation_commandes_append_liste_liste_parametres(liste) :
    text_append = "\n"    
    # Déclaration des variables : 
    for item in liste :
        var_name = item[: item.find(':')]
        var_value = item[item.find(':')+1:]
        text_append = text_append+'    '+var_name+" = "+var_value+" \n"
        text_append = text_append+'    '+"str_"+var_name+" = str("+var_name+") \n"
    # fonction append : 
    if len(liste)>0 : 
        text_append = text_append+'    \n'+"    liste_liste_parametres.append( [ "
        for i in range(len(liste)-1) :
            item = liste[i]
            var_name = item[: item.find(':')]
            text_append = text_append+"'"+var_name+":'" + "+str_"+var_name+' , '
        item = liste[-1] 
        var_name = item[: item.find(':')]
        text_append = text_append+"'"+var_name+":'"+"+"+"str_"+var_name+' ]) \n \n' 
    return text_append
    
def command_python_wrapper() :
    ''' command_python_wrapper() actualise dico_dsxl_python_wrapper
    ''' 
    # Actualise dico_dsxl_python_wrapper :
    dico_dsxl_python_wrapper["nom_exercice"] = entry_nom_exercice.get()
    dico_dsxl_python_wrapper["date_creation"] = entry_date_creation.get()
    dico_dsxl_python_wrapper["source"] = entry_source.get()
    list_variables = dico_dsxl_python_wrapper["liste_variables"]
    print(list_variables)
    list_variables_sans_etoile = []
    for item in list_variables :
        if item[0] != '*' :
            list_variables_sans_etoile.append(item)            
    dico_dsxl_python_wrapper["liste_variables"] = list_variables_sans_etoile

def command_button_nouvelle_fonction_python() :
    '''command_button_nouvelle_fonction_python() 
        1) actualise dico_dsxl_python_wrapper et 
        2) propose une nouvelle fonction python
    '''
    # Actualise dico_dsxl_python_wrapper :
    dico_dsxl_python_wrapper["nom_exercice"] = entry_nom_exercice.get()
    dico_dsxl_python_wrapper["date_creation"] = entry_date_creation.get()
    dico_dsxl_python_wrapper["source"] = entry_source.get()
    list_variables = dico_dsxl_python_wrapper["liste_variables"]
    print(list_variables)
    list_variables_sans_etoile = []
    for item in list_variables :
        if item[0] != '*' :
            list_variables_sans_etoile.append(item)            
    dico_dsxl_python_wrapper["liste_variables"] = list_variables_sans_etoile
    print(list_variables_sans_etoile)
        
    str_list_notions =  str_liste_vers_chaine_caractere(dico_dsxl_python_wrapper["liste_notions"])  
    str_list_variables =  str_liste_vers_chaine_caractere(dico_dsxl_python_wrapper["liste_variables"])  
    str_la_question = 'Recommancer une nouvelle fonction fonction_param_exercice()?'
    reponse  = ask_user(str_la_question)
    if reponse =='yes' : 
        str_la_question = 'Etes-vous sur?' 
        reponse  = ask_user(str_la_question)
        if reponse =='yes' :
            text_append = creation_commandes_append_liste_liste_parametres(dico_dsxl_python_wrapper["liste_variables"])
            text_python = "def fonction_param_exercice() : \n\n"+\
                        "    dico_exercice = {\n" +\
                        "        'nom_exercice'"+ ": '"+dico_dsxl_python_wrapper["nom_exercice"] +"' ,\n"+\
                        "        'date_creation'"+ ": '"+dico_dsxl_python_wrapper["date_creation"] +"' ,\n"+\
                        "        'source'"+ ": '"+dico_dsxl_python_wrapper["source"] +"' ,\n"+\
                        "        'liste_notions' : "+str_list_notions+" , \n"+\
                        "        'liste_variables' : "+str_list_variables+"\n"+\
                        "        }\n\n \n" +\
                        "    liste_liste_parametres = [ "+str_list_variables+" ] \n\n"+ \
                        "    # Votre code ici :\n\n\n\n\n"+\
                        text_append+'\n\n'+\
                        "    return dico_exercice, liste_liste_parametres \n\n\n"+\
                        "# Les lignes suivantes sont à supprimer après la phase de test : \n"+\
                        "dico_exercice, liste_liste_parametres = fonction_param_exercice() \n"+\
                        "list_defaut_param =dico_exercice['liste_variables'] \n"+\
                        "for i in range(len(liste_liste_parametres[0])) :\n"+\
                        "    print('valeurs par defaut --> '+list_defaut_param[i]+' | '+liste_liste_parametres[1][i]+'  <---votre valeur : ' )\n\n\n"



            # Mettre à jour text_out_python_wrapper avec le contenu remplacé
            text_out_python_wrapper.delete("1.0", tk.END)
            text_out_python_wrapper.insert("1.0", text_python)
    
#========================== PARTIE GRAPHIQUE ======"tab_python_wrapper"    
#Créer l'onglet "tab_python_wrapper"

tab_python_wrapper = ttk.Frame(tabControl)
tabControl.add(tab_python_wrapper, text='python wrapper')
tabControl.pack(expand=1, fill="both")
#tab_dsxl_python_wrapper.bind("<KeyPress>",commande_initialisation_tab_dsxl_python_wrapper)

# --------------------Première ligne

frame1 = tk.Frame(tab_python_wrapper)
frame1.pack(fill="x")

# Champs de la première ligne
label_nom_exercice = ttk.Label(frame1,text = "Nom exercice : ")
entry_nom_exercice = ttk.Entry(frame1)
label_date_creation = ttk.Label(frame1,text = "Date création : ")
entry_date_creation = ttk.Entry(frame1)
label_source = ttk.Label(frame1,text = "Source : ")
entry_source = ttk.Entry(frame1)

# Liste déroulante avec notion à selectionner : 
label_liste_notions = ttk.Label(frame1,text = "Liste notions : ")
combo_box_liste_notions = ttk.Combobox(frame1)  # Vous devrez implémenter les cases à cocher séparément
label_liste_variables = ttk.Label(frame1,text = "Liste variables : ")
combo_box_liste_variables = ttk.Combobox(frame1)

def action_liste_variables(event):
    # Obtenir l'élément sélectionné
    select_notion = event.widget.get()
    print(select_notion)
    if select_notion in dico_dsxl_python_wrapper["liste_notions"] :
        # On enlève la notion : 
        lst_temp = dico_dsxl_python_wrapper["liste_notions"]
        lst_temp.remove(select_notion)
        dico_dsxl_python_wrapper["liste_notions"] =lst_temp 
    else : 
        # On ajoute la notion :
        lst_temp = dico_dsxl_python_wrapper["liste_notions"]
        lst_temp.append(select_notion)
        dico_dsxl_python_wrapper["liste_notions"] =lst_temp
    # On actualise l'affichage : 
    str_liste_notions_choisies = liste_notions_choisies_to_str(lst_temp)
    print(str_liste_notions_choisies)
    label_liste_notions_choisies_contenu.configure(text= str_liste_notions_choisies) 
    
# Action liée au choix d'une notion : 
combo_box_liste_notions.bind("<<ComboboxSelected>>", action_liste_variables)




# Placement des champs de la première ligne
for widget in (label_nom_exercice,entry_nom_exercice, label_date_creation, entry_date_creation,\
        label_source, entry_source,label_liste_notions, combo_box_liste_notions, label_liste_variables, combo_box_liste_variables):
    widget.pack(side="left", expand=True, padx=5)

# -------------------------Seconde ligne


frame2 = tk.Frame(tab_python_wrapper)
frame2.pack(fill="both", expand=True)

# Zones de texte de la seconde ligne
text_in_python_wrapper = tk.Text(frame2)
text_out_python_wrapper = tk.Text(frame2)

# Placement des zones de texte de la seconde ligne
text_in_python_wrapper.pack(side="left", expand=True, fill="both", padx=5)
text_out_python_wrapper.pack(side="left", expand=True, fill="both", padx=5)

# --------------------------Troisième ligne


frame3 = tk.Frame(tab_python_wrapper)
frame3.pack(fill="both", expand=False)
# Label liste notions choisies :
label_liste_notions_choisies = ttk.Label(frame3,text = "Notions choisies : ")
label_liste_notions_choisies.pack(side='left', padx=5, pady=5, expand=False)

label_liste_notions_choisies_contenu = ttk.Label(frame3,text = str_liste_notions_choisies)
label_liste_notions_choisies_contenu.pack(side='left', padx=5, pady=5, expand=True)

# Le bouton "wrapper" :
button_wrapper_python = tk.Button(frame3, text="WRAP UP!")
button_wrapper_python.pack(side='left', padx=5, pady=5, expand=True)
button_wrapper_python.config(command=command_python_wrapper)

# Le bouton "nouvelle_fonction" :
button_nouvelle_fonction_python = tk.Button(frame3, text="Nouvelle fonction python")
button_nouvelle_fonction_python.pack(side='left', padx=5, pady=5, expand=True)
button_nouvelle_fonction_python.config(command=command_button_nouvelle_fonction_python)
#
#
#
#
#
#
#-----------------------------------------------------------------------------------------------

###############################################################################################
#                      TAB : tab_exercice_test                 
###############################################################################################
# -----------------Evènements liés à :  tab_test_exercice
#
#   - frame_test_1 : qui contient des entrée pour :
#           label_test_nom_exercice, 
#           label_test_date_creation, 
#           label_test_source, 
#           combo_box_liste_notions
#           combo_box_liste_variables
#
#   - frame_test_2 : qui contient :
#           combo_test_box_mode_E_C
#           combo_test_liste_parametres 
#           button_test_full_latex 
#
#   - frame_test_3 qui contient deux zones de texte : 
#           text_test_param_python    &   text_latex_main_test
    
    
    
def python_tab_test_load_variables(event) :  
    '''python_tab_test_load_variables(event) s'effectue en cliquant sur le bouton button_test_load_python_module
       Cette procedure :
           1) Regarde si le fichier fonction_param_exercice_test.py existe à la racine
               a) Si oui, il charge le module text_python_test
               b) Si non il fait une copie de './dsxl_tex_exercice/dsxl_text_python_wrapper_out.py' à la racine qu'il nomme fonction_param_exercice_test.py 
           2) Regarde si le fichier latex_main_exercice_test.tex existe à la racine
               a) Si oui, il copie le contenu sur la zone de texte text_latex_main_test
               b) Si non il fait une copie de './dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex' à la racine qu'il nomme latex_main_exercice_test.tex
           3) Il copie  fonction_param_exercice_test.py dans la zone de text du widget text_fonction_param_exercice_test 
           4) Il copie  latex_main_exercice_test.tex dans la zone de text du widget text_latex_main_exercice_test
           5) Il charge le module fonction_param_exercice_test          
           6) Il execute :  dico_exercice, liste_liste_parametres_exercice = fonction_param_exercice()
           7) Il charge les widgets : label_test_nom_exercice, label_test_date_creation, label_test_source, combo_box_liste_parametres
    '''
    # 1) Regarde si le fichier latex_main_exercice_test.tex existe à la racine
    if os.path.exists('./fonction_param_exercice_test.py'):
        with open('./fonction_param_exercice_test.py', 'r') as file:
            content = file.read()
            text_python_test.delete(1.0, tk.END)
            text_python_test.insert(1.0, content)
    else : # Le fichier './fonction_param_exercice_test.py' n'existe pas :         
        if os.path.exists('./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py'):
            with open('./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py', 'r') as file:
                content = file.read()
                text_python_test.delete(1.0, tk.END)
                text_python_test.insert(1.0, content)
            # On crée './fonction_param_exercice_test.py' :
            with open('./fonction_param_exercice_test.py', 'w') as file:
                file.write(content)
        else : # Aucun des deux fichiers n'existe
            w = Label(root, text ='./fonction_param_exercice_test.py'+'\n'+'./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py'+'\n'+"n'existent pas!", font = "50")  
            w.pack() 
            messagebox.showinfo("showinfo", "Information") 
            return 
    # 2) Regarde si le fichier latex_main_exercice_test.tex existe à la racine
    if os.path.exists('./latex_main_exercice_test.tex'):
        with open('./latex_main_exercice_test.tex', 'r') as file:
            content = file.read()
            text_latex_main_test.delete(1.0, tk.END)
            text_latex_main_test.insert(1.0, content)
    else : # Le fichier './latex_main_exercice_test.tex' n'existe pas :         
        if os.path.exists('./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex'):
            with open('./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex', 'r') as file:
                content = file.read()
                text_latex_main_test.delete(1.0, tk.END)
                text_latex_main_test.insert(1.0, content)
            # On crée './latex_main_exercice_test.tex' :
            with open('./latex_main_exercice_test.tex', 'w') as file:
                file.write(content)
        else : # Aucun des deux fichiers n'existe
            w = Label(root, text ='./latex_main_exercice_test.tex'+'\n'+'./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex'+'\n'+"n'existent pas!", font = "50")  
            w.pack() 
            messagebox.showinfo("showinfo", "Information") 
            return 
        
        
    # 5) Il charge le module fonction_param_exercice_test      
    # On charge le module : https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
    import fonction_param_exercice_test 
    reload(fonction_param_exercice_test)

    #dico_exercice, liste_liste_parametres  = fonction_param_exercice_test.fonction_param_exercice()
    #6) Il execute :  dico_exercice, liste_liste_parametres_exercice = fonction_param_exercice()
    dico_exercice, liste_liste_parametres_exercice = fonction_param_exercice_test.fonction_param_exercice()

    print(dico_exercice)
    #print(liste_liste_parametres_exercice)
    label_test_nom_exercice["text"] = 'Nom exercice : '+ dico_exercice['nom_exercice']
    label_test_date_creation["text"] = 'Date création : '+ dico_exercice['date_creation']
    label_test_source["text"] = 'Source : '+ dico_exercice['source']
    print(str_liste_vers_chaine_caractere(liste_liste_parametres_exercice[0]))
    liste_str_liste_parametres_exercice = [str(i)+'->'+str_liste_vers_chaine_caractere(liste_liste_parametres_exercice[i]) for i in range(len(liste_liste_parametres_exercice))]    
    combo_box_liste_parametres['values'] = liste_str_liste_parametres_exercice
    
#========================== PARTIE GRAPHIQUE ======"tab_exercice_test"
#Créer l'onglet "tab_exercice_test"

tab_exercice_test = ttk.Frame(tabControl)
tabControl.add(tab_exercice_test, text=' Testing Exercise')
tabControl.pack(expand=1, fill="both")

# --------------------Première ligne

frame_test_1 = tk.Frame(tab_exercice_test)
frame_test_1.pack(fill="x")

#-----------------------> Champs de la première ligne
button_test_load_python_module =  tk.Button(frame_test_1, text="Load 'dsxl_text_python_wrapper_out.py' exercise module ")
label_test_nom_exercice = ttk.Label(frame_test_1,text = "Nom exercice : "+dico_dsxl_python_wrapper["nom_exercice"])
label_test_date_creation = ttk.Label(frame_test_1,text = "Date création : "+dico_dsxl_python_wrapper["date_creation"])
label_test_source = ttk.Label(frame_test_1,text = "Source : "+dico_dsxl_python_wrapper["source"])

# Placement des champs de la première ligne
for widget in (button_test_load_python_module, label_test_nom_exercice, label_test_date_creation, label_test_source):
    widget.pack(side="left", expand=True, padx=5)

button_test_load_python_module.bind("<Button>",python_tab_test_load_variables)

#----------------------->Champs de la seconde ligne :

frame_test_2 = tk.Frame(tab_exercice_test)
frame_test_2.pack(fill="x")

def radio_button_sel():   
    print( "You selected the option " + var.get())
    global mode_exercice
    mode_exercice = var.get()
    print('mode_exercice =',mode_exercice)
    #label.config(text = selection)
    
def action_liste_parametres(event) :
    ''' Action : 
        1) Obtenir l'élément sélectionné
        2) Regarder si il est dans la liste  liste_param_test_choix
            a) Si oui, l'enlever
            b) Si non, l'inclure
        3) Actualiser la valeur du widget label_list_parametres_test      
    '''
    # Obtenir l'élément sélectionné
    select_notion = event.widget.get()
    i = select_notion.find('->')
    print(select_notion[:i])
    param_num =  int(select_notion[:i])
    dico_exercice["choix_num_param"] =  param_num
    
    if param_num in liste_param_test_choix :
        liste_param_test_choix.remove(param_num)
    else : 
        liste_param_test_choix.append(param_num)

    # Préparer l'affichage : 
    str_lst_param = '[ '
    for i in liste_param_test_choix :
        str_lst_param = str_lst_param +'  '+str(i)
    str_lst_param = str_lst_param +' ]'    
    label_list_parametres_test["text"] = "List param selection : "+str_lst_param 
    
var = tk.StringVar()
radio_button_enonce = tk.Radiobutton(frame_test_2, text="mode énoncé", variable=var, value='E', command=radio_button_sel)
radio_button_enonce.pack(side="left", expand=False, padx=5)
radio_button_corrige = tk.Radiobutton(frame_test_2, text="mode corrigé", variable=var, value='C', command=radio_button_sel)
radio_button_corrige.pack(side="left", expand=False, padx=5)
combo_box_liste_parametres = ttk.Combobox(frame_test_2,width=100)  
combo_box_liste_parametres.pack(side="left", expand=True, padx=5)
label_list_parametres_test = ttk.Label(frame_test_2,text = "List param selection : []")
label_list_parametres_test.pack(side="left", expand=True, padx=5)

# Action liée au choix d'une notion :                                 
combo_box_liste_parametres.bind("<<ComboboxSelected>>", action_liste_parametres)  

#-----------------------> Champs de la troisieme ligne :

frame_test_3 = tk.Frame(tab_exercice_test)
frame_test_3.pack(fill="x")
# Zones de texte de la 3eme ligne
text_python_test = tk.Text(frame_test_3)
text_latex_main_test = tk.Text(frame_test_3)

# Placement des zones de texte de la 3eme ligne
text_python_test.pack(side="left", expand=True, fill="both", padx=5)
text_latex_main_test.pack(side="left", expand=True, fill="both", padx=5)

#-----------------------> Champs de la quatrieme ligne :
def insert_button_latex_commands(text):
    text_latex_main_test.insert(tk.INSERT, text)


list_latex_commands=["\\NouvellePageModeEnonce","\\NouvellePageModeCorrection","\\SeulementModeEnonce{}","\\SeulementModeCorrection{}"]

frame_test_4 = tk.Frame(tab_exercice_test)
frame_test_4.pack(fill="x")

# Définir les boutons pour inserer les commandes dans text_latex_main_test 
button_0 = tk.Button(frame_test_4, text=list_latex_commands[0], command=lambda: insert_button_latex_commands(list_latex_commands[0]))
button_0.pack(side='left', padx=5, pady=5, expand=True)
button_1 = tk.Button(frame_test_4, text=list_latex_commands[1], command=lambda: insert_button_latex_commands(list_latex_commands[1]))
button_1.pack(side='left', padx=5, pady=5, expand=True)
button_2 = tk.Button(frame_test_4, text=list_latex_commands[2], command=lambda: insert_button_latex_commands(list_latex_commands[2]))
button_2.pack(side='left', padx=5, pady=5, expand=True)    
button_3 = tk.Button(frame_test_4, text=list_latex_commands[3], command=lambda: insert_button_latex_commands(list_latex_commands[3]))
button_3.pack(side='left', padx=5, pady=5, expand=True)  
              
#-----------------------> Champs de la 5eme ligne :

def command_create_full_latex():
    print('button pressed')
    from fonction_param_exercice_test import fonction_param_exercice
    reload(fonction_param_exercice_test)
    dico_exercice, liste_liste_parametres  = fonction_param_exercice()
    file_path='./parametres_dsxl/Latex_head_dsxl_commandes.tex'
    target_latex_file = './dsxl_tex_exercice/latex_test_full_text_mode_'+mode_exercice+\
            '/latex_test_full_text_'+mode_exercice+'.tex'
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
    # Use a regular expression to find and replace the character Y with X
    # Assuming that Y is any single character and not a sequence or special regex character
    pattern = r'(\\newcommand{\\EnonceCorrection}{).(?=})'
    head_content = re.sub(pattern, r'\g<1>' + mode_exercice, content)
    mode_test=True
    content = head_content + "\n\\begin{document}\n" 
    points = 5
    Ex_choix = Exercice(dico_exercice, liste_liste_parametres,mode_test=mode_test)
    print(liste_param_test_choix,mode_exercice)
    for num_param in liste_param_test_choix :        
        texte_modifie = Ex_choix.genere_code_latex(num_param, points)
        content = content+ "\n\n"+ texte_modifie
    # Préparer le contenu final
    final_content =  content + "\n\\end{document}\n"  
    #print(final_content)
    with open(target_latex_file, 'w') as file:
        file.write(final_content)

def command_sauvegarde_fonction_param_exercice_test() :
    text_content = text_python_test.get("1.0", tk.END)
    output_file_path = "./fonction_param_exercice_test.py"
    with open(output_file_path, 'w') as file:
        file.write(text_content)
    reload(fonction_param_exercice_test)

def command_sauvegarde_latex_main_exercice_test() :
    text_content = text_latex_main_test.get("1.0", tk.END)
    output_file_path = "./latex_main_exercice_test.tex"
    with open(output_file_path, 'w') as file:
        file.write(text_content)

        
frame_test_5 = tk.Frame(tab_exercice_test)
frame_test_5.pack(fill="x")

# Sauvegarder latex_main_exercice_test.tex
button_sauvegarde_fonction_param_exercice = tk.Button(frame_test_5, text="Sauvegarde fonction_param_exercice_test.py", command=lambda: command_sauvegarde_fonction_param_exercice_test())
button_sauvegarde_fonction_param_exercice.pack(side='left', padx=5, pady=5, expand=True)   

# Définir les boutons pour inserer les commandes dans text_latex_main_test 
button_create_full_latex = tk.Button(frame_test_5, text="Création code Latex", command=lambda: command_create_full_latex())
button_create_full_latex.pack(side='left', padx=5, pady=5, expand=True)            

# Sauvegarder latex_main_exercice_test.tex
button_sauvegarde_latex_main_exercice_test = tk.Button(frame_test_5, text="Sauvegarde latex_main_exercice_test.tex", command=lambda: command_sauvegarde_latex_main_exercice_test())
button_sauvegarde_latex_main_exercice_test.pack(side='left', padx=5, pady=5, expand=True)               



###############################################################################################
# ================== INITIALISATION DU PROGRAMME ET DE QUELQUES VARIABLES =====================
###############################################################################################

# Remarque : Les variables liste_fichiers_text_wrapper et Liste_fichiers_text_wrapper_full nécessitent que 
#    les widgets text_in_latex_wrapper, text_out_latex_wrapper, text_in_python_wrapper et text_out_python_wrapper
#    existent déjà. Elles ne peuvent donc pas être déplacées au début du code dans la partie variables globales. 

mode_exercice = 'C'
liste_param_test_choix = [0]
liste_fichiers_text_wrapper = [["./dsxl_tex_exercice/dsxl_text_latex_wrapper_in.tex",text_in_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_latex_wrapper_out.tex",text_out_latex_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_in.tex",text_in_python_wrapper],
                 ["./dsxl_tex_exercice/dsxl_text_python_wrapper_out.py",text_out_python_wrapper]]

Liste_fichiers_text_wrapper_full = \
                [["./dsxl_tex_exercice/latex_wrapper_in_full/dsxl_text_latex_wrapper_in.tex",text_in_latex_wrapper],
                 ["./dsxl_tex_exercice/latex_wrapper_out_full/dsxl_text_latex_wrapper_out.tex",text_out_latex_wrapper],
                 ["./dsxl_tex_exercice/python_wrapper_in_full/dsxl_text_python_wrapper_in.tex",text_in_python_wrapper]]

dico_dsxl_python_wrapper,str_liste_notions_choisies = python_wrapper_load_variables()
dico_exercice = {}

## https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
#sys.path.append('./DSXLmodule') 
#from DSXLmodule import fonction_param_exercices,class_exercice
if os.path.exists("./fonction_param_exercice_test.py") :
    print("./fonction_param_exercice_test.py EXISTS!")
    import fonction_param_exercice_test


# Fonction pour charger les contenu des fichiers dans les zones text_*_wrapper_*
load_file_to_text_wrappers()

#=======================================================================================
#---------------------------- ACTIONS A la fermeture -------------------------------------
#========================================================================================

# Configurer la sauvegarde à la fermeture
root.protocol("WM_DELETE_WINDOW", lambda: [save_text_wrappers_to_files(),\
 python_wrapper_save_variables(),save_text_wrappers_FULL_to_files(),  root.destroy()])




###############################################################################################
#----------------------------------Exécuter la boucle principale
###############################################################################################

root.mainloop()

