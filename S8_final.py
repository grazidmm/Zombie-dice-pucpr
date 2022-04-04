"""" Aluna: Graziella Dias
     Curso: Análise e desenvolvimento de sistemas - turma 1
    Entrega final  do jogo Zombie Dice"""

import random
from collections import namedtuple
#from collections import namedtuple

print("Bem-vindo ao jogo Zombie Dice!")  # Mostra a mensagem entre aspas no terminal
print("=" * 100)
print("O jogador que devorar 13 cérebros primeiro ganha;")
print("O jogador que acumular 3 tiros perde a vez e tem o placar zerado;")
print("O jogador que tirar a face 'Passos' pode escolher entre jogar o dado novamente ou passar a vez.")
print("=" * 100)

def sorteio(x):
    #sorteados= []
    tubo = [green, green, green, green, green, green, yellow, yellow, yellow, yellow, red, red, red]
    #dado_escolhido = random.choices(tubo, k=x)
    #sorteados.append(dado_escolhido)
    return dado_escolhido

def lançamento(dado_escolhido):
    fc =[]
    for i in dado_escolhido:
        if i == 'CPCTPC':
            cara = random.choice('CPCTPC')
        elif i == 'TPCTPC':
            cara = random.choice('TPCTPC')
        elif i == 'TPTCPT':
            cara = random.choice('TPTCPT')
    fc.append(cara)
    return fc
dado_escolhido = sorteio(x)

def most():
    for i in lançamento():
        score = []
        if i == "T":
            tiros += 1
        elif i == "P":
            passos += 1
        elif i == "C":
            cerebros += 1
    score = [tiros, passos, cerebros]
    return score









jogadores = 0
while jogadores < 2:  # Enquanto a variavel jogadores for menor que 2, ele imprimirá o comando if
    jogadores = int(input("Digite o número de jogadores em números inteiros :"))

    if jogadores < 2:
        print(
            "Olá! Esse jogo é recomendado para 2 players no mínimo, vamos tentar novamente?\n")  # \n é a quebra de linha
    else:
        print(
            "É uma ótima quantidade de cérebros apetit-, ops, brilhantes para o jogo!")  # se a quantidade for maior que 2, ele prossegue e mostra essa mensagem
atual = []  # lista que irá receber só os nomes
nome_jogadores = []  # cria uma lista que armazena o nome e score dos jogadores através do dicionário
i = 0
while i < jogadores:  # Para i menor que o número de jogadores, o i percorre até o mesmo valer jogdores
    jgdrs = input(f"Insira o nome do jogador {i + 1} :")  # Função format para mostrar o número do  jogador
    jogador = {"Jogador": jgdrs, "pontos": 0, "tiros": 0}  # Criação de um dicionário que define cada termo entre aspas
    nome_jogadores.append(jogador)  # add o dicionário a lista
    atual.append(jgdrs)  # add os nomes a lista
    i += 1
    # print(nome_jogadores)

# Enquanto o que estiver abaixo for verdade:
while True:
    inicio = input("Deseja iniciar o jogo? Digite 's' para sim ou  'n' para não:")
    if inicio == "s":
        print("Iniciando o jogo...")
        break  # para a perguntar não ser repetida várias vezes, uso o "break" para quebrar o looping
    elif inicio == "n":
        continue  # o "continue" continua repetindo o inicio do while ("variável "início" até receber a resposta que quebra o loop ("s").
    else:
        print("Comando inválido!")

jogador_atual = 0  # crio as variáveis que irá mostrar os pontos de tiros, cerebros, passos e definir um valor iniciar para jogador atual
tiros = 0
cerebros = 0
passos = 0
dadosorteado = []  # lista vazia dos dados ja sorteados

# lista vazia para armazenar os cerebros e tiros
cer = list()
tir = list()

# adiciona a variavel cerebros e a variável tiros nas listas (cer = 0 e tir = 0 com a adição, inicialmente)
cer.append(cerebros)
tir.append(tiros)

# Mostra o turno dos jogadores:
j = 0
while j < len(atual):  # enquanto j  for menor que os elementos do atual (jogadores), ele começa a rodada
    print("Turno do jogador", atual[j])

    dados = namedtuple('dados', ['Vermelho', 'Verde', 'Amarelo'])
    facex = dados(Vermelho='TPTCPT', Verde='CPCTPC', Amarelo='TPCTPC', )
    green = facex.Verde
    red = facex.Vermelho
    yellow = facex.Amarelo

    tubo = [green,green, green, green, green, green, yellow, yellow, yellow,yellow, red, red, red]  # Armazena na lista tubo a quantidade de dados definidos nas tuplas
    random.shuffle(tubo)  # embaralha os dados no tubo
    dado_escolhido = random.choices(tubo,k=3)  # escolhe aleatoriamente 3 dados do tubo

    faces = []  # Lista vazia para armazenar as faces sorteadas de cada dado
    for i in dado_escolhido:
        if i == facex.Verde:
            face = random.choice('CPCTPC')
            print("VOCÊ TIROU UM DADO: VERDE")
        elif i == facex.Amarelo:
            face = random.choice('TPCTPC')
            print("VOCÊ TIROU UM DADO: AMARELO")
        elif i == facex.Vermelho:
            face = random.choice('TPTCPT')
            print("VOCÊ TIROU UM DADO: VERMELHO")
        faces.append(face)  # adiciona as faces sorteadas na lista

    '''print("A primeira face sortida foi:",
          faces[0])  # "[]" mostra a posição (index) do elemento, no caso o primeiro dado sorteado
    print("A segunda face sortida foi:",
          faces[1])  # "[]" mostra a posição (index) do elemento, no caso o segundo dado sorteado
    print("A terceira face sortida foi:",
          faces[2])  # "[]" mostra a posição (index) do elemento, no caso o segundo dado sorteado'''

    # Definindo novamente para n haver problemas no loop
    cerebros = 0
    tiros = 0
    passos = 0
    # Mostra o resultado do primeiro dado sorteado e a mensagem, (a contagem começa em 0) e somando os pontos a variável
    if faces[0] == "C":
        print("A face do seu dado foi:", " ' ", faces[0], " ' ", "*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!***")
        cerebros += 1
    elif faces[0] == "T":
        print('A face do seu dado foi:', " ' ", faces[0], " ' ",
              "*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva ***")
        tiros += 1
    elif faces[0] == "P":
        print('A face do seu dado foi:', " ' ", faces[0], " ' ", "*** A VÍTIMA FUGIU ***!!")
        passos += 1

    # Mostra o resultado do segundo dado sorteado e a mensagem e somando os pontos a variável
    if faces[1] == "C":
        print("A face do seu dado foi:", " ' ", faces[1], " ' ", "*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!***")
        cerebros += 1
    elif faces[1] == "T":
        print('A face do seu dado foi:', " ' ", faces[1], " ' ",
              "*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva ***")
        tiros += 1
    elif faces[1] == "P":
        print('A face do seu dado foi:', " ' ", faces[1], " ' ", "*** A VÍTIMA FUGIU ***!!")
        passos += 1

    # Mostra o resultado do terceiro dado sorteado e a mensagem e somando os pontos a variável
    if faces[2] == "C":
        print("A face do seu dado foi:", " ' ", faces[2], " ' ", "*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!***")
        cerebros += 1
    elif faces[2] == "T":
        print('A face do seu dado foi:', " ' ", faces[2], " ' ",
              "*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva ***")
        tiros += 1
    elif faces[2] == "P":
        print('A face do seu dado foi:', " ' ", faces[2], " ' ", "*** A VÍTIMA FUGIU ***!!")
        passos += 1

    cer[j] += cerebros  # adiciona a variavel int a lista
    tir[j] += tiros

    # adiciona as listas com os cerebros e tiros ao dicionário do jogador da vez
    nome_jogadores[j]["pontos"] = cer[j]
    nome_jogadores[j]["tiros"] = tir[j]
    # printa o score atual do jogador da vez
    print("O score do jogador ", atual[j], " é: ",
          nome_jogadores[j]["pontos"], " pontos e ",
          nome_jogadores[j]["tiros"], " tiros")

    if nome_jogadores[j][
        "pontos"] >= 13:  # mostra a mensagem de vencedor caso o termo "pontos" no dicionário tenha mais ou 13 pontos
        print("jogador ", atual[j], " você ganhou!!!!!")
        break

    if nome_jogadores[j]["tiros"] >= 3:  # zera a pontuação caso o jogador atual tenha tirado 3 tiros
        print("jogador ", atual[j],
              " você tomou 3 tiros e perdeu os pontos")  # mostra o nome do jogador atual e a mensagem
        nome_jogadores[j]["pontos"] = 0
        nome_jogadores[j]["tiros"] = 0

    novamente = input("Voce deseja jogar novamente? Digite 's' ou 'n' ")  # para a continuação do jogo

    if novamente == 's':  # se o jogador desejar continuar, repete o turno
        continue
    elif novamente == 'n':  # se o jogador n desejar jogar novamente, passa para o próximo jogador
        cerebros = 0  # zera as pontuações para n serem somadas ao socre do próximo jogador
        tiros = 0
        passos = 0
        cer.append(cerebros)  # add as pontuações zeradas para não interferir no score
        tir.append(tiros)

        if j == len(atual) - 1:  # se o jogador atual (j) for igual ao número de jogadores, o protótipo acaba
            print("Acabou o número de jogadores")
            break
        else:  # caso ele ainda seja diferente (menor) que a quantidade de jogadores, ele passa para o próximo jogador "j"
            j += 1

print("o score final dos jogadores foi : ", nome_jogadores)  # printa o resultado







