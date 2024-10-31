

def aula():

    class Triangulo:
    
        def __init__(self, lado1, lado2, lado3, base, altura):
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3
            self.base = base
            self.altura = altura

        def area(self):
            return (self.base*self.altura) / 2
        
        def tipo(self):
            if self.lado1 > self.lado2 + self.lado3:
                return 'não é um triangulo'
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return 'é um triangulo isóceles'
            else:
                return 'outro tipo de triângulo'

    t1 = Triangulo(2,2,3,4,3)
    print(t1.lado1, t1.lado2,t1.lado3,t1.base)
    
    t2 = Triangulo(8,9,20,16,2)
    print(t2.lado1, t2.lado2,t2.lado3)

    print(t2.area())
    print(t2.tipo())
    print(t1.tipo())

def exercicio():
    class Aluno:
        def __init__(self, nome,nota1,nota2):
            self.nome = nome
            self.nota1 = float(nota1)
            self.nota2 = float(nota2)
        def media(self):
            return float((self.nota1 + self.nota2)/2)
        def dados(self):
            return print(f"Nome: {self.nome}, Nota1: {self.nota1} , Nota2: {self.nota2}")
        
        def resultado(self):
            media = self.media()
            if media>6.0:
                texto = "Aluno aprovado"
            else:
                texto = "Aluno reprovado"
            return print(texto)

    aluno1 = Aluno("jose",10,5)
    aluno2 = Aluno("Jailson",3,6)

    aluno1.dados()
    print(f"Media = {aluno1.media()}")
    aluno1.resultado()

    aluno2.dados()
    print(f"Media = {aluno2.media()}")
    aluno2.resultado()

if __name__ == "__main__":
    exercicio()