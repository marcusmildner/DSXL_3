def fonction_param_exercice() : 

    dico_exercice = {
        'nom_exercice': 'exercice_004' ,
        'date_creation': '12/03/2024' ,
        'source': 'Marcus' ,
        'liste_notions' :  [ 'récurrence' , 'terminale_spe' , '2nd' , 'développement' , 'fonction polynôme' , 'lecture graphique' , 'maximum' , 'tableau de variations' ] , 
        'liste_variables' :  [ 'xA:-3' , 'xB:4.' , 'ftikz:(\x)^(2.0)-2*(\x)-5' , 'ymaxpAq2:10' , 'yminpAq2:-6' , 'ypAq3a:-5' , 'ypAq3b2ant:2' , 'xpAq3bsol1:-1.8' , 'xpAq3bsol2:3.7' , 'ypAq4a1ant:1' , 'ques4aSol:\mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6' , 'ypAq4a0ant:0' , 'quespA4bSol:\mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5' , 'ypAq5:-3' , 'ques5solS: [-3\,;\,-0.7] \cup  [2.7\,;\,4]' , 'x0:1' , 'yA:10' , 'yB:3' , 'varGpAq6:\searrow' , 'varDpAq6:\nearrow' , 'y0:-6' , 'fdev: x^2-2 x -5' , 'f0pBq1: 0^2 - 2 \times 0 -5 = -5 ' , 'fm1pBq1:(-1)^2 - 2 \times (-1) -5 = -2' , 'fcan:(x-1)^2 -6' , 'formecanpBq2et1:x^2 - 2 x\times 1 + 1^2 - 6' , 'formecanpBq2et2:x^2 - 2 x -5 ' , 'ypBq3deuxant:0' , 'ypBq3unant:5' , 'quespBq3sol2ant:
\begin{array}{lll}
 f(x) &=& 0 \\
 (x-1)^2 -6  &=&0 \\
 (x-1)^2 -(\sqrt{6})^2  &=&0 \\
 (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\
\end{array}
' , 'x1deuxant:1+\sqrt{6}\in D' , 'x2deuxant:1-\sqrt{6}\in D' , 'ensSdeuxant:\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' , 'quespBq3sol1ant:
\begin{array}{lll}
 f(x) &=&5 \\
 (x-1)^2 -6  &=&5 \\
  (x-1)^2 -11  &=&0 \\
 (x-1)^2 -(\sqrt{11})^2  &=&0 \\
 (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0 
\end{array}
' , 'x1unant:1+\sqrt{11}\not\in D' , 'x2unant:1-\sqrt{11}\in D' , 'ensSunant: \{1-\sqrt{11} \}' ]
        }

 
    liste_liste_parametres = [  [ 'xA:-3' , 'xB:4.' , 'ftikz:(\x)^(2.0)-2*(\x)-5' , 'ymaxpAq2:10' , 'yminpAq2:-6' , 'ypAq3a:-5' , 'ypAq3b2ant:2' , 'xpAq3bsol1:-1.8' , 'xpAq3bsol2:3.7' , 'ypAq4a1ant:1' , 'ques4aSol:\mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6' , 'ypAq4a0ant:0' , 'quespA4bSol:\mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5' , 'ypAq5:-3' , 'ques5solS: [-3\,;\,-0.7] \cup  [2.7\,;\,4]' , 'x0:1' , 'yA:10' , 'yB:3' , 'varGpAq6:\searrow' , 'varDpAq6:\nearrow' , 'y0:-6' , 'fdev: x^2-2 x -5' , 'f0pBq1: 0^2 - 2 \times 0 -5 = -5 ' , 'fm1pBq1:(-1)^2 - 2 \times (-1) -5 = -2' , 'fcan:(x-1)^2 -6' , 'formecanpBq2et1:x^2 - 2 x\times 1 + 1^2 - 6' , 'formecanpBq2et2:x^2 - 2 x -5 ' , 'ypBq3deuxant:0' , 'ypBq3unant:5' , 'quespBq3sol2ant:
\begin{array}{lll}
 f(x) &=& 0 \\
 (x-1)^2 -6  &=&0 \\
 (x-1)^2 -(\sqrt{6})^2  &=&0 \\
 (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\
\end{array}
' , 'x1deuxant:1+\sqrt{6}\in D' , 'x2deuxant:1-\sqrt{6}\in D' , 'ensSdeuxant:\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' , 'quespBq3sol1ant:
\begin{array}{lll}
 f(x) &=&5 \\
 (x-1)^2 -6  &=&5 \\
  (x-1)^2 -11  &=&0 \\
 (x-1)^2 -(\sqrt{11})^2  &=&0 \\
 (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0 
\end{array}
' , 'x1unant:1+\sqrt{11}\not\in D' , 'x2unant:1-\sqrt{11}\in D' , 'ensSunant: \{1-\sqrt{11} \}' ] ] 

    # Votre code ici :





    xA = -3 
    str_xA = str(xA) 
    xB = 4. 
    str_xB = str(xB) 
    ftikz = (\x)^(2.0)-2*(\x)-5 
    str_ftikz = str(ftikz) 
    ymaxpAq2 = 10 
    str_ymaxpAq2 = str(ymaxpAq2) 
    yminpAq2 = -6 
    str_yminpAq2 = str(yminpAq2) 
    ypAq3a = -5 
    str_ypAq3a = str(ypAq3a) 
    ypAq3b2ant = 2 
    str_ypAq3b2ant = str(ypAq3b2ant) 
    xpAq3bsol1 = -1.8 
    str_xpAq3bsol1 = str(xpAq3bsol1) 
    xpAq3bsol2 = 3.7 
    str_xpAq3bsol2 = str(xpAq3bsol2) 
    ypAq4a1ant = 1 
    str_ypAq4a1ant = str(ypAq4a1ant) 
    ques4aSol = \mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6 
    str_ques4aSol = str(ques4aSol) 
    ypAq4a0ant = 0 
    str_ypAq4a0ant = str(ypAq4a0ant) 
    quespA4bSol = \mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5 
    str_quespA4bSol = str(quespA4bSol) 
    ypAq5 = -3 
    str_ypAq5 = str(ypAq5) 
    ques5solS =  [-3\,;\,-0.7] \cup  [2.7\,;\,4] 
    str_ques5solS = str(ques5solS) 
    x0 = 1 
    str_x0 = str(x0) 
    yA = 10 
    str_yA = str(yA) 
    yB = 3 
    str_yB = str(yB) 
    varGpAq6 = \searrow 
    str_varGpAq6 = str(varGpAq6) 
    varDpAq6 = \nearrow 
    str_varDpAq6 = str(varDpAq6) 
    y0 = -6 
    str_y0 = str(y0) 
    fdev =  x^2-2 x -5 
    str_fdev = str(fdev) 
    f0pBq1 =  0^2 - 2 \times 0 -5 = -5  
    str_f0pBq1 = str(f0pBq1) 
    fm1pBq1 = (-1)^2 - 2 \times (-1) -5 = -2 
    str_fm1pBq1 = str(fm1pBq1) 
    fcan = (x-1)^2 -6 
    str_fcan = str(fcan) 
    formecanpBq2et1 = x^2 - 2 x\times 1 + 1^2 - 6 
    str_formecanpBq2et1 = str(formecanpBq2et1) 
    formecanpBq2et2 = x^2 - 2 x -5  
    str_formecanpBq2et2 = str(formecanpBq2et2) 
    ypBq3deuxant = 0 
    str_ypBq3deuxant = str(ypBq3deuxant) 
    ypBq3unant = 5 
    str_ypBq3unant = str(ypBq3unant) 
    quespBq3sol2ant = 
\begin{array}{lll}
 f(x) &=& 0 \\
 (x-1)^2 -6  &=&0 \\
 (x-1)^2 -(\sqrt{6})^2  &=&0 \\
 (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\
\end{array}
 
    str_quespBq3sol2ant = str(quespBq3sol2ant) 
    x1deuxant = 1+\sqrt{6}\in D 
    str_x1deuxant = str(x1deuxant) 
    x2deuxant = 1-\sqrt{6}\in D 
    str_x2deuxant = str(x2deuxant) 
    ensSdeuxant = \{1+\sqrt{6} \,;\,1-\sqrt{6} \} 
    str_ensSdeuxant = str(ensSdeuxant) 
    quespBq3sol1ant = 
\begin{array}{lll}
 f(x) &=&5 \\
 (x-1)^2 -6  &=&5 \\
  (x-1)^2 -11  &=&0 \\
 (x-1)^2 -(\sqrt{11})^2  &=&0 \\
 (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0 
\end{array}
 
    str_quespBq3sol1ant = str(quespBq3sol1ant) 
    x1unant = 1+\sqrt{11}\not\in D 
    str_x1unant = str(x1unant) 
    x2unant = 1-\sqrt{11}\in D 
    str_x2unant = str(x2unant) 
    ensSunant =  \{1-\sqrt{11} \} 
    str_ensSunant = str(ensSunant) 
    
    liste_liste_parametres.append( [ 'xA:'+str_xA , 'xB:'+str_xB , 'ftikz:'+str_ftikz , 'ymaxpAq2:'+str_ymaxpAq2 , 'yminpAq2:'+str_yminpAq2 , 'ypAq3a:'+str_ypAq3a , 'ypAq3b2ant:'+str_ypAq3b2ant , 'xpAq3bsol1:'+str_xpAq3bsol1 , 'xpAq3bsol2:'+str_xpAq3bsol2 , 'ypAq4a1ant:'+str_ypAq4a1ant , 'ques4aSol:'+str_ques4aSol , 'ypAq4a0ant:'+str_ypAq4a0ant , 'quespA4bSol:'+str_quespA4bSol , 'ypAq5:'+str_ypAq5 , 'ques5solS:'+str_ques5solS , 'x0:'+str_x0 , 'yA:'+str_yA , 'yB:'+str_yB , 'varGpAq6:'+str_varGpAq6 , 'varDpAq6:'+str_varDpAq6 , 'y0:'+str_y0 , 'fdev:'+str_fdev , 'f0pBq1:'+str_f0pBq1 , 'fm1pBq1:'+str_fm1pBq1 , 'fcan:'+str_fcan , 'formecanpBq2et1:'+str_formecanpBq2et1 , 'formecanpBq2et2:'+str_formecanpBq2et2 , 'ypBq3deuxant:'+str_ypBq3deuxant , 'ypBq3unant:'+str_ypBq3unant , 'quespBq3sol2ant:'+str_quespBq3sol2ant , 'x1deuxant:'+str_x1deuxant , 'x2deuxant:'+str_x2deuxant , 'ensSdeuxant:'+str_ensSdeuxant , 'quespBq3sol1ant:'+str_quespBq3sol1ant , 'x1unant:'+str_x1unant , 'x2unant:'+str_x2unant , 'ensSunant:'+str_ensSunant ]) 
 


    return dico_exercice, liste_liste_parametres 


# Les lignes suivantes sont à supprimer après la phase de test : 
dico_exercice, liste_liste_parametres = fonction_param_exercice() 
list_defaut_param =dico_exercice['liste_variables'] 
for i in range(len(liste_liste_parametres[0])) :
    print('valeurs par defaut --> '+list_defaut_param[i]+' | '+liste_liste_parametres[1][i]+'  <---votre valeur : ' )


