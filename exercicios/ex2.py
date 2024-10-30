def calc_media_for():
    soma = 0
    media = 0
    
    for nota in range (1,6):
        soma = soma + nota
        print(f"nota = {nota}")
        
    media = soma/5
    print(f"Media = {media}")

def calc_media_while():
    
    soma = 0
    media = 0
    nota = 0

    while nota < 5:
        nota = nota + 1
        soma = soma + nota
        print(f"Nota = {nota}")
    media = soma/nota
    
    print(f"Media = {media}")


def imprimir_tabuada_for():
    
    for i in range (0,11):
        print(f"3*{i} = {3*i}")

def imprimir_tabuada_while():
    i = 0
    while i < 11:
        print(f"3*{i} = {3*i}")
        i = i+1

if __name__=="__main__":
    calc_media_for()
    calc_media_while()
    imprimir_tabuada_for()
    imprimir_tabuada_while()