#02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.

palavra1 = str(input("Digite uma palavra : "))
palavra1 = palavra1.upper()

C = 0
B = 0

for C in palavra1:
    if (C == 'A' or C == 'E' or C == 'I' or C == 'O' or C == 'U'): 
        B+=1
print("a palavra tem ", B ,"vogais")        
print("a palavra sem vogais fica: ",palavra1.replace(C,''))


"""
#nesse aqui eu fui atras de uma ajuda, o codigo original era esse aqui de baixo:
#fiquei na duvida pois o programa repetia a palavra o numero de vezes das vogais

palavra1 = str(input("Digite uma palavra : " ))
palavra1 = palavra1.upper()
for A in palavra1:
    if A == 'A' or A == 'E' or A == 'I' or A == 'O' or A == 'U':
        print("a palavra tem ",A,"vogais")
        print("a palavra sem vogais fica: ",palavra1.replace(C,''))
"""
