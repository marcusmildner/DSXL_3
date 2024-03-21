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
                                if not(len(list_y_0_sol)<5 or len(list_y_1_sol)<5 or len(list_y_2_sol)<5) : 
                                    print('A(',xA,' , ',yA,' ) B( ',xB,' , ',yB,' ) , P ( ', x0,' , ',y0,' ) \
                                    avec a = ', a, ' f(x) = ',a,' [x - ( ',x0,' )]^2 - ( ',y0,' )' )
                                    print('list_y_0_sol =',list_y_0_sol)
                                    print('list_y_1_sol =',list_y_1_sol)
                                    print('list_y_2_sol =',list_y_2_sol)
                                    counter = counter+1
                                    
print('counter = ',counter)