import os
import random

# Lista de palavras possíveis
palavras = ['computador', 'python', 'jogo', 'teclado', 'monitor', 'internet']

# Sorteia uma palavra aleatória
palavra_secreta = random.choice(palavras)

letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa tela no Windows/Linux
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A PALAVRA ERA:', palavra_formada)
        print('Tentativas:', tentativas)
        break
