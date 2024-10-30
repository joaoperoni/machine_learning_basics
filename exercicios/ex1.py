
def soma (a, b):
    return a+b 

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b

def calcular_litros():
    rendimento = 12 #km/litro
    tempo = int(input("Insira o tempo gasto na viagem em horas "))
    velocidade = int(input("Insira a velocidade media em km/h "))
    distancia = tempo * velocidade
    litros = distancia/rendimento

    print(f"Tempo gasto: {tempo}, Velocidade: {velocidade}, Distancia :{distancia}, litros: {litros}")

    return 0


if __name__=="__main__":
    
    input1 = input("Insira o primeiro numero ")
    input2 = input("Insira o segundo numero ")
    
    print(f"Soma = {soma(int(input1),int(input2))}, Sub = {sub(int(input1),int(input2))}, Mult = {mult(int(input1),int(input2))}, Div = {div(int(input1),int(input2))}")
    calcular_litros()
