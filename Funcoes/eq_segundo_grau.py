#=========== Eq Segundo Grau ============
#=========== Solucao Real ===============

import math as mt

def delta_eq(a,b,c):
    try:
        delta = mt.sqrt(mt.pow(b,2) - (4*a*c))
        return delta
    
    # delta negativo    
    except ValueError:
        delta_negat = (mt.pow(b,2) - (4*a*c))
        return delta_negat



print("\tEq Segundo Grau\n")

# Coeficientes de teste
#a,b,c = 3,-7,4
#a,b,c = 9,-12,4
#a,b,c = 5,3,5
a,b,c = 2,1,-3

if delta_eq(a,b,c) >= 0:
    x_0 = (-b + delta_eq(a,b,c))/(2*a)
    x_1 = (-b - delta_eq(a,b,c))/(2*a)

    print("x_0 = %.2f"%x_0,"x_1 = %.2f"%x_1)

else: print("Raiz nao real:  ",delta_eq(a,b,c))




