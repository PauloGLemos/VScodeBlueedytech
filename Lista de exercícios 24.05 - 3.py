#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, 
# onde o computador vai “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, 
# no final mostre quantos palpites foram necessários para vencer.

senha = "12345"
Senha1 = (input("Digite a senha : "))
while Senha1 != senha:
    print ("A senha digitada esta errada")
    Senha1 = (input("Digite a senha novamente : "))
if Senha1 == senha:
    print("A senha esta correta")
    print("-------[Bem vindo, ao jogo de adivinhacao]-------")
    print()

import random

B = (input("Tente adivinhar o numero: "))
A = (random.randrange(1,20))
print(A)
while B != A:
    print("O numero esta errado, tente novamente")
    B = (input("Tente adivinhar o numero: "))
    if B == A:
        print(f"Voce acertou o numero: {A}")



