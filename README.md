# DSXL_3
Un programme pour créer des exercices et des devoirs avec des valeurs numériques individualisées pour chaque élève/étudiant 

I. Objectifs : 

Depuis plusieurs années, mes élèves et étudiants travaillent sur des énoncés identiques, mais ayant des valeurs numériques différentes. 

Procéder ainsi a de nombreux avantages : 

1. On ne peut pas simplement recopier la solution d'un camarade car tous les calculs sont à refaire,
2. Le travail en groupe est facilité, car il permet que les élèves/étudiants partagent leur connaissances tout en devant procéder à leur propre calculs. 
3. On peut réutiliser des exercices dans les évaluations, ce qui permet aux élèves/étudiants de montrer ce qu'ils ont compris.
4. On peut être plus souple sur les échéances, chaque élève ayant son "propre" énoncé peut avancer à rythme.
5. Le corrigé est automatiquement généré par le logiciel pour éviter de devoir recalculer chaque exercice ou devoir. 


II. Principes :

Le pricipe de base de DSXL_3, écrit en python, est de générer un code XeLatex compilable contenant des variantes d'exercices pour chaque élève/étudiant en deux modes :

a. Un mode énoncé (E)
b. Un mode corrigé (C) 

DSXL_3 est composé de trois programmes : 

1. dsxl_3_devoir_creation.py : Permet de créer des devoirs individualisés pour chaque élève.
2. dsxl_3_exercice_creation.py : Permet de créer des exercices.
3. dsxl_3_documentation_creation.py : Créer la documentation conteant la liste des exercices crées, ainsi qu'une documentation expliquant comment utiliser les deux programmes dsxl_3_devoir_creation.py et dsxl_3_exercice_creation.py

III Etat du projet : beta 

Les principales fonctionnalités du programme DSXL_3 sont implémentées et la documentation est en cours de rédaction. 
Le programme en l'état n'est pas facilement utilisable. 

Dans la domentation, j'explique les étapes nécessaires pour créer un exercice/un devoir sur un cas exemple concret et assez complexe, ce qui me permet d'améliorer en retour DSXL_3.

IV. Historique :

Avant DSXL_3, il y avait DSXL_2. 
Le programme DSXL_2 (écrit aussi sous python) utilisait les paquets  datatool et sagetex. 
Le problème de sagetex était à l'époque, que je ne voyait pas comment l'installer simplement sous Windows (j'utilise Linux) et cela rendait le partage très compliqué, voire impossible. 
Bref, j'en étais le seul utilisateur.  


