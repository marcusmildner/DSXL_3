from class_exercice import * 
import numpy as np
from fractions import Fraction
import math
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



