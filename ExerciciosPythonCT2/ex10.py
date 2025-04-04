# Entrada do usuário
mediaPrimeiroSemestre = float(input("Digite a média do seu primeiro semestre: "))
mediaSegundoSemestre = float(input("Digite a média do seu segundo semestre: "))

aulasMinistradas = 100
aulasAssistidas = int(input("Quantas aulas você assistiu? "))

# Cálculo da média final (peso 4 para o primeiro semestre e 6 para o segundo)
mediaTotal = (mediaPrimeiroSemestre * 4 + mediaSegundoSemestre * 6) / 10

# Cálculo da frequência
frequencia = (aulasAssistidas / aulasMinistradas) * 100

# Verificação da média
if mediaTotal < 40:
    resultado = "Reprovado"
elif mediaTotal < 60:
    resultado = "Recuperação"
else:
    resultado = "Aprovado"

# Verificação da frequência
if frequencia <= 70:
    resultado = "Reprovado por falta"

# Exibição do resultado
print(f"Média final: {mediaTotal:.2f}")
print(f"Frequência: {frequencia:.2f}%")
print(f"Situação: {resultado}")
