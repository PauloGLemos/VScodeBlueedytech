#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

"""# A soma deles;
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
soma = num1   num2
print("A soma sera: ",soma)

# A multiplicação entre eles;
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
multiplicação = num1 * num2
print("A multiplicação sera: ",multiplicação)

# A divisão inteira deles;
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
divisão = num1 // num2
print("A divisão inteira sera: ",divisão)

# Mostre na tela qual é o maior;
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
print("Os numeros sao: ",num1 ,num2)
if num1 > num2:
    print(f"o Numero 1 ({num1}) e maior que Numero 2 ({num2})")
else:
    print(f"o Numero 2 ({num2}) e maior que Numero 1 ({num1})")

# Verifique se o resultado da soma é par ou impar e mostre na tela;
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
soma = num1 + num2
print("a soma e: ",soma)
if (soma%2) == 0:
    print(f"o numero ({soma}) e Par")
else:
    print(f"o numero ({soma}) e Ímpar")

#nesse caso eu me esqueci que (soma%2) == 0: seria o ideal para se usar, 
# pois se um numero dividido por 2 for igual a 0 ele e par senao e impar

# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
num1 = float(input("Digite o 1 numero: " ))
num2 = float(input("Digite o 2 numero: " ))
multiplicação = num1 * num2
divisão = num1 // num2
resultado = multiplicação/divisão
if multiplicação > 40: 
    print("o resultado e: ", resultado)
else:
    print(f"O resultado ({resultado}) e menor que 40")"""
