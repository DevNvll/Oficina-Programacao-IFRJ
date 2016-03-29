num = int(input("Digite um numero inteiro: "))

switch = {
    0: "Zero",
    1: "Um",
    2: "Dois",
    3: "Tres",
    4: "Quatro",
    5: "Cinco",
    6: "Seis",
    7: "Sete",
    8: "Oito",
    9: "Nove",
}

print(switch.get(num, "Não conheço"))
