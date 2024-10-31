# machine_learning_basics

## Exercicios
### Exercicio 1

Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

### Exercicio 2

Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução. Implemente cada exercício utilizando tanto o for quanto o while

Ler 5 notas e informar a média
Imprimir a tabuada do número 3 (3 x 1 = 3 ; 3 x 10 = 30)

### Exercicio 3

Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média


Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])


### Exercicio 4

Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão



Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)


### Exercicio 5

Crie um arquivo .py com duas funções
- Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
- Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)

### Exercicio 6

Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
- ValueError: se o usuário digitar um caracter
- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
- KeyboardInterrupt: caso o usuário interrompa a execução

### Exercicio 7

Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
- Cada aluno deve ocupar uma linha do novo arquivo de texto
- O formato deve ser: nome,nota (Pedro,8.0)
- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

### Exercicio 8

Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
- Números
- CEPs
- URLs

texto = " Minha casa fica na rua Carneiro,78. O CEP é 86388-000 e o meu site é https://www.iaexpert.academy"


### Exercicio 9

Crie uma classe chamada aluno com os seguintes atributos:
- Nome
- Nota 1
- Nota 2
- Crie um construtor para a classe (__init__)



Crie as seguintes funções (métodos):
- Calcula média, retornando a média aritmética entre as notas
- Mostra dados, que somente imprime o valor de todos os atributos
- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

Crie dois objetos (aluno1 e aluno2) e teste as funções