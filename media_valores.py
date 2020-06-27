#======= Media ===============#
import random as ra

def media(x): return (sum(x)/len(x))


pontuacao = []
# Popular lista com valors interos aleatorios
for value in range(0,100,1):
    pontuacao.append(ra.randrange(1,10))


pont_dow = []
pont_up = []

media_vlr = media(pontuacao)

# Classificacao de valores
for row in range(0,len(pontuacao),1):
    if pontuacao[row] < media_vlr: pont_dow.append(pontuacao[row])
    
    else: pont_up.append(pontuacao[row])        


print("Valores: ",pontuacao,"\n\nMedia: ",media(pontuacao),
      "\n\nAbaixo media: ",pont_dow,"\n\nAcima media: ",pont_up)





    
