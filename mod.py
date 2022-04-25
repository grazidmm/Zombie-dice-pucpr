#Módulo das funções


passos = 0 # precisa estar no código original
dados_mesa = []
def mão(passos): # função dos dados na mão
    dados_mão = 3 - passos
    return dados_mão


def dado_escolhido(): #função que retira 3 dados aleatórios do final do tubo e armazena os dados sorteados
    for i in range(mão(passos)):
        random.shuffle(tubo)
        sorteio = tubo.pop()
        dados_mesa.append(sorteio)
    return dados
print(dado_escolhido())

faces = []
def cores():
    for i in range(dado_escolhido()):
        if i == facex.Verde:
            face = random.choice('CPCTPC')
            print("VOCÊ TIROU UM DADO: VERDE")
        elif i == facex.Amarelo:
            face = random.choice('TPCTPC')
            print("VOCÊ TIROU UM DADO: AMARELO")
        elif i == facex.Vermelho:
            face = random.choice('TPTCPT')
            print("VOCÊ TIROU UM DADO: VERMELHO")
        faces.append(face)

def dice(faces):
    for i in range(faces):
        if i == 'T':
            print("A FACE DO SEU DADO FOI 'TIRO'\n","*** VOCÊ ACABOU DE LEVAR UM TIRO! 3 tiros e vc ta mortinho da silva ***")
        elif i == 'C':
            print("A FACE DO SEU DADO FOI 'CÉREBRO'\n","*** VOCÊ ACABOU DE DEVORAR UM CÉREBRO!***")
        elif i == 'P':
            print("A FACE DO SEU DADO FOI 'PASSOS'\n","*** A VÍTIMA FUGIU ***!!")








