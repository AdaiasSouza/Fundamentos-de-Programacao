def eh_par(number):
	if number%2 == 0:
		return True
	else:
		return False

def main():
	valores = [2, 5, 7, 9, 10, 65]

	for index in valores:
		if eh_par(index):
			print(index, "Par")
		else:
			print(index, " -> Impar")

if __name__ == '__main__':
	main()