                    # Quiz Game #

Este é um jogo de perguntas e respostas (quiz) desenvolvido em Python. O jogo apresenta uma série de perguntas sobre jogos de vídeo, onde o jogador deve escolher a resposta correta entre quatro alternativas. O objetivo é acertar o maior número de perguntas possível.


# Funcionalidades
-Perguntas e Respostas: O jogo contém 25 perguntas sobre diferentes jogos e franquias.

-Contagem de Acertos: O número de respostas corretas é armazenado e exibido ao final do jogo.

-Feedback Imediato: Após cada resposta, o jogador é informado se acertou ou errou.

-Animação de Progresso: Utiliza a biblioteca tqdm para mostrar uma barra de progresso durante a inicialização do jogo.

- Emojis: Utiliza a biblioteca emoji para exibir emojis no final do jogo, dependendo do desempenho do jogador.


# Como Jogar
-Execute o script Python.

-Responda “S” para iniciar o jogo.
Responda a cada pergunta digitando a letra correspondente à alternativa correta.

-Ao final do jogo, o número total de acertos será exibido, juntamente com uma mensagem de vitória ou derrota.

#Bibliotecas Utilizadas
-time: Para adicionar pausas no jogo.

-tqdm: Para exibir uma barra de progresso.

-emoji: Para exibir emojis no final do jogo.

                  # Exemplo de Uso #

                        Python
-------------------------------------------------------
import time 
from tqdm import tqdm
import emoji

def sucesso():
    print("\nSucesso\n")

acertos = 0

print("QUIZ")
print("Quer jogar? \n (S) \n (N) \n")

opcao = input("Qual a opção escolhida? ")
escolha = opcao.lower().upper()
if escolha != "S":
    quit()

print("INICIANDO")
time.sleep(2)
for i in tqdm(range(100)):
    time.sleep(0.1)

print("Quiz \n")

if acertos >= 10:
    print(emoji.emojize("Você venceu! :sunglasses:\n"))
else:
    print("Você perdeu o jogo!\n")
print(acertos)
-------------------------------------------------------

# Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades para o jogo. Basta abrir um pull request com suas alterações.