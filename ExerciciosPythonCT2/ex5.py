##6. Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.# Lê os números inteiros A e B
# Lê os números inteiros A e B
A = int(input("Digite o número A: "))
B = int(input("Digite o número B: "))

# Verifica se A é divisível por B
if B != 0: 
    if A % B == 0:
        print(f"O número {A} é divisível por {B}.")
    else:
        print(f"O número {A} não é divisível por {B}.")
else:
    print("Não é possível dividir por zero.")
