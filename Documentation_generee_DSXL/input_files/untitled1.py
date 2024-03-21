import math
def antecedents(a,x0,y0,y, mode = 'dec') :
    lst_antecedent =[]
    # a x**2 - 2*a*x0*x + a*x0**2 +y0 - y = 0 est à résoudre
    b = -2*a*x0
    c = a*x0**2+y0 - y
    print(a,b,c)
    Delta = b**2 - 4*a*c
    print(Delta)
    if Delta >0 :
        if mode =='dec' :
            x1 = round((-b+math.sqrt(Delta))/2/a,2) 
            x2 = round((-b-math.sqrt(Delta))/2/a,2) 
            lst_antecedent.append(x1)
            lst_antecedent.append(x2)
    if Delta ==0 :
        if mode =='dec' :
            x0 = math.round((-b)/2/a,2) 
            lst_antecedent.append(x0)
    return lst_antecedent

print(antecedents(1,1,-6,2, mode = 'dec'))
