# Autor: Gerson Ferreira dos Anjos Neto
# Componente Curricular: Algoritmos I
# Concluído em: 07/04/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou
# de outro autor, tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet.
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Declaração/Inicialização dos vetores que serão utilizados na saída de dados.
Itens = ["Açúcar", "Arroz", "Café", "Extrato de Tomate", "Macarrão", "Bolacha", "Óleo", "Farinha", "Feijão",
         "Sal", "Extras"]
Unidades = ["Kg", "Kg", "Kg", "Un", "Un", "Pct", "L", "Kg", "Kg", "Kg", "Un"]

# Declaração/Inicialização do vetor que será utilizado na validação/montagem das cestas.
Validar = [1, 4, 2, 2, 3, 1, 1, 1, 4, 1, 1]

# Declaração/Inicialização dos vetores que serão utilizados para armazenar os valores das doações. O indice dos...
# vetores nas lista Fisica e Juridica vai de 0-11 sendo que as 11 primeiras posições são destinadas a armazenar a...
# quantidade de itens por tipo (seguindo a ordem da lista Itens), a 12ª posição e destinada ao total de itens doados...
# pelo respectivo tipo de pessoa (cálculo feito posteriormente no código).
Fisica = [0] * 12
Juridica = [0] * 12
Total = [0] * 11

# Variáveis acumulador para a contagem das cestas.
quantidadeCestas = quantidadeCestasComExtra = 0

# Variáveis booleanas para o controle de menus, quantidade de doações e montagem das cestas.
validar = continuar = fazerDoacao = montarCesta = montarCestaComExtra = True


# Função 'somaTotal" - Percorre as listas: Total, Fisica e Juridica. Armazena em Total a soma das quantidades de...
# Fisica e Juridica na posição 'i' respeitando o tamanho das lista e a posição de seus elementos.
def somaTotal():
    for i in range(len(Total)):
        Total[i] = Fisica[i] + Juridica[i]


# Início do programa.
while continuar:

    # Menu Inicial - O usuário irá inserir 1, 2 ou 3 de acordo com o que deseje fazer, o programa não aceitara...
    # nenhuma entrada diferente dessas e a escolha será armazenada na variável 'menuInicial".
    print("=" * 10, "Sistema de Gerenciamento de Doações", "=" * 10)
    print("1 - Cadastrar Novo Doador")
    print("2 - Ver Relatório")
    print("3 - Finalizar Dia")
    menuInicial = input()

    while validar:
        try:
            if int(menuInicial) not in range(1, 4):
                raise ValueError
            else:
                validar = False
        except ValueError:
            menuInicial = input("Opção inválida, tente novamente: ")
    menuInicial = int(menuInicial)
    validar = True

    # Opção 3 (Finalizar o dia) - O loop inicial e quebrado e o programa prossegue a partir da linha XXX.
    if menuInicial == 3:
        continuar = False

    # Opção 2 (Ver Relatório) - Um relatório parcial e impresso, contendo as quantidades de itens doados por tipo...
    # utilizando a função 'somaTotal' para obter as quantidades e percorrendo as listas (Itens, Total, Unidades) por...
    # meio de um 'for" que realiza os "prints".
    elif menuInicial == 2:

        somaTotal()

        print("=" * 19, "Relatório Parcial", "=" * 19)
        print("Quantidade de Itens doados:")
        for i in range(len(Total)):
            print("-", Itens[i], "-", Total[i], Unidades[i])

    # Opção 1 (Cadastrar Novo Doador) - Inicia o processo de doação.
    else:

        # Menu de Doação - O usuário devera inserir o nome do Doador ("Perfumaria'), o tipo de pessoa...
        # (Física ou Jurídica). Esse ultimo e validado levando em consideração possiveis erros de digitação.
        print("Insira o nome do doador: ")
        nomeDoador = input()
        print("Qual o tipo de pessoa? (Física ou Jurídica): ")
        tipoPessoa = input()

        while tipoPessoa.lower().replace(" ", "")[0] not in "fj":
            tipoPessoa = input("Opção inválida, tente novamente: ")
        print("Seja bem-vindo(a), {}!".format(nomeDoador))

        fazerDoacao = True

        while fazerDoacao:

            # Menu de Itens - O usuário devera inserir um número de 1-11 representando o item escolhida e depois a...
            # sua respectiva quantidade a ser doada. O sistema não aceitaram nenhum número diferente das opções...
            # disponíveis, também não aceitara valor menor ou igual a 0 para a quantidade doada. Esses valores são...
            # armazenado respectivamente nas variáveis "tipoItem" e "quantidadeItem".
            print("=" * 9, "Selecione o tipo de item a ser doado:", "=" * 9)
            print("1 - Açúcar")
            print("2 - Arroz")
            print("3 - Café")
            print("4 - Extrato de Tomate")
            print("5 - Macarrão")
            print("6 - Bolacha")
            print("7 - Óleo")
            print("8 - Farinha")
            print("9 - Feijão")
            print("10 - Sal")
            print("11 - Extras")
            tipoItem = input("Item:\n")
            while validar:
                try:
                    int(tipoItem)
                    if int(tipoItem) not in range(1, 12):
                        raise ValueError
                    validar = False
                except ValueError:
                    tipoItem = input("Opção inválida, tente novamente: ")
            tipoItem = int(tipoItem)
            validar = True

            quantidadeItem = input("Quantidade: ")
            while validar:
                try:
                    float(quantidadeItem)
                    if float(quantidadeItem) <= 0:
                        raise ValueError
                    validar = False
                except ValueError:
                    quantidadeItem = input("Opção inválida, tente novamente: ")
            quantidadeItem = float(quantidadeItem)
            validar = True

            # A variável 'tipoItem' será utilizada para apontar a posição onde será somada a o valor de...
            # "quantidadeItem" na respectiva lista referente ao tipo de pessoa escolhida.
            if tipoPessoa.lower().replace(" ", "")[0] == "f":
                Fisica[tipoItem - 1] += quantidadeItem
            else:
                Juridica[tipoItem - 1] += quantidadeItem

            # Etapa Final - O usuário recebe a opção de realizar uma nova doação. Caso "Sim" o programa retorna a sua...
            # execução a partir da linha 86. Caso "Não", é dada a opção de visualizar o relatório parcial é o ciclo...
            # de doação se encerrar, por meio da alteração do valor do booleano "fazerDoacao" para 'False"...
            # essa mesma variável e reiniciada como "True" para receber os dados de um novo doador, caso o dia não...
            # seja finalizado.
            print("Item adicionado com sucesso!\nDeseja fazer outra doação? (Sim ou Não)")
            novaDoacao = input()

            while novaDoacao.lower().replace(" ", "")[0] not in "sn":
                novaDoacao = input("Opção inválida, tente novamente: ")

            if novaDoacao.lower().replace(" ", "")[0] == "n":
                print("Doação finalizada!")
                print("Ver relatório parcial? (Sim ou Não):")
                relatorioParcial = input()

                while relatorioParcial.lower().replace(" ", "")[0] not in "sn":
                    relatorioParcial = input("Opção inválida, tente novamente: ")

                if relatorioParcial.lower().replace(" ", "")[0] == "s":

                    somaTotal()
                    print("=" * 19, "Relatório Parcial", "=" * 19)
                    print("Quantidade de Itens doados:")
                    for i in range(len(Total)):
                        print("-", Itens[i], "-", Total[i], Unidades[i])

                fazerDoacao = False

# Relatório Diário - Inicia da mesma forma que o relatório parcial, utilizando a função "somaTotal", as listas...
# (Fisica, Jurídica e Total) e a estrutura "for" para dar "print" nos itens por tipo.
somaTotal()
print("=" * 16, "Relatório Diário", "=" * 16)
print("\nQuantidade de Itens Recebidos (Por Tipo de Item):")

for i in range(len(Total)):
    print("-", Itens[i], "-", Total[i], Unidades[i])

print("\nQuantidade de Itens (Por Tipo de Pessoa):")

# Os itens por tipo de pessoa são computados por meio de uma estrutura "for" que percorre as lista...
# (Física e Jurídica) dividi os valores em cada posição pelos seus equivalentes na lista Validar, e soma os valores...
# resultantes na posição destinada ao total por tipo de pessoa (Fisica[11] e Juridica[11]).
for i in range(len(Fisica) - 1):
    Fisica[i] //= Validar[i]
    Fisica[11] += Fisica[i]

for i in range(len(Juridica) - 1):
    Juridica[i] //= Validar[i]
    Juridica[11] += Juridica[i]

print("- Pessoa Física - {}".format(int(Fisica[11])))
print("- Pessoa Jurídica - {}".format(int(Juridica[11])))
print("\nQuantidade de Cestas Formadas:")

# As cestas são montadas em quanto a quantidade de itens obrigatórios para formação de uma cesta forem maiores do que...
# os valore pré-estabelecidos, as quantidades utilizadas são subtraidas e o número de cestas e incrementado.
while montarCesta:
    if Total[0] >= 1 and Total[1] >= 4 and Total[2] >= 2 and Total[3] >= 2 and Total[4] >= 3 and \
            Total[5] >= 1 and Total[6] >= 1 and Total[7] >= 1 and Total[8] >= 4 and Total[9] >= 1:
        Total[0] -= 1
        Total[1] -= 4
        Total[2] -= 2
        Total[3] -= 2
        Total[4] -= 3
        Total[5] -= 1
        Total[6] -= 1
        Total[7] -= 1
        Total[8] -= 4
        Total[9] -= 1
        quantidadeCestas += 1
    else:
        montarCesta = False

print("{} Cesta(s)".format(int(quantidadeCestas)))
print("\nQuantidade de Cestas com Item Extra:")

# A cestas com item extra são calculadas em dois casos:
# [1] Se o número de itens extras for maior ou igual a quantidade cestas, a "quantidadeCestasComExtra" é igual a...
# quantidade de itens extras e a quantidade restante de itens extra e a diferença pela quantidade de cestas com...
# item extra.
if Total[10] >= quantidadeCestas:
    quantidadeCestasComExtra = quantidadeCestas
    Total[10] -= quantidadeCestasComExtra
# [2] Caso o número de itens extras seja menor que o número de cestas, a "quantidadeCestasComExtra" é igual a...
# quantidade de itens extras. Nesse caso não sobram itens extras, logo a variável e recebe 0.
else:
    quantidadeCestasComExtra = Total[10]
    Total[10] = 0

print("{} Cesta(s)".format(int(quantidadeCestasComExtra)))
print("\nQuantidade de Cestas sem Item Extra:")
print("{} Cesta(s)".format(int(quantidadeCestas - quantidadeCestasComExtra)))

# Os itens restantes são impressos da seguinte forma:
# [1] Se a soma dos itens em "Total" for maior que zero, restam itens que serão impressos utilizando uma estrutura...
# "for" para percorrer as listas (Total e Itens) e realizar os "prints".
if sum(Total) > 0:
    print("\nQuantidade de Itens Sobrando:")
    for i in range(len(Total)):
        if Total[i] > 0:
            print("-", Itens[i], "-", Total[i], Unidades[i])
# [2] Caso a soma seja igual a zero, o usuário é informado que não restaram itens.
else:
    print("\nNão restou nenhum item.")
