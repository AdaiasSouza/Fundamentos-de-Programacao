def maior_valor(list):
	for index in range(0,len(list),1):
		maior = list[0]

		if list[index] > maior:
			maior = list[index]

	return maior

def main():
	valores = [0, -1, 10, -100, 5]
	print(valores, ", Maior -> ", maior_valor(valores))
	

if __name__ == '__main__':
	main()


