# DESAFIO 02

salario = float(input('Olá colaborador, por favor, digite seu salário:\n'))

if salario < 280.00 : 
    salarioReajustado = salario + salario* 0.20 
    print(f''' 
    Seu salário antes do Reajuste: R$ {salario:.2f}
    Percentual de aumento: 20%
    Valor do aumento: R$ {salarioReajustado-salario}
    Seu salário Reajustado é: R$ {salarioReajustado:.2f}
    ''')

elif salario > 280.00 and salario < 700.00 : 
    salarioReajustado = salario + salario* 0.15
    print(f''' 
    Seu salário antes do Reajuste: R$ {salario:.2f}
    Percentual de aumento: 15%
    Valor do aumento: R$ {salarioReajustado-salario}
    Seu salário Reajustado é: R$ {salarioReajustado:.2f}
    ''')

elif salario > 700.00 and salario < 1500.00 : 
    salarioReajustado = salario + salario* 0.10 
    print(f''' 
    Seu salário antes do Reajuste: R$ {salario:.2f}
    Percentual de aumento: 10%
    Valor do aumento: R$ {salarioReajustado-salario}
    Seu salário Reajustado é: R$ {salarioReajustado:.2f}
    ''')

else : 
    salarioReajustado = salario + salario* 0.05

    print(f''' 
    Seu salário antes do Reajuste: R$ {salario:.2f}
    Percentual de aumento: 5%
    Valor do aumento: R$ {salarioReajustado-salario}
    Seu salário Reajustado é: R$ {salarioReajustado:.2f}
    ''')
