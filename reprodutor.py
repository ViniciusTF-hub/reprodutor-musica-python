import pygame
import os
playlist = ['What I_ve Done Linkin Park.MP3', 'Gabriel Guedes- Santo pra Sempre.MP3', 'Isaias Saad-Ousado Amor.MP3']
posicao_atual = 0
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def tocarmusica():
    try:
        print(f'Reproduzindo... {playlist[posicao_atual]}')
        pygame.mixer.music.load(playlist[posicao_atual])
        pygame.mixer.music.play()
    except pygame.error:
        print('Erro: arquivo de música não encontrado.')
def pausar():
    pygame.mixer.music.pause()
    print('Pausado')
def despausar():
    pygame.mixer.music.unpause()
    print('Despausado')
def volume():
    try:
        valor= float(input('Digite o volume (0 a 1.0): '))
        if valor >= 0.0 and valor <= 1.0:
            pygame.mixer.music.set_volume(valor)
            print(f'Volume ajustado para {valor}')
        else:
            print('Valor fora do intervalo')
    except ValueError:
        print('Entrada Invalida')
def sair():
    pygame.mixer.music.stop()
    print('Saindo')
def proxima():
    global posicao_atual
    if posicao_atual < len(playlist) - 1:
        posicao_atual= posicao_atual + 1
    else:
        posicao_atual = 0
    tocarmusica()
def anterior():
    global posicao_atual
    if posicao_atual > 0:
        posicao_atual= posicao_atual - 1
    else:
        posicao_atual = len(playlist) - 1
    tocarmusica()
def menu():
    alternativa= input('''
==============================
 🎵 Reprodutor de Música 🎵
==============================

1- Tocar
2- Pausar
3- Despausar
4- Volume
5- Proxima
6- Anterior
7- Sair
''').lower()
    return alternativa

pygame.init()
pygame.mixer.init()


while True:
    limpar_tela()
    alternativa = menu()  
    if alternativa == '1' or alternativa == 'tocar':
        if not pygame.mixer.music.get_busy():
            tocarmusica()
        else:
            print('A música já está tocando.')
    elif alternativa == '2' or alternativa == 'pausar':
        pausar()
    elif alternativa == '3' or alternativa == 'despausar':
        despausar()
    elif alternativa == '4' or alternativa == 'volume':
        volume()
    elif alternativa == '5' or alternativa == 'proxima':
        proxima()
    elif alternativa == '6' or alternativa == 'anterior':
        anterior()
    elif alternativa == '7' or alternativa == 'sair':
        sair()
        break
    else:
     print('Opção invalida')
    input("\nPressione Enter para continuar...")
