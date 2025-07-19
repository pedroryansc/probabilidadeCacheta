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

def jogador():
  # Configuração do socket do jogador
  hostDestino = "localhost"
  porta = 8082
  cargaDados = 2048

  jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  enderecoServidor = (hostDestino, porta)

  jogador.connect(enderecoServidor)
  print("Jogador conectado ao servidor!")

  mao_codificada = jogador.recv(cargaDados)
  mao = eval(mao_codificada.decode("utf-8"))

  # Início do jogo
  jogoEmAndamento = True

  rodadas = 0

  print("\n----- Cacheta -----")
  print("Início do jogo!")

  while jogoEmAndamento:
      # Recebimento do baralho e do monte atual
      dados_codificados = jogador.recv(cargaDados)
      dadosRecebidos = eval(dados_codificados.decode("utf-8"))

      baralho = dadosRecebidos[0]
      monte = dadosRecebidos[1]

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

      # Jogar carta no monte
      mostrarMao(mao)
      print("       ", end="")
      for i in range(1, 11):
          print(f"({i})    ", end="")

      posicao = int(input("\n\nCarta para ser jogada: ")) - 1
      cartaJogada = mao.pop(posicao)

      monte.append(cartaJogada)

      carta = formatacaoCarta(cartaJogada)
      print(f"\nCarta jogada: [{carta[0]}, {carta[1]}]")

      # Envio do baralho e do monte atual para o servidor
      dadosParaEnviar = [baralho, monte]
      dados_codificados = str(dadosParaEnviar).encode("utf-8")

      jogador.send(dados_codificados)
      print("\nÉ a vez do outro jogador...")

jogador()