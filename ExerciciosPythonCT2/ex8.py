numA = float(input("digite o primeiro numero: "))
op = (input("digite o Operador(+,-,*,/)"))
numB = float(input("digite o segundo numero: "))

if op == '+':
    resultado = numA + numB

if op == '-':
    resultado = numA - numB
    
if op == '*':
    resultado = numA * numB
    
if op == '/':
    resultado = numA / numB
    if numB != 0: 
            if numA % numB == 0:
                print(f"O número {numA} é divisível por {numB}.")


print(f"O resultado de{numA}, {op}, {numB} é {resultado}")
