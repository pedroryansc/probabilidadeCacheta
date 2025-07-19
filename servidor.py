import socket, random

def servidor():
    # Configuração do socket do servidor
    host = "localhost"
    porta = 8082

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

    mao = [baralho.pop(random.randint(0, len(baralho) - 1)) for _ in range(9)]
    monte = []
    rodadas = 0

    print("\n----- Cacheta -----")
    print("Início do jogo!")

    while jogoEmAndamento:
        rodadas += 1

        print("------------------------------")

        print(f"\n{rodadas}ª Rodada")

servidor()