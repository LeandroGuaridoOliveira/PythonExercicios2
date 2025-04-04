# Recebe os dados de entrada
dias_uteis = int(input("Informe o total de dias úteis do mês: "))
horas_trabalhadas = int(input("Informe o total de horas trabalhadas no mês: "))
valor_hora = float(input("Informe quanto o trabalhador recebe por hora: "))

# Cálculo da jornada mensal normal (8 horas por dia útil)
jornada_mensal_normal = dias_uteis * 8

# Cálculo do total de horas extras (se houver)
if horas_trabalhadas > jornada_mensal_normal:
    horas_extras = horas_trabalhadas - jornada_mensal_normal
else:
    horas_extras = 0

# Cálculo do valor das horas extras (50% a mais do valor da hora normal)
valor_hora_extra = valor_hora * 1.5
total_extra = horas_extras * valor_hora_extra  # Aqui calculamos o valor das horas extras

# Cálculo do salário base (sem as horas extras)
salario_base = jornada_mensal_normal * valor_hora

# Cálculo do salário total (com horas extras)
salario_total = salario_base + total_extra

# Exibe o resultado
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Valor das horas extras: R$ {total_extra:.2f}")
print(f"Salário total com horas extras: R$ {salario_total:.2f}")
