import numpy as np

def aula():
    coleta = {'mosquito':2, 'cao':3}
    coleta2 = { 'gato':3}
    coleta.update(coleta2)
    for especie, num_especies in coleta.items():
        print(f"especie = {especie}, numero de especimes: {num_especies}")

    biomol = ('proteina', 'gordura', 'acidos', 'carbo', 'proteina','carbo','carbo')

    print(set(biomol))

    c1 = {1,2,3,4,5}
    c2 = {3,4,5,6,7}
    print(c1.difference(c2))

def aula2():
    matriz = np.array([[2,3,1],[4,5,7]])
    # print(matriz)
    # print(matriz.shape)
    # print(matriz[0])
    # print(matriz[0][2])

    for i in range (matriz.shape[0]):
        # print(matriz[i])
        for j in range (matriz.shape[1]):
            print(matriz[i][j])

def exercicio_lista():

    lista=[]
    soma = 0

    for i in range (1,6):
        lista.append(i)  
        print(lista)      

    for i in lista:
        soma = soma + i

    print(f"soma = {soma}")


def exercicio_dict():

    dict = {'Ze':3, 'Jorge':10, 'Ana':8}
    soma=0
    media = 0
    nota = 0

    for aluno, nota in dict.items():
        print(f"Aluno: {aluno}, Nota: {nota}")
        soma = soma+nota

    media = soma/len(dict)
    print(f"Media: {media}")

def exercicio_matriz():
    matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
    
    soma = 0
    for i in range (matriz.shape[0]):
        for j in range (matriz.shape[1]):
            soma = soma + matriz[i][j]
    print(f"soma = {soma}")

if __name__=="__main__":
    # aula()
    #aula2()
    #exercicio_matriz()