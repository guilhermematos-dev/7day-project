import time
import sys
import random

''' Funções de imersão '''
def pausa_curta():
    time.sleep(1)

def pausa_longa():
    time.sleep(2)

def animacao(letra, velocidade=0.05):
    for char in letra:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

''' Funções de jogabilidade'''

personagem = {
    "guerreiro": {"nome": "Guerreiro", "vida": 100, "força": 15},
    "mago": {"nome": "Mago", "vida": 70, "força": 25},
    "arqueiro": {"nome": "Arqueiro", "vida": 80, "força": 20}
}

direcoes = ['esquerda', 'direita', 'frente']

armadilha = ["Você pisa em uma armadilha de espinhos...", "Uma flecha dispara de uma parede em sua direção...", "O chão está cedendo sob seus pés...", "Uma corda te puxa para cima..."]

inimigos = {
    "ratos": {"nome": "Horda de ratos", "vida": 145, "força": 3, "descricao": "Uma horda de ratos gigantes aparecem em sua direção, sedentos por carne fresca!"},
    "rastejante": {"nome": "Rastejante", "vida": 45, "força": 20, "descricao":"Um rastejante vem lentamente em sua direção... Ele parece estar sofrendo... e faminto."},
    "esqueleto": {"nome": "Esqueleto", "vida": 60, "força": 25, "descricao": "Ossos começam a se juntar de cadaveres antigos, formando um esqueleto rancoroso!"},
    "zumbi": {"nome": "Zumbi", "vida": 75, "força": 30, "descricao": "Barulhos de correntes ecoam pela masmorra... Um zumbi faminto está vindo em sua direção!"},
    "fantasma": {"nome": "Fantasma", "vida": 20, "força": 35, "descricao": "Você sente um calafrio na espinha... Um fantasma aparece, procurando por vingança!"},
    "carrasco": {"nome": "Carrasco", "vida": 200,"força": 60, "descricao": "Você sente uma presença ameaçadora... Algo metálico se arrastando no chão... Aquele que executa punições está vindo!"}
}

caminhos = ['Você se encontra em um corredor escuro, com paredes úmidas e musgo crescendo sob elas.', 'Você entra em uma sala iluminada por tochas, com um cheiro podre no ar.', 'Você avança em um túnel estreito, onde o som de gotas ecoam ao longe.', 'Você encontra uma pilha de cadaveres abandonados, cobrindo todo o chão.', 'Você encontra monumentos antigos, corredores largos com escritas desgastadas nas paredes, você não entende o que está escrito.', 'Você entra em uma sala de tortura, com instrumentos enferrujados na mesa ao lado, mas ainda sim são assustadores.', 'Você encontra uma biblioteca abandonada, com livros empoeirados e páginas rasgadas espalhadas pelo chão.', 'Você encontra cadáveres pendurados de cabeça para baixo, com seus pescoços cortados, você agora entende da onde vinha o barulho de gotas...']

saida = ['Você vê uma luz brilhante ao longe, diferente de uma tocha, é uma luz natural.', 'Você sente o cheiro de ar fresco, diferente do cheiro de sangue e podridão.', 'Você ouve o som de pássaros cantando ao longe, diferente do som de sangue pingando.', 'Você consegue ver uma abertura mais adiante, se revelando ser a saída.']

def introducao():
    animacao("Você acorda em um lugar escuro, preso em uma cela... Ou pelo menos era o que parecia...")
    pausa_curta()
    animacao("Barulhos ecoam no que parece ser uma masmorra, nenhum sinal de luz ou saída, apenas o som distante de gotas caindo...")
    pausa_curta()
    animacao("Você sente uma presença ameaçadora dentro da masmorra.")
    pausa_longa()
    animacao("...")
    pausa_curta()
    animacao("Você sente que deve sair o quanto antes. Você sai da sua cela e se depara com três caminhos a frente...")

def evento_armadilha():
    animacao(random.choice(armadilha))
    if random.random() < 0.5:
        pausa_longa()
        animacao("Mas você consegue escapar a tempo!")
    else:
        animacao("Você não conseguiu escapar a tempo... Você sofreu dano!")
        armadilhadano = random.randint(5, 15)
        personagemescolhido['vida'] -= armadilhadano
        animacao(f"Vida restante: {personagemescolhido['vida']}")

def evento_inimigo():
    listainimigo = list(inimigos)
    chaveinimigo = random.choice(listainimigo)
    inimigo = inimigos[chaveinimigo]
    animacao(inimigo['descricao'])
    while personagemescolhido['vida'] > 0 and inimigo['vida'] > 0:
        barradestatus = animacao(f"{personagemescolhido['nome']} (Vida: {personagemescolhido['vida']}) vs {inimigo['nome']} (Vida: {inimigo['vida']})")
        acao = input("Você deseja (A) atacar ou (F) fugir? ").lower()
        if acao not in ['a', 'f']:
            animacao("Escolha inválida! Tente novamente.")
            continue
        barradestatus
        acao
        if acao == 'a':
            inimigo['vida'] -= personagemescolhido['força']
            animacao(f"Você ataca o {inimigo['nome']}! Causando {personagemescolhido['força']} de dano.")
            if inimigo['vida'] <= 0:
                animacao(f"Você derrotou o {inimigo['nome']}!")
                break
            elif inimigo['vida'] > 0:
                personagemescolhido['vida'] -= inimigo['força']
                animacao(f"O {inimigo['nome']} contra atacou! Causando {inimigo['força']} de dano.")
                barradestatus
                if verificar_vida() == False:
                    break
            else:
                continue
        elif acao == 'f':
            if random.random() < 0.5:
                animacao("Você conseguiu fugir!")
                break
            else:
                animacao("Você não conseguiu fugir!")
                personagemescolhido['vida'] -= inimigo['força'] + 10
                animacao(f"O {inimigo['nome']} te ataca enquanto você tenta fugir! Causando {inimigo['força'] + 10} de dano.")
                if verificar_vida() == False:
                    break
                else:
                    barradestatus
                    continue

def bossfight():
    animacao("Você sente uma presença muito mais ameaçadora do que as anteriores...")
    pausa_curta()
    animacao(f"De repente, o {inimigos['carrasco']['nome']} aparece diante de você!")
    while personagemescolhido['vida'] > 0 and inimigos['carrasco']['vida'] > 0:
        barradestatus = animacao(f"{personagemescolhido['nome']} (Vida: {personagemescolhido['vida']}) vs {inimigos['carrasco']['nome']} (Vida: {inimigos['carrasco']['vida']})")
        acao = input("Você deseja (A) atacar ou (F) fugir? ").lower()
        if acao not in ['a', 'f']:
            animacao("Escolha inválida! Tente novamente.")
            continue
        barradestatus
        acao
        if acao == 'a':
            inimigos['carrasco']['vida'] -= personagemescolhido['força']
            animacao(f"Você ataca o {inimigos['carrasco']['nome']}! Causando {personagemescolhido['força']} de dano.")
            if inimigos['carrasco']['vida'] <= 0:
                animacao(f"Você derrotou o {inimigos['carrasco']['nome']}!")
                break
            elif inimigos['carrasco']['vida'] > 0:
                personagemescolhido['vida'] -= inimigos['carrasco']['força']
                animacao(f"O {inimigos['carrasco']['nome']} contra atacou! Causando {inimigos['carrasco']['força']} de dano.")
                barradestatus
                if verificar_vida() == False:
                    break
                else:
                    continue
        elif acao == 'f':
            if random.random() < 0.5:
                animacao("Você conseguiu fugir!")
                break
            else:
                animacao("Você não conseguiu fugir!")
                personagemescolhido['vida'] -= inimigos['carrasco']['força'] + 10
                animacao(f"O {inimigos['carrasco']['nome']} te ataca enquanto você tenta fugir! Causando {inimigos['carrasco']['força'] + 10} de dano.")
                if verificar_vida() == False:
                    break
                else:
                    barradestatus
                    continue

def gameplay():
    pausa_curta()
    animacao("Você se depara com três caminhos: esquerda, direita e frente.")
    while True:
        caminho_seguro = random.choice(direcoes)
        escolherdirecao = input("Como deseja prosseguir?: ").lower()
        if escolherdirecao not in direcoes:
            animacao("Escolha inválida!")
            continue
        elif escolherdirecao == caminho_seguro:
            animacao(f"Você escolheu a {escolherdirecao} para prosseguir...")
            break
        else:
            if random.random() < 0.5:
                evento_armadilha()
                break
            else:
                evento_inimigo()
                break

def verificar_vida():
    if personagemescolhido['vida'] <= 0:
        animacao("Você morreu!")
        return False
    else:
        return True

def progressao():
    while personagemescolhido['vida'] > 0:
        if verificar_vida() == False:
            break
        else:
            animacao(random.choice(caminhos))
            gameplay()
            if verificar_vida() == True:
                if random.random() < 0.05:
                    animacao(random.choice(saida))
                    bossfight()
                    if verificar_vida() == True:
                        if inimigos['carrasco']['vida'] <= 0:
                            animacao(f"Ao derrotar o {inimigos['carrasco']['nome']}, você pode avançar para a saída!")
                            pausa_longa()
                            animacao("Você conseguiu escapar da masmorra!")
                            break
                        else:
                            animacao(f"Você fugiu do {inimigos['carrasco']['nome']}... Mas ele ainda está atrás de você!")
                            continue
                    else:
                        continue

''' Início do jogo '''

animacao("Terror & Torment")
pausa_curta()
animacao("Com quem irá começar sua aventura?")

listachave = list(personagem)

while True:
    for numero, chave in enumerate(personagem, 1):
        animacao(f"{numero} - {personagem[chave]['nome']} (Vida: {personagem[chave]['vida']} Força: {personagem[chave]["força"]})")

    escolhernumero = input("Escolha seu personagem: ")
    if escolhernumero not in ['1', '2', '3']:
        animacao("Escolha inválida! Tente novamente.")
        continue
    numeroescolhido = int(escolhernumero)
    chavescolhida = listachave[numeroescolhido - 1]
    personagemescolhido = personagem[chavescolhida]
    
    animacao(f"Você escolheu o {personagemescolhido['nome']}")
    break
while verificar_vida() == True:
    pausa_curta()
    introducao()
    gameplay()
    if verificar_vida() == True:
        animacao("A presença ameaçadora parece estar ficando mais forte...")
    else:
        break
    progressao()
    break