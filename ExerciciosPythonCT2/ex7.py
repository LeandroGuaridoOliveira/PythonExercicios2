"""
Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
tabela a seguir:

Categoria Idade
Infantil 5 a 7
Juvenil 8 a 10
Adolescente 11 a 15
Adulto 16 a 30
Senior acima de 30
"""
# Entrada do usuário
idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    categoria = "Infantil"
elif 8 <= idade <= 10:
    categoria = "Juvenil"
elif 11 <= idade <= 15:
    categoria = "Adolescente"
elif 16 <= idade <= 30:
    categoria = "Adulto"
else:
    categoria = "Senior"

# Exibição da categoria
print(f"A categoria do nadador é: {categoria}")
