
def aula():
    try:
        n = int(input('Digite um numero inteiro '))
    except:
        print("Valor invalido")
    else:
        print(f"Valor digitado é : {n}")


def aula1():
    while True:
        try:
            p=int(input("digite um numero inteiro "))
        except ValueError:
            print("Valor invalido ")
        except KeyboardInterrupt:
            print("Codigo Interrompido ")
            break
        else:
            print(f"Valor digitado é {p}")


def exercicio():

    while True:

        lista = []

        try:
            lista.append(float(input("Valor 1: ")))
            lista.append(float(input("Valor 2: ")))
            div = lista[0]/lista[2]
        except ZeroDivisionError:
            print("Divisão por zero detectada")
        except ValueError:
            print("Caracter detectado")
        except IndexError:
            print("Invalid index on list")
        except KeyboardInterrupt:
            print("Codigo interrompido ")
            break
        else:
            print(f"Divisao = {div}")

if __name__=="__main__":
    exercicio()