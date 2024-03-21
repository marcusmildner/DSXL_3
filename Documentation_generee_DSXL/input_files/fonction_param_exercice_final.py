import math
import sympy as sym
def fonction_param_exercice() : 

    dico_exercice = {
        'nom_exercice': 'exercice_004' ,
        'date_creation': '12/03/2024' ,
        'source': 'Marcus' ,
        'liste_notions' :  [ '2nd' , 'développement' , 'fonction polynôme' , 'lecture graphique' , 'maximum' , 'tableau de variations' ] , 
        'liste_variables' :  [ r'xA:-3' , 
                              r'xB:4.' , 
                              r'ftikz:(\x)^(2.0)-2*(\x)-5' , 
                              r'ymaxpAq2:10' , 'yminpAq2:-6' , 
                              r'ypAq3a:-5' , 'ypAq3b2ant:2' , 'xpAq3bsol1:-1.8' , 'xpAq3bsol2:3.7' ,
                              r'ypAq4a1ant:1' , 
                              r'ques4aSol:\mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6' , 
                              r'ypAq4a0ant:0' , 
                              r'quespA4bSol:\mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5' , 
                              r'ypAq5:-3' , 
                              r'ques5solS: [-3\,;\,-0.7] \cup  [2.7\,;\,4]' , 
                              r'x0:1' , 'yA:10' , 'yB:3' , 
                              r'varGpAq6:\searrow' , r'varDpAq6:\nearrow' , 
                              r'y0:-6' , 
                              r'fdev: x^2-2 x -5' , 
                              r'f0pBq1: 0^2 - 2 \times 0 -5 = -5 ' , 
                              r'fm1pBq1:(-1)^2 - 2 \times (-1) -5 = -2' , 
                              r'fm2pBq1: (\sqrt{2})^2 - 2 \times \sqrt{2} -5 = 2 - 2 \times \sqrt{2} -5 =  -3 - 2  \sqrt{2}  ' ,
                              r'fcan:(x-1)^2 -6' , 
                              r'formecanpBq2et1:x^2 - 2 x\times 1 + 1^2 - 6' , 
                              r'formecanpBq2et2:x^2 - 2 x -5 ' , 
                              r'ypBq3deuxant:0' , 'ypBq3unant:5' , 
                              r'quespBq3sol2ant:\begin{array}{lll} f(x) &=& 0 \\ (x-1)^2 -6  &=&0 \\ (x-1)^2-(\sqrt{6})^2  &=&0 \\ (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\\end{array}' , 
                              r'x1deuxant:1+\sqrt{6}\in D' , 'x2deuxant:1-\sqrt{6}\in D' , 
                              r'ensSdeuxant:\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' , 
                              r'quespBq3sol1ant:\begin{array}{lll} f(x) &=&5 \\ (x-1)^2 -6  &=&5 \\  (x-1)^2 -11  &=&0 \\ (x-1)^2 -(\sqrt{11})^2  &=&0 \\ (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0\end{array}' ,
                              r'x1unant:1+\sqrt{11}\not\in D' , 'x2unant:1-\sqrt{11}\in D' , 
                              r'ensSunant: \{1-\sqrt{11} \}' ]
        }

 
    liste_liste_parametres = [  [ r'xA:-3' , 
                              r'xB:4.' , 
                              r'ftikz:(\x)^(2.0)-2*(\x)-5' , 
                              r'ymaxpAq2:10' , 'yminpAq2:-6' , 
                              r'ypAq3a:-5' , 'ypAq3b2ant:2' , 'xpAq3bsol1:-1.8' , 'xpAq3bsol2:3.7' ,
                              r'ypAq4a1ant:1' , 
                              r'ques4aSol:\mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6' , 
                              r'ypAq4a0ant:0' , 
                              r'quespA4bSol:\mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5' , 
                              r'ypAq5:-3' , 
                              r'ques5solS: [-3\,;\,-0.7] \cup  [2.7\,;\,4]' , 
                              r'x0:1' , 'yA:10' , 'yB:3' , 
                              r'varGpAq6:\searrow' , r'varDpAq6:\nearrow' , 
                              r'y0:-6' , 
                              r'fdev: x^2-2 x -5' , 
                              r'f0pBq1: 0^2 - 2 \times 0 -5 = -5 ' , 
                              r'fm1pBq1:(-1)^2 - 2 \times (-1) -5 = -2' , 
                              r'fm2pBq1: (\sqrt{2})^2 - 2 \times \sqrt{2} -5 = 2 - 2 \times \sqrt{2} -5 =  -3 - 2  \sqrt{2}  ' ,
                              r'fcan:(x-1)^2 -6' , 
                              r'formecanpBq2et1:x^2 - 2 x\times 1 + 1^2 - 6' , 
                              r'formecanpBq2et2:x^2 - 2 x -5 ' , 
                              r'ypBq3deuxant:0' , 'ypBq3unant:5' , 
                              r'quespBq3sol2ant:\begin{array}{lll} f(x) &=& 0 \\ (x-1)^2 -6  &=&0 \\ (x-1)^2-(\sqrt{6})^2  &=&0 \\ (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\\end{array}' , 
                              r'x1deuxant:1+\sqrt{6}\in D' , 'x2deuxant:1-\sqrt{6}\in D' , 
                              r'ensSdeuxant:\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' , 
                              r'quespBq3sol1ant:\begin{array}{lll} f(x) &=&5 \\ (x-1)^2 -6  &=&5 \\  (x-1)^2 -11  &=&0 \\ (x-1)^2 -(\sqrt{11})^2  &=&0 \\ (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0\end{array}' ,
                              r'x1unant:1+\sqrt{11}\not\in D' , 'x2unant:1-\sqrt{11}\in D' , 
                              r'ensSunant: \{1-\sqrt{11} \}' ]] 
    def antecedents(a,x0,y0,y) :
        lst_antecedent =[]
        # a x**2 - 2*a*x0*x + a*x0**2 +y0 - y = 0 est à résoudre
        b = -2*a*x0
        c = a*x0**2+y0 - y
        #print(a,b,c)
        Delta = b**2 - 4*a*c
        #print(Delta)
        if Delta >0 :
            x1 = round((-b-math.sqrt(Delta))/2/a,2) 
            x2 = round((-b+math.sqrt(Delta))/2/a,2) 
            lst_antecedent.append(x1)
            lst_antecedent.append(x2)
        if Delta ==0 : 
            x0 = math.round((-b)/2/a,2) 
            lst_antecedent.append(x0)
        return lst_antecedent

    def text_antecedent_genere(lst_antecedent) :
        if len(lst_antecedent) ==0 :  
            text_antecedent = r"\mbox{ n'a pas d'antécedent.}"
        else : 
            text_antecedent = r' \mbox{ pour } x \approx '+str(lst_antecedent[0])
            if len(lst_antecedent) == 1 :
                text_antecedent = text_antecedent +'\mbox{.}'
            else :
                text_antecedent = text_antecedent+ r' \mbox{ et } x \approx '+str(lst_antecedent[1]) +r'\mbox{.}'

        return text_antecedent
    x = sym.symbols('x')
    
    # =============================== python_contraintes.py ====================================
    # Contraintes c1 et c2 :
    xmin=-5
    xmax=6
    ymin=-8
    ymax=22
    margex = 2
    margey = 3
    # Variable pour compter le nombre d'énoncés différents : 
    counter = 0
    for xA in range(xmin+margex,-margex+1): #  Contrainte c3 A
        for xB in range(margex,xmax-margex+1): #  Contrainte c3 B 
            for x0 in range(xA+1,xB): #  Contrainte c6
                for a in [-1,1]: 
                    if xA+xB!=2*x0: #  Contrainte c5
                        for y0 in range(ymin+margey,ymax-margey+1): #  Contrainte c7
                            yA = a*(xA-x0)**2+y0
                            yB = a*(xB-x0)**2+y0
                            if (yB>ymin+margey) and (yB<ymax-margey) and (yA>ymin+margey) and (yA<ymax-margey) :  
                                # On définit les listes pour les images ayant 0, 1 et 2 antécédents : 
                                list_y_0_sol = []
                                list_y_1_sol = []
                                list_y_2_sol = []
                                for y in range(ymin+margey,ymax-margey+1) : 
                                    if y< min(yA,yB,y0) or y> max(yA,yB,y0) :
                                        list_y_0_sol.append(y)
                                    if y>min(yA,yB) and y<max(yA,yB) :
                                        list_y_1_sol.append(y)
                                    if (a==1) and (y>y0) and (y<min(yA,yB)) : 
                                        list_y_2_sol.append(y)
                                    if (a==-1) and (y<y0) and (y>max(yA,yB)) : 
                                        list_y_2_sol.append(y) 
                                    # La condition suivante permet juste de restreindre le nombre de possibilités en imposant un nombre minimal de solutions : 
                                    if not(len(list_y_0_sol)<1 or len(list_y_1_sol)<2 or len(list_y_2_sol)<3) : 
                                        #print('A(',xA,' , ',yA,' ) B( ',xB,' , ',yB,' ) , P ( ', x0,' , ',y0,' ) \
                                        #avec a = ', a, ' f(x) = ',a,' [x - ( ',x0,' )]^2 - ( ',y0,' )' )
                                        #print('list_y_0_sol =',list_y_0_sol)
                                        #print('list_y_1_sol =',list_y_1_sol)
                                        #print('list_y_2_sol =',list_y_2_sol)
                                        #counter = counter+1
 

                                        # Variables dans list_y_2_sol
                                        ypBq3deuxant =list_y_2_sol[0]  # VL
                                        ypAq5 = list_y_2_sol[1]  # VL
                                        ypAq3b2ant =list_y_2_sol[2]  # VL
                    
                                        # Variables dans list_y_1_sol
                                        ypBq3unant = list_y_1_sol[0]  # VL
                                        ypAq4a1ant = list_y_1_sol[1] # VL
                                        
                                        # Variables dans list_y_0_sol
                                        ypAq4a0ant = list_y_0_sol[0]  # VL
                                        

                                        str_xA = str(xA) # VL
                                        str_xB = str(xB) # VL
                                        str_x0 = str(x0)  # VL
                                        str_yA = str(yA)  # VL
                                        str_yB = str(yB)  # VL        
                                        str_y0 = str(y0)  # VL    
                                        #ftikz = r'(\x)^(2.0)-2*(\x)-5' 
                                        b = -2*a*x0
                                        c = a*x0**2+y0
                                        str_ftikz = str(a)+r'*(\x)^(2.0) '+str(b)+r'*(\x)'+str(c) 

                                        ymaxpAq2 = max(yA,y0,yB)
                                        str_ymaxpAq2 = str(ymaxpAq2) 
                                        yminpAq2 = min(yA,y0,yB)
                                        str_yminpAq2 = str(yminpAq2) 
                                        #VC
                                        ypAq3a = a*(0-x0)**2 + y0 
                                        str_ypAq3a = str(ypAq3a) 
                                        
                                        str_ypAq3b2ant = str(ypAq3b2ant)  # VL
                                        # VC 
                                        lst_antecedent = antecedents(a,x0,y0,ypAq3b2ant)
                                        if len(lst_antecedent) ==2 :
                                            xpAq3bsol1 = lst_antecedent[0]
                                            str_xpAq3bsol1 = str(xpAq3bsol1) 
                                            xpAq3bsol2 = lst_antecedent[1]
                                            str_xpAq3bsol2 = str(xpAq3bsol2)         
                                        
                                        str_ypAq4a1ant = str(ypAq4a1ant)  # VL
                                        #VC
                                        lst_antecedent = antecedents(a,x0,y0,ypAq4a1ant)
                                        text_antecedent = text_antecedent_genere(lst_antecedent)
                                        #ques4aSol = r'\mbox{pour }x\approx 3.6\mbox{ et }x\approx -1.6' 
                                        str_ques4aSol = text_antecedent
                                        
                                        str_ypAq4a0ant = str(ypAq4a0ant)  # VL
                                        #VC 
                                        #quespA4bSol = r'\mbox{pour}x\approx -1.5\mbox{ et }x\approx 3.5' 
                                        lst_antecedent = antecedents(a,x0,y0,ypAq4a0ant)
                                        text_antecedent = text_antecedent_genere(lst_antecedent)    
                                        str_quespA4bSol = text_antecedent
                                        
                                        str_ypAq5 =str(ypAq5)
                                        #ques5solS =  r'[-3\,;\,-0.7] \cup  [2.7\,;\,4]' 
                                        lst_antecedent = antecedents(a,x0,y0,ypAq5)
                                        if len(lst_antecedent) ==2 : 
                                            if a >0 :
                                                str_ques5solS =  '[ '+str(xA)+r'\,;\,'+str(lst_antecedent[0])+' ] \cup  [ '+str(lst_antecedent[1])+r'\,;\,'+str(xB)+' ]' 
                                            else :
                                                str_ques5solS =  '[ '+str(lst_antecedent[1])+r'\,;\,'+str(lst_antecedent[0])+' ]' 
                                        if a>0 :        
                                            str_varGpAq6 = r'\searrow'
                                            str_varDpAq6 = '\\nearrow' 
                                        else :
                                            str_varGpAq6 = '\\nearrow'
                                            str_varDpAq6 = r'\searrow'

                                        # Utilisation de sympy as sym :
                                        # https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html
                                        f_can = a*(x-x0)**2+y0
                                        f_dev = sym.expand(f_can)
                                        #fdev =  r'x^2-2 x -5'     
                                        str_fdev = sym.latex(f_dev)
                                        #f0pBq1 =  r'0^2 - 2 \times 0 -5 = -5'  
                                        str_f0pBq1 = sym.latex(f_dev.subs(x,0))
                                        # fm1pBq1 = r'(-1)^2 - 2 \times (-1) -5 = -2' 
                                        with sym.evaluate(False):
                                            str_fm1pBq1 = sym.latex(f_dev.subs(x,-1))
                                        with sym.evaluate(True):
                                            str_fm1pBq1 = str_fm1pBq1+' = '+sym.latex(f_dev.subs(x,-1))    
                                        #str_fm2pBq1= r'(\sqrt{2})^2 - 2 \times \sqrt{2} -5 = 2 - 2 \times \sqrt{2} -5 =  -3 - 2  \sqrt{2}' 
                                        with sym.evaluate(False):
                                            str_fm2pBq1 =  sym.latex(f_dev.subs(x,sym.sqrt(2)))
                                        with sym.evaluate(True):
                                            str_fm2pBq1 =str_fm2pBq1+' = '+  sym.latex(f_dev.subs(x,sym.sqrt(2)))
                                        # fcan = '(x-1)^2 -6' 
                                        str_fcan = sym.latex(f_can)
                                        #formecanpBq2et1 = r'x^2 - 2 x\times 1 + 1^2 - 6'     
                                        with sym.evaluate(False):
                                            f_semidev = a*(x**2-2*x0*x+x0**2)+y0
                                            str_formecanpBq2et1 = sym.latex(f_semidev)
                                        #formecanpBq2et2 = r'x^2 - 2 x -5'  
                                        str_formecanpBq2et2 = str_fdev
                                        # f(x) - ypBq3unant = a*(x-x0)^2 +y0 - ypBq3deuxant :                                        
                                        str_ypBq3deuxant = str(ypBq3deuxant)  # VL
                                        y1 = y0 - ypBq3deuxant
                                        f_factor = a*((x-x0-sym.sqrt(int(-y1/a)))*(x-x0+sym.sqrt(int(-y1/a))))
                                        str_quespBq3sol2ant =r'\begin{array}{lll}  f(x) &=& '+str_ypBq3deuxant+r' \\ '+sym.latex(f_can-ypBq3deuxant)+r' &=&0 \\ '+sym.latex(f_factor)+r' &=&0 \\ \end{array}' 
                                        #quespBq3sol2ant = r'\begin{array}{lll}  f(x) &=& 0 \\  (x-1)^2 -6  &=&0 \\  (x-1)^2 -(\sqrt{6})^2  &=&0 \\  (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\ \end{array}'
                                        lst_ant = sym.solve(f_can-ypBq3deuxant)
                                        #x1deuxant = r'1+\sqrt{6}\in D' 
                                        str_x1deuxant = sym.latex(lst_ant[0])+r'\in D'
                                        #x2deuxant = r'1-\sqrt{6}\in D' 
                                        str_x2deuxant =  sym.latex(lst_ant[1])+r'\in D'
                                        #ensSdeuxant = r'\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' 
                                        str_ensSdeuxant = r'\{ '+sym.latex(lst_ant[0])+r'\,;\,'+sym.latex(lst_ant[1])+r' \}'


                                        
                                        str_ypBq3unant = str(ypBq3unant)  # VL
                                        # f(x) - ypBq3unant = a*(x-x0)^2 +y0 - ypBq3unant
                                        f_factunant = f_can - ypBq3unant
                                        y1 = y0 - ypBq3unant
                                        f_factor = a*((x-x0-sym.sqrt(int(-y1/a)))*(x-x0+sym.sqrt(int(-y1/a))))
                                        #quespBq3sol1ant = r'\begin{array}{lll} f(x) &=&5 \\  (x-1)^2 -6  &=&5 \\   (x-1)^2 -11  &=&0 \\  (x-1)^2 -(\sqrt{11})^2  &=&0 \\  (x-1-\sqrt{11})  (x-1+\sqrt{11}) &=&0 \end{array}'
                                        str_quespBq3sol1ant =r'\begin{array}{lll}  f(x) &=& '+str_ypBq3unant+r' \\ '+sym.latex(f_can-ypBq3unant)+r' &=&0 \\ '+sym.latex(f_factor)+r' &=&0 \\ \end{array}' 
                                        #quespBq3sol2ant = r'\begin{array}{lll}  f(x) &=& 0 \\  (x-1)^2 -6  &=&0 \\  (x-1)^2 -(\sqrt{6})^2  &=&0 \\  (x-1-\sqrt{6})  (x-1+\sqrt{6}) &=&0 \\ \end{array}'
                                        lst_ant = sym.solve(f_can-ypBq3unant)
                                        #x1deuxant = r'1+\sqrt{6}\in D' 
                                        str_x1unant = sym.latex(lst_ant[0])+r'\in D'
                                        #x2deuxant = r'1-\sqrt{6}\in D' 
                                        str_x2unant =  sym.latex(lst_ant[1])+r'\in D'
                                        #ensSdeuxant = r'\{1+\sqrt{6} \,;\,1-\sqrt{6} \}' 
                                        str_ensSunant = r'\{ '+sym.latex(lst_ant[0])+r'\,;\,'+sym.latex(lst_ant[1])+r' \}'

                                        #x1unant = r'1+\sqrt{11}\not\in D' 
                                        strxSol = ''
                                        if (xA<= lst_ant[0]) and (lst_ant[0]<xB) : 
                                            str_x1unant = sym.latex(lst_ant[0])+r'\in D'
                                            strxSol =  sym.latex(lst_ant[0])
                                        else :
                                            str_x1unant = sym.latex(lst_ant[0])+r'\not\in D'
                                        #x2unant = r'1-\sqrt{11}\in D' 
                                        if (xA<= lst_ant[1]) and (lst_ant[1]<xB) : 
                                            str_x2unant = sym.latex(lst_ant[1])+r'\in D'
                                            strxSol =  sym.latex(lst_ant[1])
                                        else :
                                            str_x2unant = sym.latex(lst_ant[1])+r'\not\in D'

                                        str_ensSunant = r'\{'+strxSol+'\}' 

                                        liste_liste_parametres.append( [ 'xA:'+str_xA , 'xB:'+str_xB , 'ftikz:'+str_ftikz , 'ymaxpAq2:'+str_ymaxpAq2 , 'yminpAq2:'+str_yminpAq2 , 'ypAq3a:'+str_ypAq3a , 'ypAq3b2ant:'+str_ypAq3b2ant , 'xpAq3bsol1:'+str_xpAq3bsol1 , 'xpAq3bsol2:'+str_xpAq3bsol2 , 'ypAq4a1ant:'+str_ypAq4a1ant , 'ques4aSol:'+str_ques4aSol , 'ypAq4a0ant:'+str_ypAq4a0ant , 'quespA4bSol:'+str_quespA4bSol , 'ypAq5:'+str_ypAq5 , 'ques5solS:'+str_ques5solS , 'x0:'+str_x0 , 'yA:'+str_yA , 'yB:'+str_yB , 'varGpAq6:'+str_varGpAq6 , 'varDpAq6:'+str_varDpAq6 , 'y0:'+str_y0 , 'fdev:'+str_fdev , 'f0pBq1:'+str_f0pBq1 , 'fm1pBq1:'+str_fm1pBq1, 'fm2pBq1:'+str_fm2pBq1 , 'fcan:'+str_fcan , 'formecanpBq2et1:'+str_formecanpBq2et1 , 'formecanpBq2et2:'+str_formecanpBq2et2 , 'ypBq3deuxant:'+str_ypBq3deuxant , 'ypBq3unant:'+str_ypBq3unant , 'quespBq3sol2ant:'+str_quespBq3sol2ant , 'x1deuxant:'+str_x1deuxant , 'x2deuxant:'+str_x2deuxant , 'ensSdeuxant:'+str_ensSdeuxant , 'quespBq3sol1ant:'+str_quespBq3sol1ant , 'x1unant:'+str_x1unant , 'x2unant:'+str_x2unant , 'ensSunant:'+str_ensSunant ]) 
 


    return dico_exercice, liste_liste_parametres 

dico_exercice, liste_liste_parametres  =fonction_param_exercice() 

print(len(liste_liste_parametres))
## Les lignes suivantes sont à supprimer après la phase de test : 
#dico_exercice, liste_liste_parametres = fonction_param_exercice() 
#list_defaut_param =dico_exercice['liste_variables'] 
#for i in range(len(liste_liste_parametres[0])) :
#    print('valeurs par defaut --> '+list_defaut_param[i] )
#    print('      votre valeur --> '+liste_liste_parametres[1][i] )
#    print('')
#dico_exercice, liste_liste_parametres  = fonction_param_exercice()
#print(len(liste_liste_parametres))
