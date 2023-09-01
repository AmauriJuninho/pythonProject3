#while True:
 #   nome = input("Digite o nome do aluno: ")
 #  idade = int(input("Digite a idade do aluno: "))

    #notas = []
    #for i in range(4):
        #nota = float(input(f"Digite a nota {i + 1} do aluno: "))
        #notas.append(nota)

    #media = sum(notas) / len(notas)

    #print(f"Média do aluno {nome}: {media:.2f}")

    #if media > 8:
        #print("Você foi aprovado!")
        #break
    #else:
        # print("Você não atingiu a média mínima. Por favor, tente novamente.\n")

#=====================================================================================================================

#se a media for maior do que 8 sai do sistema0

#nome = input("digite o seu nome: ")
#idade = int(input("digite a sua idade"))


#while True:
     #nota1 = float(input("Digite a sua nota 1: "))
     #nota2 = float(input("Digite a sua nota 2: "))
     #nota3 = float(input("Digite a sua nota 3: "))
     #nota4 = float(input("Digite a sua nota 4: "))
     #media = (nota1+nota2+nota3+nota4)/4
     #print(media)
     #if media >= 8:
         #break

#print("sai do sistema")

#=====================================================================================================================

nome = input("digite o seu nome: ")
idade = input("digite sua idade: ")

while not (nome.isalpha() and idade.isdigit()):
    print("voce digitou o nome ou a idade errado")
    nome = input("digite o seu nome:" )
    idade = input("digite a sua idade")




# vou criar um loop que vai ficar verificando até digitar as notas corretamente
while True:

    #Bandeira
    b1 = False
    b2 = False
    b3 = False
    b4 = False


    #nota1
    nota1 = input("digite a sua nota 1: ") #pegando a primeira nota
    # 1) testar se a nota 1 tem um caracter do tipo "." ou "," se tiver vamos remover
    # 2) vamos verificar se o que restou é um digito
    if str.isdigit(nota1.replace(".", "")) or str.isdigit(nota1.replace(",", "")):
         # vou pegar o valor que é uma string e converter para um float
         # se ela tiver "," eu retiro a virgula e coloco um ponto "." no lugar
         nota1 = float(nota1.replace(",", "."))
         print("depois ", nota1)
         b1 = True
    else:
         b1 = False



    #nota2
    nota2 = input("digite a sua nota 2: ")
    if str.isdigit(nota2.replace(".", "")) or str.isdigit(nota2.replace(",", "")):
        nota2 = float(nota2.replace(",", "."))
        print("depois ", nota2)
        b2 = True
    else:
        b2 = False





    # nota3
    nota3 = input("digite a sua nota 3: ")
    if str.isdigit(nota3.replace(".", "")) or str.isdigit(nota3.replace(",", "")):
        nota3 = float(nota3.replace(",", "."))
        print("depois ", nota3)
        b3 = True
    else:
        b3 = False






    # nota4
    nota4 = input("digite a sua nota 4: ")
    if str.isdigit(nota4.replace(".", "")) or str.isdigit(nota4.replace(",", "")):
        nota3 = float(nota4.replace(",", "."))
        print("depois ", nota4)
        b4 = True
    else:
        b4  = False










