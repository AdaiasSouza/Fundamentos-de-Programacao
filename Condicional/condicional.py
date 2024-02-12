import random 

def maior_valor(lista_numeros):
	maior_valor = lista_numeros[0]

	for num in range(len(lista_numeros)):
		if num >= maior_valor:
			maior_valor = num

	return maior_valor

#random.seed(42)

for i in range(10):

	lista_numeros = []

	for i in range(10):
		lista_numeros.append(random.randrange(0, 100, 1))

	print("Lista: ",lista_numeros, ",Maior: ",maior_valor(lista_numeros), end="\n\n")
