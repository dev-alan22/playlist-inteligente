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
