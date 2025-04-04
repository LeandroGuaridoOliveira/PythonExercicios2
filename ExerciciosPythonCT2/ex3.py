##Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma
##partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a
##alavra EMPATE.

time1 = (input("Digite um time: "))
golsTime1 = int(input(f"Digite os gols do {time1} "))
time2 = (input("Digite outro Time: "))
golsTime2 = int(input(f"Digite os gols do, {time2}"))
if golsTime1 > golsTime2:
    print(time1, "venceu")
elif golsTime2 > golsTime1:
    print(time2, "venceu")
else:
    print("empate")

