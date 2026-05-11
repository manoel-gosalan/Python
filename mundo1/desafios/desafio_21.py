# * ============================================================
# * DESAFIO 21 — Tocando um MP3
# * MP3を再生する (MP3 wo sasei suru)
# * Curso em Vídeo | Gustavo Guanabara | Mundo 1
# * ============================================================

# ? ─────────────────────────────────────────────────────────────
# ? Faça um programa que tenha uma lista com pelo menos
# ? 5 músicas no formato:
# ?   ["musica1.mp3", "musica2.mp3", ...]
# ?
# ? O programa deve:
# ?   → Embaralhar aleatoriamente a ordem das músicas
# ?   → Mostrar a ordem em que elas serão tocadas
# ?   → Exibir qual música vai tocar PRIMEIRO
# ?
# ? ! Você não precisa tocar o MP3 de verdade —
# ? ! só simule a ordem e mostre qual seria a primeira.
# ? ! (tocar áudio real precisaria de biblioteca externa)
# ?
# ? Dica: combine random.shuffle() com indexação da lista
# ? ヒント: shuffle() してから lista[0] で最初の曲を取れます！
# ? ─────────────────────────────────────────────────────────────
import pyglet
from pathlib import Path
import random
import time

separador = "─" * 40

playlist = [
Path (__file__).parent / "music" / "auracosmica.mp3",
Path (__file__).parent / "music" / "crystallize.mp3",
Path (__file__).parent / "music" / "roundtable-rival.mp3",
Path (__file__).parent / "music" / "slide.mp3"
]

aleatorio = playlist.copy()

random.shuffle(aleatorio)

print(f"\n{separador}")
print("Playlist original:")
print(separador)
print(f"  1. {playlist[0].name}")
print(f"  2. {playlist[1].name}")
print(f"  3. {playlist[2].name}")
print(f"  4. {playlist[3].name}")

print(f"\n{separador}")
print("Playlist embaralhada:")
print(separador)
print(f"  1. {aleatorio[0].name}")
print(f"  2. {aleatorio[1].name}")
print(f"  3. {aleatorio[2].name}")
print(f"  4. {aleatorio[3].name}")

print(f"\n{separador}")
print(f"Tocando agora: {aleatorio[0].name}")
print(separador)

musica = pyglet.media.load(str(aleatorio[0]))
musica.play()
time.sleep(musica.duration)

# * がんばって！🎌
