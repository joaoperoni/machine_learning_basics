import re


frase = 'Olá, meu número de telefone é (42)0000-0000'
frase2 = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
email = 'Entre em contato, meu email é teste@teste.com'
frase3 = 'FeT-1992 é a placa do carro'
frase4 = 'Olá, meu número de telefone é (42)0000-0000. O numero (56)11111-1111 é o antigo'
emails = ''' Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

def search():
    print(re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase))
    print(re.search(r'[A-Za-z]{3}-\d{4}',frase2))
    print(re.search(r'\w+@\w+\.com',email))

def match():
    print(re.match(r'[A-Za-z]{3}-\d{4}',frase3))

def findall():
    print(re.findall(r'\(\d{2}\)\d{4,5}-\d{4}',frase4))
    print(re.findall(r'\w+@\w+\.\w*',emails))
    
def exercicio():
    texto = " Minha casa fica na rua Carneiro,78. O CEP é 86388-000 e o meu site é https://www.iaexpert.academy/ ou https://aexpert.academy/"
    numero = re.findall(r'\d',texto)
    CEP = re.findall(r'\d{5}-\d{3}',texto)
    site = re.findall(r'https?://[A-Za-z0-9./]+',texto)

    print(f"Numero: {numero}, CEP: {CEP}, site: {site}")


if __name__ == "__main__":
    # search()
    # match()
    # findall()
    exercicio()