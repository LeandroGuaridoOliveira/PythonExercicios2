"""
Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a
seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
código condição de pagamento
1 A vista em dinheiro ou cheque, recebe 10% de desconto
2 A vista no cartão de crédito, recebe 5% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em quatro vezes, preço normal de etiqueta mais juros de 7%

"""
import math

precoProduto = float(input("Digite o preço do protudo: "))
print("Qual será a forma de pag?\n 1- Dinheiro ou cheque\n 2- A vista no Cartao de crédito\n 3- em 2x sem juros\n 4- em 4x com juros de 7% ")
formaPag = input()

if formaPag == "1":
    precoProduto = precoProduto * 0.90
elif formaPag == "2":
    precoProduto = precoProduto * 0.95
elif formaPag == "3":
    precoProduto = precoProduto / 2 
    print(f"O valor a ser pago da 2 parcela é de: R$ {precoProduto}")
elif formaPag == "4":
    precoProduto = precoProduto * 1.07
    
print(f"O valor a ser pago agora é de: R$ {precoProduto}")



