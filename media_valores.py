def media_notas(n1, n2, n3):
    return (n1+n2+n3)/3

def media_final(media_notas, prova_final):
    nota_final = (media_notas + prova_final)/2
    return nota_final  

def status_aluno(media):
    if media >= 5:
        return "Aprovado"
    # elif media >= 4 and media < 7:
    #     return "Prova final"
    else:
        return "Reprovado"

def main():

    qtd_alunos = int(input("Quantidade de alunos: "))
    contador = 0    

    while contador < qtd_alunos:

        print("Aluno: ", contador + 1)
        nota_um = float(input("Inforne nota 1: "))
        nota_dois = float(input("Inforne nota 2: "))
        nota_tres = float(input("Inforne nota 3: "))

        media_calculada = media_notas(nota_um, nota_dois, nota_tres)


        if media_calculada >= 7:            
            print("Media: ", media_calculada, status_aluno(media_calculada)) 
            alunos_aprovados.append(media_calculada)

        elif media_calculada >= 4 and media_calculada < 7:
            nota_final = float(input("nota final: "))            
            media_fina = media_final(media_calculada, nota_final)
            print("Media: ", media_fina, status_aluno(media_fina))


        else:
            print("Media: ", media_calculada, "Situacao: ",status_aluno(media_calculada))             

        contador += 1
        print("\n")


if __name__ == '__main__':
    main()




    
