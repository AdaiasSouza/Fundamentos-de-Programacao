#============ Normalizacao de Dados ==========
import random as ra


# Geracao aleatoria de valores
list_valores = []

for i in range(0,10,1):
    list_valores.append(round(ra.randrange(500,1000),2)) # intervalo de teste [500,1000]

# Lista para populacao de valores normalizados
list_norma = []

# Definicao do dominio 
new_min, new_max = 0,1

dist_old = (max(list_valores) - min(list_valores))
dist_new = (new_max - new_min)


for i in range(0,len(list_valores),1):
    
    a = (((list_valores[i] - min(list_valores))/dist_old )*dist_new) + new_min    

    list_norma.append(round(a,2))

print("Lista Antiga: ",list_valores,"\n","Lista Normalizada: ",list_norma)
    
     
