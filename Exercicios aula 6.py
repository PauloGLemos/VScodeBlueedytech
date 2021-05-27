"""#1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma():
        var1 = int(input("Digite num1:" ))
        var2 = int(input("Digite num2:" ))
        var3 = int(input("Digite num3:" ))

        somas = (var1 + var2 + var3)   
        print(f"A soma dos valores é:", {somas})
soma()

#3. Faça um programa com uma função chamada somaImposto. 
#3. A função possui dois parâmetros formais: taxaImposto, 
#3. que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
#3. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto():
    custo = int(input("Digite o valor do custo:" ))
    Qimposto = int(input("Digite a taxa de imposto:" ))

    taxaImposto = custo + (Qimposto*custo /100)
somaImposto()"""

"""#4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O 
#4. salário é pago conforme a quantidade de horas trabalhadas. 
#4. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def empresaXYZ():
    horas = int(input("Digite horas trabalhadas: "))

    if horas >= 40:
        print("voce recebera um extra de 1.5 por horas trabalhadas",  (horas * 1.5) * 100)
    else:
        print("seu salario e igual a", horas * 100)

empresaXYZ()

#5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def IMC():
    peso = float(input("Digite seu peso: " ))
    altura = float(input("Digite sua altura: " ))

    somas = round(peso/(altura*altura),2)  
    print("seu IMC e:", somas)
    if somas < 18.5:
        print("IMC, MAGREZA")
    elif (somas >= 18.5) and (somas<= 24.9):
        print("IMC, NORMAL")
    elif (somas >= 25.0) and (somas <= 29.9):
        print("IMC, SOBREPESO, grau de obesidade 1")
    elif (somas >= 30.0) and (somas <= 39.9):
        print("IMC, OBESIDADE, grau de obesidade 2")
    else:
        print("IMC, OBESIDADE GRAVE, grau de obesidade 3")
IMC()

#6.	Escreva uma função que, dado um número nota representando a nota de um estudante, 
#6.	converte o valor de nota para um conceito (A, B, C, D, E e F).

def Notas():
    notas= float(input("Digite sua nota" )) 
    print("sua nota e:",notas)
    if notas >=9.0:
        print("A")
    elif notas >=8.0:
        print("B")
    elif notas >=7.0:
        print("C")
    elif notas >=6.0:
        print("D")
    elif (notas <=4.0) and (notas >=1.0):
        print("E")
    else:
        print("F")
Notas()

#7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
#7. Se eles forem iguais, imprima que eles são iguais.

def MenorNumero ():
    num1= float(input("Digite num1 " )) 
    num2= float(input("Digite num2 " )) 
    print("")
    if num1 > num2:
       print("o menor Numero e", num2)
    elif num2 > num1:
        print("o menor Numero e", num1)
    else:
        print("os Numeros sao iguais")
MenorNumero()"""

def Data():
    Dia= int(input("Digite o Dia " ))
    Mes= int(input("Digite o Mes " ))
    Ano= int(input("Digite o Ano " ))

    print("A data escolhida foi",Dia ,Mes ,Ano )
    if Mes == "01":
        print(Dia,"Janeiro",Ano)
    elif Mes == "02":
        print(Dia,"Fevereiro",Ano)
    elif Mes == "03":
        print(Dia,"Marco",Ano)
    elif Mes == "04":
        print(Dia,"Abril",Ano)
    elif Mes == "05":
        print(Dia,"Maio",Ano)
    elif Mes == "06":
        print(Dia,"Junho",Ano)
    elif Mes == "07":
        print(Dia,"Julho",Ano)
    elif Mes == "08":
        print(Dia,"Agosto",Ano)
    elif Mes == "09":
        print(Dia,"Setembro",Ano)
    elif Mes == "10":
        print(Dia,"Outubro",Ano)
    elif Mes == "11":
        print(Dia,"Novembro",Ano)
    elif Mes == "12":
        print(Dia,"Dezembro",Ano)
    else:
        print("Mes inexistente")

Data()