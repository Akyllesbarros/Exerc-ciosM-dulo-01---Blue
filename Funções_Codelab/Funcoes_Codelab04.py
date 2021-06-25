# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def salario(valor, h) :
    valor= h * valor
    if h > 40 : 
        valor = 1.5 * valor
    return valor

print(salario(500, 50))