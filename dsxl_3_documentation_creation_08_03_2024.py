#!/usr/bin/env python
import os
import json
import pandas as pd
# Module pour traiter les expressions régulières 
import re
import sys
import numpy as np
from fractions import Fraction
import math
#https://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
from importlib import reload


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
#reload(list_function_param_exercices)
#Ex_001 = Exercice(list_of_fonction_param_exercices[0] )
#print(list_of_dico_exercices)
# print(Exercice._registry)

nom_ficher_LISTES_EXERCICES = './Documentation_generee_DSXL/input_files/DSXL_3_doc_and_exercices_LISTES_EXERCICES.tex' 
text_LISTES_EXERCICES = "\n"
num_param = 0
points = 10
for exerciceobject in Exercice._registry:
    print (exerciceobject.liste_notions)
    print (exerciceobject.nom_exercice)
    # Ex_choix = Exercice(dico_exercice, liste_liste_parametres,mode_test=mode_test)
    #print(liste_param_test_choix,mode_exercice)       
    
    nom_exercice_modifie = 'Exercice\\_'+exerciceobject.nom_exercice[exerciceobject.nom_exercice.find('_')+1:]
    print(nom_exercice_modifie)
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\section{"+nom_exercice_modifie+'}'+'\n\n'
    for notion in exerciceobject.liste_notions :
        text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\index[notions]{"+notion+'}'+'\n'
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\begin{description}\n"
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\item[Date de création : ]"+exerciceobject.date_creation+'\n'
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\item[Source : ]"+exerciceobject.source+'\n'
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\item[Liste des notions : ]"
    for notion in exerciceobject.liste_notions :
        text_LISTES_EXERCICES = text_LISTES_EXERCICES+notion+' : '
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+'\n'    
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\item[Nombre de variantes de l'exercice : ]"+\
                                        str(len(exerciceobject.liste_liste_parametres))+'\n'
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\end{description}\n\n"
    #text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\index{"+notion+'}'+'\n' 
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+"\\centerline{\\bf\\large Barème utilisé pour l'exercice : "+str(points)+\
                    " points / paramètre utilisé : numéro "+str(+num_param)+'}\n\n' 
    texte_modifie = exerciceobject.genere_code_latex(num_param, points)    
    text_LISTES_EXERCICES = text_LISTES_EXERCICES+ "\n\n"+ texte_modifie
  
    #print(final_content)
    
with open(nom_ficher_LISTES_EXERCICES, 'w') as file:
    file.write(text_LISTES_EXERCICES)
