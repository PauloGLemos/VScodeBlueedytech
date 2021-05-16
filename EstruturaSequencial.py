'''#1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Alo Mundo")

#2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
Numero = int (input('Digite um Numero: '))

print('O número informado foi', Numero)

#3 Faça um Programa que peça dois números e imprima a soma.
Numero1 = int (input('Digite o 1 Numero: '))
Numero2 = int (input('Digite o 2 Numero: '))
Soma = Numero1 + Numero2
print('A soma sera', Soma )

#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
Numero1 = float (input('Digite a 1 Nota: '))
Numero2 = float (input('Digite a 2 Nota: '))
Numero3 = float (input('Digite a 3 Nota: '))
Numero4 = float (input('Digite a 4 Nota: '))

Soma = (Numero1 + Numero2 + Numero3 + Numero4) / 4

print('A media sera', Soma )

#5 Faça um Programa que converta metros para centímetros.
Numero1 = int (input('Digite o valor em Metros: '))

Soma = Numero1*100

print('O valor em Centimetros sera', Soma )

#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
Numero1 = float (input('Digite o raio: '))
Soma = (Numero1 * Numero1) * 3.14

print('A area da circunferencia sera', Soma,'cm2')

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Numero1 = float (input('Digite o Lado: '))
Soma = (Numero1 * Numero1) 

print('A area do Quadrado sera', Soma )
print('O dobro da area do Quadrado sera', Soma * 2)

#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
Numero1 = float (input('Digite quanto voce ganha por hora: '))
Numero2 = float (input('Digite as horas trabalhadas no mês: '))

Soma = (Numero1 * Numero2) 
print('Seu Salario sera', Soma )

#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
F = float (input('Digite a temperatura em Fahrenheit: '))
Soma = 5 * ((F-32) / 9)

print('A temperatura em Celsius e', Soma )

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
C = float (input('Digite a temperatura em Celsius: '))
Soma = C * 9/5 + 32

print('A temperatura em Fahrenheit e', Soma )

#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float (input('Digite sua Altura: '))
Soma = (72.7*altura) - 58 +0.5
print ('Seu peso ideal e:', round(Soma))

#14 João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#14Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#14Imprima os dados do programa com as mensagens adequadas.

Peso = int (input('Digite quantos quilos voce pegou: '))
Soma = Peso - 50
print ('Voce pegou:', Peso,'KG')
if Peso >= 51:
    print('voce pagara uma taxa extra de:',Soma*4,'R$')
else:
    print('voce nao pagara taxa extra')'''

#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#16 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#16 Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Litros1 = 'Litros'
Metros = 'Metros'
latas1 = 'Latas'
Reais = 'R$'
latas = 80

metros = int (input('Digite quantos metros voce ira pintar: {0} '.format(Metros)))
Soma = metros/3
Soma2 = Soma/18
print('voce precisara de: {0} {1}'.format(Soma, Litros1))
if metros <= 54:
    print('voce precisara apenas de 1 Lata')
    print('voce pagara:','80 {0}'.format(Reais))
else:
    print('Ou seja de:',(round(Soma2+0.5)),'{0}'.format(latas1))
    print('Sendo um valor de:',(round(Soma2+0.5)*80),'{0}'.format(Reais))