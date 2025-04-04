#Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate.

numero1 = int(input("Digite um Numero: "))
numero2 = int(input("Digite outro Numero: "))
if numero1 > numero2:
    print(numero1, "é maior")
elif numero2 > numero1:
    print(numero2, "é maior")
else:
    print("empate")

