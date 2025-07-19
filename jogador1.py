import socket, random

def formatacaoCarta(carta):
  naipe = carta[0]
  numero = carta[1]

  if(naipe == 1):
    naipe = "♣"
  elif(naipe == 2):
    naipe = "♦"
  elif(naipe == 3):
    naipe = "♥"
  else:
    naipe = "♠"

  if(numero == 1):
    numero = "Ás"
  elif(numero == 11):
    numero = "J"
  elif(numero == 12):
    numero = "Q"
  elif(numero == 13):
    numero = "K"

  return [naipe, numero]

def mostrarMao(mao):
  print("\nMão: ", end="")

  for i in range(len(mao)):
    carta = formatacaoCarta(mao[i])

    print(f"[{carta[0]}, {carta[1]}] ", end="")
  
  print()

def jogador1():
    # Criação do baralho com 52 cartas
    baralho = []

    for naipe in range(1, 5):
        for numero in range(1, 14):
            baralho.append([naipe, numero])

    # Início do jogo
    jogoEmAndamento = True

    mao = [baralho.pop(random.randint(0, len(baralho) - 1)) for _ in range(9)]
    monte = []
    rodadas = 0

    print("\n----- Cacheta -----")
    print("Início do jogo!")

    while jogoEmAndamento:
        rodadas += 1

        print("------------------------------")

        print(f"\n{rodadas}ª Rodada")

        if(monte):
            carta = formatacaoCarta(monte[-1])
            print(f"\nTopo do monte: [{carta[0]}, {carta[1]}]")

        # Comprar carta ou pegar do monte
        print("\nComprar Carta (1)", end="")
        if(monte):
            print(" | Pegar do Monte (2)")
        else:
            print()

        mostrarMao(mao)

        opcao = int(input("\nOpção: "))

        if(opcao == 1):
            posicaoCarta = random.randint(0, len(baralho) - 1)
            novaCarta = baralho.pop(posicaoCarta)
            mensagem = "Carta comprada"
        elif(monte):
            novaCarta = monte.pop()
            mensagem = "Carta pega do monte"

        mao.append(novaCarta)

        carta = formatacaoCarta(novaCarta)
        print(f"\n{mensagem}: [{carta[0]}, {carta[1]}]") 

        # Jogar carta
        mostrarMao(mao)
        print("       ", end="")
        for i in range(1, 11):
            print(f"({i})    ", end="")

        posicao = int(input("\n\nCarta para ser jogada: ")) - 1
        cartaJogada = mao.pop(posicao)

        monte.append(cartaJogada)

        carta = formatacaoCarta(cartaJogada)
        print(f"\nCarta jogada: [{carta[0]}, {carta[1]}]")

jogador1()