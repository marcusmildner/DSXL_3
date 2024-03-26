#!/usr/bin/env python
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
from pathlib import Path
import random

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
root.title("DSXL 3 : création devoirs")

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

def remplace_Underscore8_par_BackslashUnderscore8(str_chaine) :
    str_chaine_for_latex =''
    for charactere in str_chaine :
        if charactere =='_' :
            str_chaine_for_latex =str_chaine_for_latex+'\_'
        else :
            str_chaine_for_latex =str_chaine_for_latex+charactere
    return str_chaine_for_latex


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

def Liste_sous_repertoires_fichiers_extension(chemin,extension = 'csv') :
    dico_sous_repertoires_fichiers_extension = {}
    # List all subdirectory using pathlib
    basepath = Path(chemin)
    for entry in basepath.iterdir():
        if entry.is_dir():
            print('Directories :',entry.name) 
            sous_repertoires =entry.name
            liste_fichiers_extension = []
            # List all files in directory using pathlib
            basepath2 = Path(chemin+'/'+entry.name)
            files_in_basepath2 = (entry2 for entry2 in basepath2.iterdir() if entry2.is_file())
            for item in files_in_basepath2:
                print(item.name) 
                if extension in item.name.lower() :
                    liste_fichiers_extension.append(item.name)
            dico_sous_repertoires_fichiers_extension[sous_repertoires] = liste_fichiers_extension
    return dico_sous_repertoires_fichiers_extension

def trouve_numero_exercice(str_nom) :
    i = str_nom.find('_')
    if i ==-1 :
        return 'no _ found'
    else:
        return(str_nom[i+1:])

def retourne_list_objetsexercices_de_list_exercices(list_exercice) :
    '''list_exercice contient des entrées de la forme 'Ex_001 : 10', etc...
        Cette fonction récupère l'objetexercice et le stocke dans list_objetsexercices.
        Si l'objetexercice n'est pas trouvé, il y aura None comme entrée. 
        Remarque : 
        a) un DM, DS peut avoir plusieurs fois le même exercice. 
        b) exerciceobject.nom_exercice a le format 'exercice_XXX' où XXX est le numéro de l'exercice. 
    '''
    list_objetsexercices = [None]*len(list_exercice)
    for exerciceobject in Exercice._registry:
        exercice_numero = trouve_numero_exercice(exerciceobject.nom_exercice)
        if exercice_numero == 'no _ found' :
            print("Attention le nom d'un de l'exercice "+exerciceobject.nom_exercice+\
                  "n'a pas un format correct!")
        else : 
            for k in range(len(list_exercice)) :
                if list_exercice[k].find(exercice_numero) != -1 : 
                    list_objetsexercices[k] = exerciceobject
        #print (exerciceobject.liste_notions)
    return list_objetsexercices
################################ INITIALISATION ###############################################



chemin = './donnees_exercices'
extension = 'csv'
dico_sous_repertoires_fichiers_extension = \
        Liste_sous_repertoires_fichiers_extension(chemin,extension = 'csv')
print(dico_sous_repertoires_fichiers_extension)

################################# tabControl ##################################################

#Créer le contrôle d'onglets (Notebook)
tabControl = ttk.Notebook(root)

###############################################################################################
#                      TAB : tab_niveaux_et_classes                
###############################################################################################
tab_niveaux_et_devoirs = ttk.Frame(tabControl)
tabControl.add(tab_niveaux_et_devoirs, text='Niveaux / devoirs')
tabControl.pack(expand=True, fill="y")

# -----------------Commandes liées à :  tab_niveaux_et_devoirs 
def selection_classe(chemin) :
    global list_entry_ligne_colonne 
    global list_objetsexercices
    global nombre_colonnes
    global nombre_lignes
    df_devoir = pd.read_csv('./donnees_exercices/'+chemin)
    liste_etiquettes = list(df_devoir.columns)
    nombre_colonnes = len(liste_etiquettes)
    nombre_lignes = len(df_devoir)+1 # <-- ligne étiquettes à ajouter 
    # La 1ere ligne du tableau : 
    list_ligne_colonne = [liste_etiquettes]
    liste_entry_etiquettes =[]
    for j in range(nombre_colonnes) :
        entry_etiquette = tk.Entry(frame_CSV_file_parametres)
        entry_etiquette.insert(0, liste_etiquettes[j]) 
        entry_etiquette.grid(row=0,column=j)
        liste_entry_etiquettes.append(entry_etiquette)
    list_entry_ligne_colonne = [liste_entry_etiquettes]
    # Les lignes qui correspondent aux élèves : 
    for i in df_devoir.index : 
        ligne_entry = []
        ligne = []
        for j in range(nombre_colonnes) :
            etiquette = liste_etiquettes[j]
            ligne.append(df_devoir[etiquette][i])
            entry_etiquette = tk.Entry(frame_CSV_file_parametres)
            entry_etiquette.insert(0, df_devoir[etiquette][i]) 
            entry_etiquette.grid(row=i+1,column=j,sticky=tk.EW)
            ligne_entry.append(entry_etiquette)
        list_ligne_colonne.append(ligne)
        list_entry_ligne_colonne.append(ligne_entry)
    #print(list_ligne_colonne)
    # Ligne num max param :
    list_label_caption = []
    list_label_caption.append('num max param :')
    list_labels = []
    label_num_max_param = tk.Label(frame_CSV_file_parametres, text='num max param :')
    label_num_max_param.grid(row=nombre_lignes+1,column=0,sticky=tk.EW)
    list_labels.append(label_num_max_param)
    for j in range(1,nombre_colonnes) :
        label_num_max_param = tk.Label(frame_CSV_file_parametres, text='---')
        label_num_max_param.grid(row=nombre_lignes+1,column=j,sticky=tk.EW)
        list_labels.append(label_num_max_param)
    # On cherche les exerciceobjet des exercices du devoir : 
    list_exercice = liste_etiquettes[1:-2]
    print('list_exercice =',list_exercice)
    list_objetsexercices = retourne_list_objetsexercices_de_list_exercices(list_exercice)
    print('list_objetsexercices =',list_objetsexercices)
    for k in range(len(list_objetsexercices)) : 
        if list_objetsexercices[k] == None :
            list_labels[k+1].config(text = 'Not found')
        else :
            list_labels[k+1].config(text = str(len(list_objetsexercices[k].liste_liste_parametres)-1))
            
        
    
#========================== PARTIE GRAPHIQUE =================
liste_frames_niveaux = []
for niveau in dico_sous_repertoires_fichiers_extension :
    frame_niveau = tk.Frame(tab_niveaux_et_devoirs)
    frame_niveau.pack(fill="both",expand = True,side = "top")
    liste_frames_niveaux.append(frame_niveau)
    # Champs de la première ligne
    label_niveau = ttk.Label(frame_niveau,text = niveau+" : ")
    label_niveau.pack(fill="both",expand = True,side = "left")
    for devoir in dico_sous_repertoires_fichiers_extension[niveau] :
        chemin = niveau+'/'+devoir
        button_devoir = tk.Button(frame_niveau, text=devoir, command=lambda: selection_classe(chemin))
        button_devoir.pack(side='left', padx=5, pady=5, expand=True)

###############################################################################################
#                      TAB : devoir_parametres                
###############################################################################################
def renew_all_exercices_param() :
    for i in range(1 , nombre_lignes):
        for j in range(1,len(list_objetsexercices)+1) :
            if list_objetsexercices[j-1] != None :
                max_param = len(list_objetsexercices[j-1].liste_liste_parametres)-1
                choix_param = random.randint(1, max_param)
                entry = list_entry_ligne_colonne[i][j]
                entry.delete(0, tk.END)
                entry.insert(0, str(choix_param))

def  save_all_exercice_param() :
    liste_champs = []
    for j in range(nombre_colonnes) :
        champs = list_entry_ligne_colonne[0][j].get()
        liste_champs.append(champs)
    print("champs = ",champs)    
    df_devoir_save = pd.DataFrame(columns = liste_champs)
    for i in range(1,nombre_lignes) :
        dico_valeurs_ligne = {}
        for j in range(nombre_colonnes) :
            dico_valeurs_ligne[liste_champs[j]] = [list_entry_ligne_colonne[i][j].get()]
        print( dico_valeurs_ligne)   
        # https://saturncloud.io/blog/how-to-append-a-row-to-pandas-dataframe-using-pandasconcat/
        df_devoir_save = pd.concat([df_devoir_save, pd.DataFrame(dico_valeurs_ligne)], ignore_index=True)
    str_la_question = 'Voulez-vous écraser le fichier '+'./donnees_exercices/'+chemin+' ?'    
    reponse = ask_user(str_la_question)
    if reponse =='yes' :
        reponse2 = ask_user('Vous êtes sur?')
        if reponse2=='yes' : 
            df_devoir_save.to_csv('./donnees_exercices/'+chemin, index=False)           
    
def latex_code_generate() :
    str_la_question = "Le code Latex sera généré à partir des données du fichier"+'./donnees_exercices/'+chemin+'\n'\
                    +"Avez-vous saugardé les données du tableau?"
    reponse= ask_user(str_la_question)
    if reponse =='yes' :
        reponse2 = ask_user('Générer les fichier Latex (mode E et mode C) ?')
        if reponse2 =='yes' :
            generer = True
        else :
            generer = False
    else : 
        reponse2 = ask_user('Sauvegarder les données du tableau et générer les fichiers Latex (mode E et mode C) ? ')
        if reponse2 =='yes' :
            save_all_exercice_param()
            generer = True
        else :
            generer = False
    if generer :        
        file_path_head='./parametres_dsxl/Latex_head_dsxl_commandes.tex'
        # Open the file in read mode
        with open(file_path_head, 'r') as file:
            # Read the content of the file
            head_text = file.read()
        content = "% =========================================================================\n"
        content = content+ "% DEVOIR :"+'./donnees_exercices/'+chemin+'\n'
        content = content+ "% =========================================================================\n"
        content = content + head_text
        content = content + "\n\\begin{document}\n" 
        # On parcourt les élèves (lignes) 
        for i in range(1 , nombre_lignes):
            nom_eleve = list_entry_ligne_colonne[i][0].get()
            content = content +"{\\bf "+nom_eleve+" \\large   \\hfill  Mathématiques \\hfill   $ e^{i\\pi}+1=0$ }\n"
            content = content +"\\bigskip\n"
            content = content +"\\centerline{\\bf \\large "+remplace_Underscore8_par_BackslashUnderscore8(chemin)+"}\n"
            content = content +"\\bigskip \n"
            content = content +"\\COPY{0}{\\pointssujetTOTAL} \n"
            # Pour chaque élève on parcourt les exercices : 
            for j in range(0,len(list_objetsexercices)) :
                str_num_ex_points = list_entry_ligne_colonne[0][j+1].get()
                points = int(str_num_ex_points[str_num_ex_points.find(':')+1:])
                param_choix =  int(list_entry_ligne_colonne[i][j+1].get())
                Ex_choix = list_objetsexercices[j]
                texte_modifie = Ex_choix.genere_code_latex(param_choix, points)
                #texte_modifie = texte_modifie +'\\points{'+str(points)+'}\n\n'
                content = content+ "\n\n"+ texte_modifie
            # Nombre total de points : 
            content = content+ "\n\n \\AffichepointssujetTOTAL"
            # On ajoute les nouvelles pages qu'il faut :
            for s in range(int(list_entry_ligne_colonne[i][nombre_colonnes-1].get())) :
                content = content+ "\n\n \\NouvellePageModeEnonce \n\n"
            for s in range(int(list_entry_ligne_colonne[i][nombre_colonnes-2].get())) :
                content = content+ "\n\n \\NouvellePageModeCorrection\n\n"  
        content = content + "\n\\end{document}\n" 
        # Saving two version (E and C) of latex file : 
        print("Jusqu'ici tout va bien!")
        for mode_exercice in ['E','C'] : 
            # Use a regular expression to find and replace the character Y with X
            # Assuming that Y is any single character and not a sequence or special regex character
            pattern = r'(\\newcommand{\\EnonceCorrection}{).(?=})'
            content = re.sub(pattern, r'\g<1>' + mode_exercice, content)
            target_latex_file = './creation_devoir/mode_'+mode_exercice+\
                '/devoir_mode_'+mode_exercice+'.tex'
            with open(target_latex_file, 'w') as file:
                file.write(content)

#========================== PARTIE GRAPHIQUE =================
tab_devoir_parametres = ttk.Frame(tabControl)
tabControl.add(tab_devoir_parametres, text='Devoirs : Parametres')
tabControl.pack(expand=True, fill="y")
# Frame pour les buttons permettant de renouveller les parametres du devoir de la classe : 
frame_button_parametres = tk.Frame(tab_devoir_parametres)
frame_button_parametres.pack(fill="both",expand = True,side = "top")
button_renew_all_exercices_param = tk.Button(frame_button_parametres, text='Renouveller tous les paramètres des exercices', \
                                             command=lambda: renew_all_exercices_param())
button_renew_all_exercices_param.pack(side='left', padx=5, pady=5, expand=True)
button_save_changes = tk.Button(frame_button_parametres, text='Sauvegarder tous les paramètres des exercices', \
                                             command=lambda: save_all_exercice_param())
button_save_changes.pack(side='left', padx=5, pady=5, expand=True)
button_latex_code_generate = tk.Button(frame_button_parametres, text='Génerer code Latex pour les modes Enoncés et Corrigés', \
                                             command=lambda: latex_code_generate())
button_latex_code_generate.pack(side='left', padx=5, pady=5, expand=True)
# Frame pour representer le fichier CSV contenant les paramètres du devoir :
frame_CSV_file_parametres = tk.Frame(tab_devoir_parametres)
frame_CSV_file_parametres.pack(fill="both",expand = True,side = "top")   

#=======================================================================================
#---------------------------- ACTIONS A la fermeture -------------------------------------
#========================================================================================

# Configurer la sauvegarde à la fermeture
root.protocol("WM_DELETE_WINDOW", lambda: [root.destroy()])




###############################################################################################
#----------------------------------Exécuter la boucle principale
###############################################################################################

root.mainloop()

