nome = str(input("Digite o nome do funcionário: "))
salarioB = float(input("Digite o salário base: "))
aumento = 0
salarioBNovo = 0

if salarioB <= 280:
    aumento = salarioB*0.20
    salarioBNovo = salarioB + aumento
elif (salarioB <= 700):
    aumento = salarioB*0.15
    salarioBNovo = salarioB + aumento
elif (salarioB <= 1500):
    aumento = salarioB*0.1
    salarioBNovo = salarioB + aumento
else:
    aumento = salarioB*0.05
    salarioBNovo = salarioB + aumento

print("Nome do funcionário: " + str(nome))
print("Salário antes do aumento: R$" + str(salarioB))
print("Valor do aumento: R$" + str(aumento))
print("Porcentual do aumento: " + str(int(salarioB/aumento)) + "%")
print("Salário bruto novo: R$" + str(salarioBNovo))
