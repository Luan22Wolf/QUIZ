import time 
from tqdm import tqdm
import emoji

def sucesso():
    print("\nSucesso\n")

#Usando variável para armazernar as respostas corretas
acertos = 0

print("QUIZ")
print("Quer jogar ? \n (S) \n (N) \n")

opcao = input("Qual a opção escolhida ? ")
escolha = opcao.lower().upper()
#print(escolha)
if escolha != "S":
    quit()

print("INICIANDO")
time.sleep(2)
for i in tqdm(range(100)):
    time.sleep(0.1)

print("Quiz \n")

print("1- Pergunta:\n Qual empresa desenvolveu a franquia GTA \n(A)Microsolft \n(B)Ubisolft\n(C)Rockstar\n(D)EA\n")
resposta1 = input("Qual das altertivas está correta ? ")
resposta_1=resposta1.lower().upper()
if resposta_1 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("2- Pergunta:\n Qual GTA tem um personagem com experiência militar \n(A)GTA VICE CITY \n(B)GTA SAN ANDREAS\n(C)GTA 5\n(D)GTA VICE CITY STORY\n")
resposta2 = input("Qual das altertivas está correta ? ")
resposta_2=resposta2.lower().upper()
if resposta_2 == "D":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("3- Pergunta:\n Em qual jogo da Nintendo o personagem principal é um encanador italiano chamado Mario? \n(A) The Legend of Zelda: Breath of the Wild \n(B) Super Mario Odyssey\n(C) Animal Crossing: New Horizons \n(D) Splatoon 2\n")
resposta3 = input("Qual das alternativas está correta? ")
resposta_3 = resposta3.lower().upper()
if resposta_3 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("4- Pergunta:\n Qual franquia da SEGA é famosa por seu mascote azul, o Sonic the Hedgehog? \n(A) Street Fighter \n(B) Sonic the Hedgehog\n(C) Final Fantasy \n(D) Resident Evil\n")
resposta4 = input("Qual das alternativas está correta? ")
resposta_4 = resposta4.lower().upper()
if resposta_4 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("5- Pergunta:\n Em qual jogo da Ubisoft o jogador pode explorar o antigo Egito como parte da Irmandade dos Assassinos? \n(A) Far Cry 5 \n(B) The Division 2\n(C) Assassin's Creed Origins \n(D) Watch Dogs 2\n")
resposta5 = input("Qual das alternativas está correta? ")
resposta_5 = resposta5.lower().upper()
if resposta_5 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("6- Pergunta:\n Qual jogo da Bethesda se passa em um mundo pós-apocalíptico e permite aos jogadores explorar um vasto terreno devastado? \n(A) Skyrim \n(B) Fallout 4\n(C) DOOM Eternal \n(D) Wolfenstein II: The New Colossus\n")
resposta6 = input("Qual das alternativas está correta? ")
resposta_6 = resposta6.lower().upper()
if resposta_6 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("7- Pergunta:\n Qual jogo da EA é conhecido por sua franquia de simuladores de vida onde os jogadores controlam personagens virtuais? \n(A) Battlefield V \n(B) Apex Legends\n(C) The Sims 4 \n(D) FIFA 21\n")
resposta7 = input("Qual das alternativas está correta? ")
resposta_7 = resposta7.lower().upper()
if resposta_7 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("8- Pergunta:\n Em qual jogo da Nintendo o protagonista, Link, precisa resgatar a Princesa Zelda e derrotar o vilão Ganon? \n(A) Super Mario Galaxy \n(B) The Legend of Zelda: Ocarina of Time\n(C) Metroid Prime \n(D) Donkey Kong Country\n")
resposta8 = input("Qual das alternativas está correta? ")
resposta_8 = resposta8.lower().upper()
if resposta_8 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("9- Pergunta:\n Qual personagem icônico da SEGA é um ouriço azul que corre em velocidades extremas? \n(A) Knuckles \n(B) Tails\n(C) Sonic \n(D) Shadow\n")
resposta9 = input("Qual das alternativas está correta? ")
resposta_9 = resposta9.lower().upper()
if resposta_9 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("10- Pergunta:\n Qual jogo da Ubisoft se passa em uma distopia futurista em Londres, onde os jogadores recrutam membros para resistir a uma tirania tecnológica? \n(A) Assassin's Creed Syndicate \n(B) Far Cry 6\n(C) Watch Dogs: Legion \n(D) Rainbow Six Siege\n")
resposta10 = input("Qual das alternativas está correta? ")
resposta_10 = resposta10.lower().upper()
if resposta_10 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("11- Pergunta:\n Em qual jogo da Bethesda os jogadores enfrentam dragões e exploram uma terra vasta e cheia de perigos chamada Skyrim? \n(A) Fallout 3 \n(B) The Elder Scrolls V: Skyrim\n(C) DOOM (2016) \n(D) Dishonored\n")
resposta11 = input("Qual das alternativas está correta? ")
resposta_11 = resposta11.lower().upper()
if resposta_11 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("12- Pergunta:\n Qual jogo da EA é uma franquia de futebol que é lançada anualmente, apresentando atualizações nas equipes e jogadores? \n(A) Madden NFL \n(B) NBA Live\n(C) FIFA \n(D) NHL\n")
resposta12 = input("Qual das alternativas está correta? ")
resposta_12 = resposta12.lower().upper()
if resposta_12 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("13- Pergunta:\n Em qual jogo da Nintendo os jogadores podem explorar um vasto mundo aberto com criaturas fofas chamadas Pikmin? \n(A) Pikmin 3 \n(B) Super Smash Bros. Ultimate\n(C) Splatoon 2 \n(D) Luigi's Mansion 3\n")
resposta13 = input("Qual das alternativas está correta? ")
resposta_13 = resposta13.lower().upper()
if resposta_13 == "A":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("14- Pergunta:\n Qual jogo da SEGA é um clássico de luta que apresenta personagens como Ryu e Chun-Li? \n(A) Sonic the Hedgehog \n(B) Streets of Rage 4\n(C) Virtua Fighter \n(D) Mortal Kombat 11\n")
resposta14 = input("Qual das alternativas está correta? ")
resposta_14 = resposta14.lower().upper()
if resposta_14 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("15- Pergunta:\n Qual jogo da Ubisoft permite aos jogadores explorar uma versão fictícia do antigo Egito enquanto jogam como um Medjay chamado Bayek? \n(A) Assassin's Creed Unity \n(B) Far Cry 5\n(C) Ghost Recon Breakpoint \n(D) Assassin's Creed Origins\n")
resposta15 = input("Qual das alternativas está correta? ")
resposta_15 = resposta15.lower().upper()
if resposta_15 == "D":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("16- Pergunta:\n Qual jogo da Bethesda é conhecido por seu mundo aberto cheio de dragões, guildas e magia? \n(A) Elder Scrolls Online \n(B) Skyrim\n(C) Fallout: New Vegas \n(D) Prey\n")
resposta16 = input("Qual das alternativas está correta? ")
resposta_16 = resposta16.lower().upper()
if resposta_16 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("17- Pergunta:\n Qual franquia da EA é um jogo de tiro em primeira pessoa que se passa durante a Segunda Guerra Mundial e apresenta modos multijogador intensos? \n(A) Battlefield 1 \n(B) Medal of Honor: Warfighter\n(C) Battlefield V \n(D) Apex Legends\n")
resposta17 = input("Qual das alternativas está correta? ")
resposta_17 = resposta17.lower().upper()
if resposta_17 == "A":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("18- Pergunta:\n Em qual jogo da Nintendo os jogadores podem capturar e treinar criaturas chamadas Pokémon em sua jornada para se tornarem Mestres Pokémon? \n(A) Animal Crossing: New Horizons \n(B) Super Mario 3D World\n(C) Pokémon Sword/Shield \n(D) Splatoon 2\n")
resposta18 = input("Qual das alternativas está correta? ")
resposta_18 = resposta18.lower().upper()
if resposta_18 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("19- Pergunta:\n Qual personagem da SEGA é um ouriço azul que possui uma paixão por velocidade e anéis dourados? \n(A) Sonic \n(B) Knuckles\n(C) Tails \n(D) Shadow\n")
resposta19 = input("Qual das alternativas está correta? ")
resposta_19 = resposta19.lower().upper()
if resposta_19 == "A":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("20- Pergunta:\n Qual jogo da Ubisoft se passa em uma versão futurista de Londres, onde os jogadores podem recrutar e controlar qualquer pessoa na cidade? \n(A) Watch Dogs 2 \n(B) Watch Dogs: Legion\n(C) Far Cry 6 \n(D) The Division 2\n")
resposta20 = input("Qual das alternativas está correta? ")
resposta_20 = resposta20.lower().upper()
if resposta_20 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("21- Pergunta:\n Qual jogo da Bethesda é conhecido por seu ambiente pós-apocalíptico e sua ênfase na construção de abrigos e comunidades? \n(A) Fallout 76 \n(B) The Elder Scrolls IV: Oblivion\n(C) Dishonored \n(D) Prey\n")
resposta21 = input("Qual das alternativas está correta? ")
resposta_21 = resposta21.lower().upper()
if resposta_21 == "A":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("22- Pergunta:\n Qual jogo da EA é conhecido por seu modo de jogo de futebol americano, apresentando times da NFL e modos de carreira emocionantes? \n(A) FIFA \n(B) Madden NFL\n(C) NBA Live \n(D) NHL\n")
resposta22 = input("Qual das alternativas está correta? ")
resposta_22 = resposta22.lower().upper()
if resposta_22 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("23- Pergunta:\n Em qual jogo da Nintendo os jogadores podem explorar uma ilha deserta, coletar insetos e pescar em busca de novas descobertas? \n(A) Animal Crossing: New Horizons \n(B) Super Mario Odyssey\n(C) The Legend of Zelda: Breath of the Wild \n(D) Splatoon 2\n")
resposta23 = input("Qual das alternativas está correta? ")
resposta_23 = resposta23.lower().upper()
if resposta_23 == "A":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("24- Pergunta:\n Qual jogo da SEGA é um título de estratégia em tempo real que envolve a conquista de territórios e o desenvolvimento de civilizações? \n(A) Sonic the Hedgehog \n(B) Total War: Three Kingdoms\n(C) Streets of Rage 4 \n(D) Shenmue III\n")
resposta24 = input("Qual das alternativas está correta? ")
resposta_24 = resposta24.lower().upper()
if resposta_24 == "B":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")

print("25- Pergunta:\n Qual jogo da Ubisoft é um RPG de ação que se passa em um mundo medieval, permitindo aos jogadores explorar, lutar e interagir com personagens históricos? \n(A) Far Cry 5 \n(B) Watch Dogs 2\n(C) Assassin's Creed Valhalla \n(D) The Division 2\n")
resposta25 = input("Qual das alternativas está correta? ")
resposta_25= resposta25.lower().upper()
if resposta_25 == "C":
    print("Sucesso\n")
    acertos += 1
else:
    print("Errou\n")


if acertos >= 10:
    print(emoji.emojize("Você venceu! :sunglasses:\n"))
else:
    print("Você perdeu o jogo!\n")
print(acertos)