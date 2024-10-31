

def aula():
    # print("ex7")
    with open('exercicios/texto.txt') as tex:
        # for linha in tex:
        #     print(linha)
        r = tex.readlines()
        
        print(r)
    with open('exercicios/texto2.txt','w') as texto:
        texto.write("Olá a todos")


def exercicio():
    alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

    with open('exercicios/exercicio.txt','w') as ex_w:
        for nome,nota in alunos.items():
            ex_w.write(f"{nome}, {nota} \n")

    with open('exercicios/exercicio.txt','r') as ex_r:
        for lines in ex_r:
            print(lines)

if __name__=="__main__":
    exercicio()