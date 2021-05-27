'''lista = [10, 20, 30, 70, 60, 50, 40, 80]

print("a liste é:",lista)

print("------------------------------------------------------------------------------------------")

resultado = len(lista)
print("o tamanha da lista é:",resultado)

print("------------------------------------------------------------------------------------------")

resultado = max (lista)
print("o maior numero é:",resultado)

print("------------------------------------------------------------------------------------------")

resultado = min (lista)
print("o menor numero é:",resultado)

print("------------------------------------------------------------------------------------------")

resultado = sum (lista)
print("a soma dos numeros é:",resultado)

print("------------------------------------------------------------------------------------------")

lista.append(90)
print("90 foi adicionado a lista:",lista)

print("------------------------------------------------------------------------------------------")

lista.extend([91,92,93])
print("a lista [91,92,93] foi adicionada:",lista)

print("------------------------------------------------------------------------------------------")

lista.sort()
print("a lista foi organizada:",lista)

print("------------------------------------------------------------------------------------------")

for i in range(1,51):
    i = i*0.18
    print (round(i,3))

print("------------------------------------------------------------------------------------------")

var1 = float(input("quantos paes voce vai comprar " ))
print(var1*0.18)

print("------------------------------------------------------------------------------------------")'''

'''senha = 'teste'
entrada = input('Digite a Senha: ')
while entrada != senha:
    print('a senha esta errada')
    entrada = input('Digite a Senha novamente: ')
print('A senha digitada esta correta ')
    else:
    entrada == senha
    print('A senha digitada esta correta ')'''



nome = input('Digite o seu nome: ')
partidas = int(input('Digite a quantidade de partidas: '))

lista1 = []

for jogo in range(partidas):
    lista1.append(int(input(f'quantos gols foram feitos na partida {jogo+1}? :')))
    totalgosl = sum(lista1)

dicionario = {"Nome":nome,"Partidas":partidas,"Gols":lista1}
print(f'o jogador{dicionario["Nome"]} jogou {dicionario["Partidas"]} e fez um total de{dicionario["lista1"]}')
