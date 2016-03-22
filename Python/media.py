nota1 = input("Digite sua primeira nota: ")
nota2 = input("Digite sua segunda nota: ")

if((float(nota1)+float(nota2))/2 >= 7):
    print("Sua media: ", (float(nota1)+float(nota2))/2)
    print("Você esta aprovado!")
else:
    print("Sua media: ", (float(nota1)+float(nota2))/2)
    print("Você está reprovado!")
