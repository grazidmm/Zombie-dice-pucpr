"""" Aluna: Graziella Dias
     Curso: Análise e desenvolvimento de sistemas - turma 1
     entrega do jogo Zombie Dice"""

import random
from collections import namedtuple

print("Bem-vindo ao jogo Zombie Dice!")  # Mostra a mensagem entre aspas no terminal
print("=" * 100)
print("O jogador que devorar 13 cérebros primeiro ganha;")
print("O jogador que acumular 3 tiros perde os cérebros da rodada;")
print("O jogador que tirar a face 'Passos' e quiser jogar novamente, continua com o dado e  completa com os demais aleatórios do tubo.")
print("=" * 100)


def Njogadores(jogadores):
    while jogadores < 2:  # Enquanto a variavel jogadores for menor que 2, ele imprimirá o comando if
        jogadores = int(input("Digite o número de jogadores em números inteiros :"))

        if jogadores < 2:
            print(
                "Olá! Esse jogo é recomendado para 2 players no mínimo, vamos tentar novamente?\n")  # \n é a quebra de linha
        else:
            print(
                "É uma ótima quantidade de cérebros apetit-, ops, brilhantes para o jogo!")
        return jogadores

def nomes(i):
    while i < QTDJogs:  # Para i menor que o número de jogadores, o i percorre até o mesmo valer jogdores
        jgdrs = input(f"Insira o nome do jogador {i + 1} :")  # Função format para mostrar o número do  jogador
        jogador = {"Jogador": jgdrs, "pontos": 0,
                   "tiros": 0}  # Criação de um dicionário que define cada termo entre aspas
        nome_jogadores.append(jogador)  # add o dicionário a lista
        atual.append(jgdrs)  # add os nomes a lista
        i += 1

def iniciar():
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
            continue

def dado_retirado():
    dados_atuais = []
    mãos = len(ddmão)
    pegar = 3 - mãos
    if len(tubo) < pegar: #caso os dados no tubo sejam insuficientes para completar a rodada, coloca todos os dados de volta
        mesa = len(ddmesa)
        for i in range(mesa):
            retomar = ddmesa.pop()
            tubo.append(retomar)
    for i in range(pegar):
        random.shuffle(tubo)
        sorteio = tubo.pop()
        dados_atuais.append(sorteio)
        ddmesa.append(sorteio)
    if mãos != 0:
        for i in range(mãos):
            sort_m = ddmão.pop()
            dados_atuais.append(sort_m)
    return dados_atuais


def tamanho():
    qt = len(tubo)
    mesa = len(ddmesa)
    if qt != 0:
        print("=" * 50)
        print("Há", qt, "dados no tubo.")
        print("=" * 50)
    else:
        print("=" * 50)
        print("Não há mais dados! Tubo vazio.")
        print("=" * 50)
    return '-----Quantidade atual de dados-----'


def cores(dadoesc):
    for i in dadoesc:
        if i == 'CPCTPC':
            cara = random.choice('CPCTPC')
            print("VOCÊ TIROU UM DADO: VERDE")
        elif i == 'TPCTPC':
            cara = random.choice('TPCTPC')
            print("VOCÊ TIROU UM DADO: AMARELO")
        elif i == 'TPTCPT':
            cara = random.choice('TPTCPT')
            print("VOCÊ TIROU UM DADO: VERMELHO")
        faces.extend(cara)
    if faces[0] == 'P':
        ddmão.append(dadoesc[0])
    if faces[1] == 'P':
        ddmão.append(dadoesc[1])
    if faces[2] == 'P':
        ddmão.append(dadoesc[2])
    return faces


def dice(faces):
    for i in faces:
        if i == "T":
            pontos_jogador[0] += 1
        elif i == "C":
            pontos_jogador[1] += 1
        elif i == "P":
            pontos_jogador[2] += 1


def análise(faces):
    for i in faces:
        if i == "C": print("*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!! ***\n")
        if i == "P": print("*** A VÍTIMA FUGIU ***!!\n")
        if i == "T": print("*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva. ***\n")
    return "-----Esses foram os pontos da rodada-----"


# ======================================================================
#Uso da tupla para definir as faces dos dados
dados = namedtuple('dados', ['Vermelho', 'Verde', 'Amarelo'])
facex = dados(Vermelho='TPTCPT', Verde='CPCTPC', Amarelo='TPCTPC')
green = facex.Verde
red = facex.Vermelho
yellow = facex.Amarelo
#add os dados no tubo
tubo = [green, green, green, green, green, green, yellow, yellow, yellow, yellow, red, red, red]

jogadores = 0
QTDJogs = Njogadores(jogadores)  # chama a função que pergunta a quantidade de jogadores

ddmesa = []  # dados já sorteados que ficam fora do tubo
ddmão = []  # sempre passos, lista criada para manter o dado passos e jogar ele novamente caso o jogador queira
atual = []  # lista que irá receber só os nomes
nome_jogadores = []  # cria uma lista que armazena o nome e score dos jogadores através do dicionário
pontos_jogador = [0, 0, 0] #lista para receber os pontos de passos, tiros e cérebros

i = 0
names = nomes(i)  #chama lista que pergunta o nome dos jogadores
startar = iniciar() #chama a lista que pergunta se o jogador quer jogar novamente ou não

j = 0
while j < len(atual):  # enquanto j  for menor que os elementos do atual (jogadores), ele começa a rodada
    if len(tubo) == 0:
        mesa = len(ddmesa)
        for i in range(mesa):
            retomar = ddmesa.pop()
            tubo.append(retomar)

    print("Turno do jogador", atual[j])
    faces = []  # Lista vazia para armazenar as faces sorteadas de cada dado (lista para ajudar na função que mostra a face
    dadoesc = dado_retirado() # Chama a função que retira os dados aleatoriamente do tubo
    print(dadoesc)
    color = cores(dadoesc)#chama a função que define as cores de acordo com os dados sorteados na função dadoesc(usada como parâmetro)
    print(color)
    pontos = dice(faces)#chama a função que adiciona os pontos do jogador de acordo com as faces tiradas
    qtd = tamanho()#chama a função que mostra a quantidade dos dados do tubo
    anl = análise(faces)#chama a função que mostra a mensagem das faces de cada dado

    nome_jogadores[j]["pontos"] += pontos_jogador[1]
    nome_jogadores[j]["tiros"] += pontos_jogador[0]

    if nome_jogadores[j]["tiros"] >= 3:  # zera a pontuação da rodada caso o jogador atual tenha tirado 3 tiros
        print("jogador ", atual[j],
              " você tomou 3 tiros,perdeu os pontos da rodada e a vez.")  # mostra o nome do jogador atual e a mensagem
        #print("Infelimente para você.... Agora é a vez do(a)", atual[j + 1])
        for i in faces: #retira os pontos ganhos na rodada
            if i == "T":
                pontos_jogador[0] -= 1
            elif i == "C":
                pontos_jogador[1] -= 1
            elif i == "P":
                pontos_jogador[2] -= 1
        pontos_jogador = [0, 0, 0]
        ddmão = []
        input("Vamos jogar?")
        j += 1
        continue
    else:
        # printa o score atual do jogador da vez
        print("O score do jogador ", atual[j], " é: ",
              nome_jogadores[j]["pontos"], " pontos e ",
              nome_jogadores[j]["tiros"], " tiros")

        if nome_jogadores[j][
            "pontos"] >= 13:  # mostra a mensagem de vencedor caso o termo "pontos" no dicionário tenha mais ou 13 pontos
            print("jogador ", atual[j], " você ganhou!!!!!")
            break

        novamente = input("Voce deseja jogar novamente? Digite 's' ou 'n': ")  # para a continuação do jogo

        if novamente == 's':# se o jogador desejar continuar, repete o turno
            pontos_jogador = [0,0,0]
            continue
        elif novamente == 'n':  # se o jogador n desejar jogar novamente, passa para o próximo jogador
            ddmão = []
            if j == len(atual) - 1:  # se o jogador atual (j) for igual ao número de jogadores, volta para o jogador 0
                j = 0
                # dados já sorteados que ficam fora do tubo
                pontos_jogador = [0, 0, 0]
            else:  # caso ele ainda seja diferente (menor) que a quantidade de jogadores, ele passa para o próximo jogador "j"
                pontos_jogador = [0, 0, 0]
                j += 1
print("o score final dos jogadores foi : ", nome_jogadores)  # printa o resultado





