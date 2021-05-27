#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Valide a data e retorne NULL caso a data seja inválida.

def Data():
    Dia= int(input("Digite o Dia " ))
    Mes= int(input("Digite o Mes " ))
    Ano= int(input("Digite o Ano " ))

    print("A data escolhida foi: " f"{Dia}/{Mes}/{Ano}")

    Mes1 =  ["null","Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

    if  Mes == 1:
        print("A data escolhida foi: ",Dia,Mes1[1],Ano)
    elif Mes == 2:
        print("A data escolhida foi: ",Dia,Mes1[2],Ano)
    elif Mes == 3:
        print("A data escolhida foi: ",Dia,Mes1[3],Ano)
    elif Mes == 4:
        print("A data escolhida foi: ",Dia,Mes1[4],Ano)
    elif Mes == 5:
        print("A data escolhida foi: ",Dia,Mes1[5],Ano)
    elif Mes == 6:
        print("A data escolhida foi: ",Dia,Mes1[6],Ano)
    elif Mes == 7:
        print("A data escolhida foi: ",Dia,Mes1[7],Ano)
    elif Mes == 8:
        print("A data escolhida foi: ",Dia,Mes1[8],Ano)
    elif Mes == 9:
        print("A data escolhida foi: ",Dia,Mes1[9],Ano)
    elif Mes == 10:
        print("A data escolhida foi: ",Dia,Mes1[10],Ano)
    elif Mes == 11:
        print("A data escolhida foi: ",Dia,Mes1[11],Ano)
    elif Mes == 12:
        print("A data escolhida foi: ",Dia,Mes1[12],Ano)
    else:
        print("Mes inexistente")

Data()


