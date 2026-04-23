playlist = []

def adicionar_musica(nome, artista, duracao):
    musica = {
        "nome": nome,
        "artista": artista,
        "duracao": duracao
    }
    playlist.append(musica)

def listar_playlist():
    for musica in playlist:
        print(f'{musica["nome"]} - {musica["artista"]} ({musica["duracao"]}s)')

def calcular_duracao_total():
    total = 0
    for musica in playlist:
        total += musica["duracao"]
    return total

def musica_mais_longa():
    maior = playlist[0]
    for musica in playlist:
        if musica["duracao"] > maior["duracao"]:
            maior = musica
    return maior


# Testando
adicionar_musica("Song A", "Artista 1", 180)
adicionar_musica("Song B", "Artista 2", 240)
adicionar_musica("Song C", "Artista 3", 150)

print("Playlist:")
listar_playlist()

print("Duração total:", calcular_duracao_total())
print("Mais longa:", musica_mais_longa())

playlist = []
fila_acoes = []
historico = []
fila_acoes.append ("Adicionar música A")
acao = fila_acoes.pop(0)  # pega a primeira da fila (FIFO)
acao = fila_acoes.pop(0)  # pega a primeira da fila (FIFO)
playlist.append("Música A")
historico.append("Adicionar música A")
playlist.remove("Música A")

playlist = []
fila_acoes = []
historico = []

import json

def salvar_dados ():
    with open ("playlist.json", "w") as arquivos:
        json.dump(playlist, arquivos)

def carregar_dados():
    global playlist
    try:
        with open("playlist.json", "r") as arquivo:
            playlist = json.load(arquivo)
    except:
        playlist = []

def registrar_acao(acao):
    fila_acoes.append(acao)
    historico.append(acao)

def processar_acao():
    if fila_acoes:
        acao = fila_acoes.pop(0)
        if acao.startswith("Adicionar música"):
            musica = acao.replace("Adicionar música ", "")
            playlist.append(musica)
        elif acao.startswith("Remover música"):
            musica = acao.replace("Remover música ", "")
            if musica in playlist:
                playlist.remove(musica)
        print(f"Ação processada: {acao}")


def executar_fluxo():
    carregar_dados()
    registrar_acao("Adicionar música A")
    processar_acao()
    salvar_dados()

