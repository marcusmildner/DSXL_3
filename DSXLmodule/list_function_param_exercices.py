from class_exercice import * 
import numpy as np
from fractions import Fraction
import math
import sympy as sym
#list_of_fonction_param_exercices = []
#------------------------------------------------------fonction_param_exercice_001
def fonction_param_exercice_001() : 

    dico_exercice = {
        'nom_exercice': 'exercice_001' ,
        'date_creation': '10/01/2024' ,
        'source': 'marcus' ,
        'liste_notions' :  [ 'Pythagore' , 'triangle rectangle'  , 'triangle rectangle' , 'droites perpendiculaires' , 'aire triangle' , 'hauteur triangle' ] , 
        'liste_variables' :  [ 'a:3' , 'b:4' , 'h2:25' , 'h:5.000' , 'w:6' , 'BH:2.40' ]
        }

 
    liste_liste_parametres = [  [ 'a:3' , 'b:4' , 'h2:25' , 'h:5.000' , 'w:6' , 'BH:2.40' ] ] 

    # Votre code ici :
    for a in range(3,11) :
        for b in range(a+1,10) :
            h2 = a**2+b**2
            h = round(h2**(0.5), 4) 
            w = a*b/2
            BH = round(w*2/h2**(0.5),2)
            liste_liste_parametres.append(['a:'+str(a) , 'b:'+str(b) , 'h2:'+str(h2) , 'h:'+str(h) , 'w:'+str(w) , 'BH:'+str(BH) ])



    return dico_exercice, liste_liste_parametres 

dico_exercice, liste_liste_parametres = fonction_param_exercice_001()
Ex_001 = Exercice(dico_exercice, liste_liste_parametres)
#------------------------------------------------------fonction_param_exercice_002
def fonction_param_exercice_002() : 

    dico_exercice = {
        'nom_exercice': 'exercice_002' ,
        'date_creation': '21/02/2024' ,
        'source': 'annales apmep, Baccalauréat Métropole20 mars 2023, sujet 1, exercice 3' ,
        'liste_notions' :  [ 'fonction logarithme' , 'fonction exponentielle' , 'limite de suite' , 'programme de calcul' , 'récurrence' , 'script python' , 'suite bornée' , 'suite monotone' , 'terminale spe' ] , 
        'liste_variables' :  [ 'pourc:90' , 'nouvques:130' , 'Nquesun:300' , 'u1:3' , 'q:0.9' , 'm:1.3' , 'u2:4' , 'u3:4.9' , 'u2cent:400' , 'u3cent:490' , 'uinf:13' , 'Au:\dfrac{100}{9}' , 'useuil:8.5' , 'uDelta:4.5' , 'AuDenom:9' , 'AuNum:100' , 'tmp1:0.405' , 'seuilDec:8.6' , 'seuilAlg:9' , 'vinf:9' , 'Av:6' , 'Lv:-0.19' , 'v1:3' , 'v2:4.04' , 'tmp2:0.5' , 'pLv:0.19' , 'tmp3:-13.08' , 'nvapprox:14.08' , 'nv:15' , 'useuilcent:850' , 'choixmod:1ere' , 'uinfcent:1300' , 'vinfcent:900' , 'choixmod2:1ere' ]
        }

 
    liste_liste_parametres = [  [ 'pourc:90' , 'nouvques:130' , 'Nquesun:300' , 'u1:3' , 'q:0.9' , 'm:1.3' , 'u2:4' , 'u3:4.9' , 'u2cent:400' , 'u3cent:490' , 'uinf:13' , 'Au:\dfrac{100}{9}' , 'useuil:8.5' , 'uDelta:4.5' , 'AuDenom:9' , 'AuNum:100' , 'tmp1:0.405' , 'seuilDec:8.6' , 'seuilAlg:9' , 'vinf:9' , 'Av:6' , 'Lv:-0.19' , 'v1:3' , 'v2:4.04' , 'tmp2:0.5' , 'pLv:0.19' , 'tmp3:-13.08' , 'nvapprox:14.08' , 'nv:15' , 'useuilcent:850' , 'choixmod:1ere' , 'uinfcent:1300' , 'vinfcent:900' , 'choixmod2:1ere' ] ] 

    # Votre code ici :
    def seuil(p) :
        n=1
        u= u1
        while u<=p :
            n=n+1
            u= q*u+ m
        return n



    for pourc in range(80,91,5) :
        for nouvques in range(100,151,5) :
            for Nquesun in range(100,201,25) :
                uinf = Fraction(nouvques/(100-pourc))
                for vinf in range(int(uinf)-1,int(uinf)+1,2) :
                    str_pourc = str(pourc) 
                    str_nouvques = str(nouvques) 
                    str_Nquesun = str(Nquesun) 
                    u1 =  Fraction(Nquesun,100)
                    str_u1 = str(u1) 
                    q = Fraction(pourc,100)
                    str_q = str(float(q))
                    m = Fraction(nouvques,100)
                    str_m = str(float(m)) 
                    u2 = u1*q+m
                    str_u2 = str(float(u2) )
                    u3 = u2*q+m
                    str_u3 = str(float(u3) )
                    u2cent = 100*u2
                    str_u2cent = str(u2cent) 
                    u3cent = 100*u3
                    str_u3cent = str(u3cent) 
                    str_uinf = str(uinf) 
                    Au = -(u1 - uinf)*Fraction(100,pourc)
                    str_Au = str(Au) 
                    useuil = math.trunc(min(uinf,vinf))-0.5
                    str_useuil = str(useuil) 
                    uDelta = uinf - useuil
                    str_uDelta = str(uDelta) 
                    AuDenom =Au.denominator
                    str_AuDenom = str(AuDenom) 
                    AuNum =  Au.numerator
                    str_AuNum = str(AuNum) 
                    tmp1 = uDelta/Au 
                    str_tmp1 = str(tmp1) 
                    seuilDec = round(math.log(tmp1)/math.log(q),1)
                    str_seuilDec = str(seuilDec) 
                    seuilAlg = seuil(useuil) 
                    str_seuilAlg = str(seuilAlg) 
                    #vinf = 9 
                    str_vinf = str(vinf) 
                    Av = vinf-u1 
                    str_Av = str(Av) 
                    Lv = -0.19 
                    str_Lv = str(Lv) 
                    v1 = vinf-Av
                    str_v1 = str(v1) 
                    v2 = vinf-Av*math.exp(Lv)
                    str_v2 = str(round(v2,2)) 
                    tmp2 = vinf - useuil
                    str_tmp2 = str(tmp2) 
                    pLv = -Lv
                    str_pLv = str(pLv) 
                    tmp3 = round(math.log(tmp2/Av)/pLv,2)
                    str_tmp3 = str(tmp3) 
                    nvapprox = 1-tmp3
                    str_nvapprox = str(nvapprox) 
                    nv = math.trunc(nvapprox+1)
                    str_nv = str(nv) 
                    useuilcent = int(useuil*100)
                    str_useuilcent = str(useuilcent) 
                    if seuilAlg < nv :
                        choixmod = "1ere"
                    else : 
                        choixmod = "2eme"
                    str_choixmod = str(choixmod) 
                    uinfcent = uinf*100
                    str_uinfcent = str(uinfcent) 
                    vinfcent = vinf*100
                    str_vinfcent = str(vinfcent) 
                    choixmod2 = '1ere'
                    str_choixmod2 = str(choixmod2) 
    
                    liste_liste_parametres.append( [ 'pourc:'+str_pourc , 'nouvques:'+str_nouvques , 'Nquesun:'+str_Nquesun , 'u1:'+str_u1 , 'q:'+str_q , 'm:'+str_m , 'u2:'+str_u2 , 'u3:'+str_u3 , 'u2cent:'+str_u2cent , 'u3cent:'+str_u3cent , 'uinf:'+str_uinf , 'Au:'+str_Au , 'useuil:'+str_useuil , 'uDelta:'+str_uDelta , 'AuDenom:'+str_AuDenom , 'AuNum:'+str_AuNum , 'tmp1:'+str_tmp1 , 'seuilDec:'+str_seuilDec , 'seuilAlg:'+str_seuilAlg , 'vinf:'+str_vinf , 'Av:'+str_Av , 'Lv:'+str_Lv , 'v1:'+str_v1 , 'v2:'+str_v2 , 'tmp2:'+str_tmp2 , 'pLv:'+str_pLv , 'tmp3:'+str_tmp3 , 'nvapprox:'+str_nvapprox , 'nv:'+str_nv , 'useuilcent:'+str_useuilcent , 'choixmod:'+str_choixmod , 'uinfcent:'+str_uinfcent , 'vinfcent:'+str_vinfcent , 'choixmod2:'+str_choixmod2 ]) 
 


    return dico_exercice, liste_liste_parametres 
dico_exercice, liste_liste_parametres = fonction_param_exercice_002()
Ex_002 = Exercice(dico_exercice, liste_liste_parametres)
#------------------------------------------------------fonction_param_exercice_003
def fonction_param_exercice_003() : 

    dico_exercice = {
        'nom_exercice': 'exercice_003' ,
        'date_creation': '20/03/2024' ,
        'source': 'annales apmep, Brevet Amérique du Nord 31 mai 2023' ,
        'liste_notions' :  [ '3eme' , 'aire triangle' , 'calcul angle' , 'droites parallèles' , 'triangle rectangle' , 'réciproque de Pythagore' , 'Thalès' , 'fonctions trigonométriques' ] , 
        'liste_variables' :  [ 'AN:13' , 'LN:5' , 'AL:12' , 'ON:3' , 'ANcarre:169' , 'LNcarre:25' , 'ALcarre:12' , 'OH:7.25' , 'angleLNA:67' , 'aireLNA:30' , 'aireOHN:10.8' , 'aireLOHA:19.2' , 'propAire:0.64' , 'NUMpropAire:64' , 'DENpropAire:100' ]
        }

 
    liste_liste_parametres = [  [ 'AN:13' , 'LN:5' , 'AL:12' , 'ON:3' , 'ANcarre:169' , 'LNcarre:25' , 'ALcarre:144' , 'OH:7.25' , 'angleLNA:67' , 'aireLNA:30' , 'aireOHN:10.8' , 'aireLOHA:19.2' , 'propAire:0.64' , 'NUMpropAire:64' , 'DENpropAire:100' ] ] 

    # Votre code ici :
    for a in range(2,5) :
        for b in range (a+1, 10) :
            for k in range(2,5) : 
                 
                LN = b**2-a**2
                ON = Fraction(LN,k)
                strON = str(ON)
                strLN = str(LN)
                AL = 2*a*b
                strAL = str(AL)
                AN = a**2+b**2
                strAN = str(AN)    
                ANcarre = AN**2
                strANcarre = str(ANcarre)
                LNcarre = LN**2
                strLNcarre =str(LNcarre)
                ALcarre = AL**2
                strALcarre = str(ALcarre)
                OH = Fraction(AL*ON,LN)
                strOH = "\\frac{"+str(OH.numerator)+"}{"+str(OH.denominator)+"}"
                angleLNA = int(np.arccos(LN/AN)*180/np.pi)
                strangleLNA= str(angleLNA)
                aireLNA = Fraction(LN*AL,2)
                straireLNA = str(aireLNA)
                aireOHN = Fraction(ON,2)*OH
                straireOHN = str(aireOHN)
                aireLOHA = aireLNA - aireOHN
                floataireLOHA = float(aireLOHA)
                straireLOHA = str(round(floataireLOHA,2))
                propAire = aireLOHA/aireLNA
                strpropAire = str(propAire)
                NUMpropAire = propAire.numerator
                strNUMpropAire = str(NUMpropAire)
                DENpropAire = propAire.denominator
                strDENpropAire = str(DENpropAire)
                liste_liste_parametres.append([ 'AN:'+strAN , 'LN:'+strLN , 'AL:'+strAL , 'ON:'+strON , 'ANcarre:'+strANcarre ,\
                                               'LNcarre:'+strLNcarre , 'ALcarre:'+strALcarre , 'OH:'+strOH ,\
                                               'angleLNA:'+strangleLNA , 'aireLNA:'+straireLNA , 'aireOHN:'+straireOHN , \
                                               'aireLOHA:'+straireLOHA , 'propAire:'+strpropAire , \
                                               'NUMpropAire:'+strNUMpropAire , 'DENpropAire:'+strDENpropAire ])

    return dico_exercice, liste_liste_parametres 

dico_exercice, liste_liste_parametres = fonction_param_exercice_003()
Ex_003 = Exercice(dico_exercice, liste_liste_parametres)

#------------------------------------------------------fonction_param_exercice_004

def fonction_param_exercice_004() : 

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
                              r'ensSunant: \{1-\sqrt{11} \}' ,
                              r'y0p:-6' , 'yAp:10' , 'yBp:3' , 
                              r'y0m: ' , 'yAm: ' , 'yBm: ' ]
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
                              r'ensSunant: \{1-\sqrt{11} \}' ,
                              r'y0p:-6' , 'yAp:10' , 'yBp:3' , 
                              r'y0m: ' , 'yAm: ' , 'yBm: '  ]] 
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
            lst_x0 = [x for x in range(xA+1,xB)]
            lst_x0.remove(0) # On exclut x0=0
            for x0 in lst_x0: #  Contrainte c6
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
                                    if not(len(list_y_0_sol)<4 or len(list_y_1_sol)<4 or len(list_y_2_sol)<4) : 
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
                                        str_ftikz = str(a)+r'*(\x)^(2.0) +'+str(b)+r'*(\x)'+'+'+str(c) 

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
                                        f_semidev = a* (x**2-2*x0*x+x0**2)+y0  		       
                                        with sym.evaluate(False):                                           
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
                                        # Attribution des six nouvelles variables : 
                                        if a> 0 :
                                            str_yAp = str_yA
                                            str_y0p = str_y0
                                            str_yBp = str_yB
                                            str_yAm = ' '
                                            str_y0m = ' '
                                            str_yBm = ' '
                                        else : 
                                            str_yAm = str_yA
                                            str_y0m = str_y0
                                            str_yBm = str_yB
                                            str_yAp = ' '
                                            str_y0p = ' '
                                            str_yBp = ' '
                                            
                                            
                                        liste_liste_parametres.append( [ 'xA:'+str_xA , 'xB:'+str_xB , 'ftikz:'+str_ftikz , 'ymaxpAq2:'+str_ymaxpAq2 , 'yminpAq2:'+str_yminpAq2 , 'ypAq3a:'+str_ypAq3a , 'ypAq3b2ant:'+str_ypAq3b2ant , 'xpAq3bsol1:'+str_xpAq3bsol1 , 'xpAq3bsol2:'+str_xpAq3bsol2 , 'ypAq4a1ant:'+str_ypAq4a1ant , 'ques4aSol:'+str_ques4aSol , 'ypAq4a0ant:'+str_ypAq4a0ant , 'quespA4bSol:'+str_quespA4bSol , 'ypAq5:'+str_ypAq5 , 'ques5solS:'+str_ques5solS , 'x0:'+str_x0 , 'yA:'+str_yA , 'yB:'+str_yB , 'varGpAq6:'+str_varGpAq6 , 'varDpAq6:'+str_varDpAq6 , 'y0:'+str_y0 , 'fdev:'+str_fdev , 'f0pBq1:'+str_f0pBq1 , 'fm1pBq1:'+str_fm1pBq1, 'fm2pBq1:'+str_fm2pBq1 , 'fcan:'+str_fcan , 'formecanpBq2et1:'+str_formecanpBq2et1 , 'formecanpBq2et2:'+str_formecanpBq2et2 , 'ypBq3deuxant:'+str_ypBq3deuxant , 'ypBq3unant:'+str_ypBq3unant , 'quespBq3sol2ant:'+str_quespBq3sol2ant , 'x1deuxant:'+str_x1deuxant , 'x2deuxant:'+str_x2deuxant , 'ensSdeuxant:'+str_ensSdeuxant , 'quespBq3sol1ant:'+str_quespBq3sol1ant , 'x1unant:'+str_x1unant , 'x2unant:'+str_x2unant , 'ensSunant:'+str_ensSunant , 
        'yAp:'+str_yAp , 'y0p:'+str_y0p ,'yBp:'+str_yBp,    'yAm:'+str_yAm , 'y0m:'+str_y0m ,'yBm:'+str_yBm ]) 
 


    return dico_exercice, liste_liste_parametres 

dico_exercice, liste_liste_parametres = fonction_param_exercice_004()
Ex_004 = Exercice(dico_exercice, liste_liste_parametres)
