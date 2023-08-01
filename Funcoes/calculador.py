def calculadora(number_one, number_two, operation):
	if operation == '+':
		return number_one + number_two
	elif operation == '-':
		return number_one - number_two
	elif operation == '*':
		return number_one * number_two
	else:
		return number_one / number_two




def main():

	executa = True
	while executa: 
		print("\tMenu: ")
		print("+ Adição", "\n", "- Subtracao", "\n", "* Multiplicacao","\n", "/ Divisao")
		number_one = int(input("Numero 1: "))
		number_two = int(input("Numero 2: "))
		operation = str(input("Operacao: "))
		print(number_one, operation,  number_two, " = ", calculadora(number_one, number_two, operation))
		
		print("Novo calculo ?  1 - Sim 0 Nao")
		opcao = int(input())
		if opcao:
			executa = True
		else:
			executa = False
			print("Finalizando...")


if __name__ == '__main__':
	main()