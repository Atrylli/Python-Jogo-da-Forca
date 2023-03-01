# Desenvolvimento de Game em Linguagem Python 

import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')
        
# Função que desenha a forca na tela
def display_hangman(chances):

    #Lista de estágios da forca
    stages = [ # estágio 6 (final)
                """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / \\
                 -
                """,
                # estágio 5
                """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     / 
                 -
                """,                 
                # estágio 4 
                """
                 --------
                 |      |
                 |      O
                 |     \\|/
                 |      |
                 |     
                 -
                """,
                # estágio 3
                """
                 --------
                 |      |
                 |      O
                 |     \\|
                 |      |
                 |     
                 -
                """,
                # estágio 2
                """
                 --------
                 |      |
                 |      O
                 |      |
                 |      |
                 |     
                 -
                """,                
                # estágio 1
                """
                 --------
                 |      |
                 |      O
                 |     
                 |      
                 |     
                 -
                """,
                # estágio 0
                """
                 --------
                 |      |
                 |     
                 |     
                 |     
                 |     
                 -
                """
    ]
    return stages[chances]
                

# Função Game
def game():

    limpa_tela()
    # Inicio da interface
    print("\n**************Bem vindo(a) ao jogo da forca!**************")
    print("\nEscolha uma das opções abaixo")
    print("1 - Desejo inserir um conjunto de palavras para adivinhar")
    print("2 - Desejo inserir somente uma palavra para forca")
    
    palavras = []
    
    escolha = int(input("\nDigite a opção numérica: "))    
    if escolha == 1:
        while True:
            entrada = input("Digite uma palavra (ou 'sair' para encerrar o conjunto e iniciar o jogo): ").lower()
            if entrada == "sair":
                break
            palavras.append(entrada) 
    else:
        entrada = input("Digite uma palavra para ser adivinhada: ").lower()
        palavras.append(entrada)
    
    limpa_tela()

    # Tela inicial da forca
    print("Adivinhe a palavra abaixo: \n")
    
    palavra = random.choice(palavras)
    
    lista_letras_palavras = [letra for letra in palavra]
    
    tabuleiro = ["_"] * len(palavra)
    
    chances = 6
    
    # Lista para as letras erradas
    letras_tentativas = []
    
    
    while chances > 0:
        
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite um palpite: ").lower() # converte o resultado para letra minúscula
        
        # Caso o usuário digite a palavra inteira
        if tentativa == palavra:
            lista_letras_palavras = tentativa 
            certo = True
            break   
        
        
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        
        # Lista de tentativas
        letras_tentativas.append(tentativa)
        
        # Condicional - digitando letra por letra
        if tentativa in lista_letras_palavras:
            print("Você acertou a letra!")
            # Loop
            for indice in range(len(lista_letras_palavras)):
                #Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
                    certo = True
        
            # Condicional
            if "_" not in tabuleiro:
                certo = True 
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1
    
    if certo == True:
        print("\nVocê venceu, a palavra era: {}".format(palavra))
    
    # Condicional - fora do while
    if "_" in tabuleiro and chances == 0:
        print("\nVocê perdeu, a palavra era: {}".format(palavra))
        
        
# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. você está aprendendo programação em Python com a DSA. :)\n")