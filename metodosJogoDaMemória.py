##
# Parametros da partida
##

# Tamanho (da lateral) do tabuleiro. NECESSARIAMENTE PAR E MENOR QUE 10!
dim = 4

# Numero de jogadores
nJogadores = 2

# Numero total de pares de pecas
totalDePares = dim ** 2 / 2

##
# Programa principal
##

# Cria um novo tabuleiro para a partida
tabuleiro = novoTabuleiro(dim)

# Cria um novo placar zerado
placar = novoPlacar(nJogadores)

# Partida continua enquanto ainda ha pares de pecas a
# casar.
paresEncontrados = 0
vez = 0
while paresEncontrados < totalDePares:

    # Requisita primeira peca do proximo jogador
    while True:

        # Imprime status do jogo
        imprimeStatus(tabuleiro, placar, vez)

        # Solicita coordenadas da primeira peca.
        coordenadas = leCoordenada(dim)
        if coordenadas == False:
            continue

        i1, j1 = coordenadas

        # Testa se peca ja esta aberta (ou removida)
        if abrePeca(tabuleiro, i1, j1) == False:
            print "Escolha uma peca ainda fechada!"
            raw_input("Pressione <enter> para continuar...")
            continue

        break

        # Requisita segunda peca do proximo jogador
    while True:

        # Imprime status do jogo
        imprimeStatus(tabuleiro, placar, vez)

        # Solicita coordenadas da segunda peca.
        coordenadas = leCoordenada(dim)
        if coordenadas == False:
            continue

        i2, j2 = coordenadas

        # Testa se peca ja esta aberta (ou removida)
        if abrePeca(tabuleiro, i2, j2) == False:
            print "Escolha uma peca ainda fechada!"
            raw_input("Pressione <enter> para continuar...")
            continue

        break

        # Imprime status do jogo
    imprimeStatus(tabuleiro, placar, vez)

    print "Pecas escolhidas --> ({0}, {1}) e ({2}, {3})\n".format(i1, j1, i2, j2)

    # Pecas escolhidas sao iguais?
    if tabuleiro[i1][j1] == tabuleiro[i2][j2]:

        print "Pecas casam! Ponto para o jogador {0}.".format(vez + 1)

        incrementaPlacar(placar, vez)
        paresEncontrados = paresEncontrados + 1
        removePeca(tabuleiro, i1, j1)
        removePeca(tabuleiro, i2, j2)

        time.sleep(5)
    else:

        print "Pecas nao casam!"

        time.sleep(3)

        fechaPeca(tabuleiro, i1, j1)
        fechaPeca(tabuleiro, i2, j2)
        vez = (vez + 1) % nJogadores

# Verificar o vencedor e imprimir
pontuacaoMaxima = max(placar)
vencedores = []
for i in range(0, nJogadores):

    if placar[i] == pontuacaoMaxima:
        vencedores.append(i)

if len(vencedores) > 1:

    sys.stdout.write("Houve empate entre os jogadores ")
    for i in vencedores:
        sys.stdout.write(str(i + 1) + ' ')

    sys.stdout.write("\n")

else:

    print "Jogador {0} foi o vencedor!".format(vencedores[0] + 1)


