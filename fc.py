import random
from collections import namedtuple
from random import randint

dados = namedtuple('dados', ['Vermelho', 'Verde', 'Amarelo'])
facex = dados(Vermelho='TPTCPT', Verde='CPCTPC', Amarelo='TPCTPC')
green = facex.Verde
red = facex.Vermelho
yellow = facex.Amarelo

tubo = [green, green, green, green, green, green, yellow, yellow, yellow, yellow, red, red, red]

passos = 0
dadosorteado = []
def mão(passos):
    dados_mão = 3 - passos
    return dados_mão



def dado_escolhido():
    for i in range(mão(passos)):
        random.shuffle(tubo)
        sorteio = tubo.pop()
        dadosorteado.append(sorteio)
    return dadosorteado

print(dado_escolhido())

faces = []
def cores():
    for i in range(dado_escolhido()):
        if i == 'CPCTPC':
            face = random.choice('CPCTPC')
            print("VOCÊ TIROU UM DADO: VERDE")
        elif i == 'TPCTPC':
            face = random.choice('TPCTPC')
            print("VOCÊ TIROU UM DADO: AMARELO")
        elif i == 'TPTCPT':
            face = random.choice('TPTCPT')
            print("VOCÊ TIROU UM DADO: VERMELHO")
        faces.append(face)
    return faces


print(faces)

def dice(faces):
    for i in cores():
        if i == 'T':
            tiros += 1
            print("A FACE DO SEU DADO FOI 'TIRO'\n","*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva ***")
        elif i == 'C':
            cérebros += 1
            print("A FACE DO SEU DADO FOI 'CÉREBRO'\n","*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!***")
        elif i == 'P':
            passos += 1
            print("A FACE DO SEU DADO FOI 'PASSOS'\n","*** A VÍTIMA FUGIU ***!!")



tiros = 0
cérebros = 0
cer = []
tir = []
cer.append(cérebros)
tir.append(tiros)


jgdrs = input(f"Insira o nome do jogador :")
jogador = {"Jogador": jgdrs, "pontos": 0, "tiros": 0}
nome_jogadores.append(jogador)  # add o dicionário a lista
atual.append(jgdrs)


print(cores())
print (dice(faces))

def turno(cer,tir,pas)
    while True:
        novamente = input("Voce deseja jogar novamente? Digite 's' ou 'n' ")
        if novamente == 's':
            continue
        elif novamente == 'n':
            cer = 0
            tir = 0
            pas = 0
            cer.append(cerebros)
            tir.append(tiros)









