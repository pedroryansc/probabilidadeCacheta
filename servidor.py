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

def servidor():
    # Configuração do socket do servidor
    host = "localhost"
    porta = 8082
    cargaDados = 2048

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    enderecoServidor = (host, porta)
    servidor.bind(enderecoServidor)
    servidor.listen()

    print(f"Aguardando por jogadores no endereço {host} e porta {porta}...")

    j1, endereco = servidor.accept()
    print("Jogador 1 conectado! Aguardando pelo Jogador 2")

    j2, endereco = servidor.accept()
    print("Jogador 2 conectado!")

    # Criação do baralho com 52 cartas
    baralho = []

    for naipe in range(1, 5):
        for numero in range(1, 14):
            baralho.append([naipe, numero])

    # Início do jogo
    jogoEmAndamento = True

    monte = []
    rodadas = 0

    maoJ1 = [baralho.pop(random.randint(0, len(baralho) - 1)) for _ in range(9)]
    maoJ2 = [baralho.pop(random.randint(0, len(baralho) - 1)) for _ in range(9)]

    maoJ1_codificada = str(maoJ1).encode("utf-8")
    j1.send(maoJ1_codificada)

    maoJ2_codificada = str(maoJ2).encode("utf-8")
    j2.send(maoJ2_codificada)

    print("\n----- Cacheta -----")
    print("Início do jogo!")

    while jogoEmAndamento:
        rodadas += 1

        print("\n------------------------------")

        print(f"\n{rodadas}ª Rodada")

        for i in range(1, 3):
            dadosParaEnviar = [baralho, monte]
            dados_codificados = str(dadosParaEnviar).encode("utf-8")

            if(i == 1): # Vez do Jogador Nº 1
                print("\nVez do Jogador 1...")
                j1.send(dados_codificados)

                dados_codificados = j1.recv(cargaDados)
            else: # Vez do Jogador Nº 2
                print("\nVez do Jogador 2...")
                j2.send(dados_codificados)

                dados_codificados = j2.recv(cargaDados)
            
            print("Jogada feita!")

            dadosRecebidos = eval(dados_codificados.decode("utf-8"))
            baralho = dadosRecebidos[0]
            monte = dadosRecebidos[1]

servidor()