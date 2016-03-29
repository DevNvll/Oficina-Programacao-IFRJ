nome = str(input("Digite o nome do funcionário: "))
salarioB = float(input("Digite o salario base: "))
aumento = 0
salarioBNovo = 0

if (salarioB <= 280):
    aumento = salarioB*0.20
    salarioBNovo = salarioB + aumento
if (salarioB > 280 and salarioB <= 700):
    aumento = salarioB*0.15
    salarioBNovo = salarioB + aumento
if (salarioB > 700 and salarioB <= 1500):
    aumento = salarioB*0.1
    salarioBNovo = salarioB + aumento
if (salarioB > 1500):
    aumento = salarioB*0.05
    salarioBNovo = salarioB + aumento

print("Nome do funcionario: " + str(nome))
print("Salario antes do aumento: R$" + str(salarioB))
print("Valor do aumento: R$" + str(aumento))
print("Salario bruto novo: R$" + str(salarioBNovo))
