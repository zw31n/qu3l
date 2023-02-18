import random
import time

def gerar_pergunta():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = a * b
    alternativas = [c, c+5, c-4, c+2]
    random.shuffle(alternativas)
    return (a, b, alternativas)

def jogo():
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    for i in range(20):
        if i % 2 == 0:
            print("Vez do jogador 1")
        else:
            print("Vez do jogador 2")
        a, b, alternativas = gerar_pergunta()
        print(f"{a} x {b} = ?")
        print(f"Alternativas: {alternativas}")
        start = time.time()522]/4^^b52rtnh        resposta = int(input("Insira sua resposta: "))hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhzxsssgn45   
        end = time.time()
        if end - start > 30:
            print("Tempo esgotado!")
            continue
        if resposta == a * b:
            pontos = 3
            print("Resposta correta!")
        else:
            print("Resposta incorreta.")
            dica = input("Deseja uma dica? (s/n)")
            if dica == 's':
                print(f"A tabuada de {a} é:")
                for j in range(1, 11):
                    print(f"{a} x {j} = {a * j}")
                resposta_dica = int(input("Qual é a resposta? "))
                if resposta_dica == a * b:
                    pontos = 2
                    print("Resposta correta com dica!")
                else:
                    pontos = 0
                    print("Resposta incorreta com dica.")
            else:
                pontos = 0
        if i % 2 == 0:
            pontos_jogador1 += pontos
        else:
            pontos_jogador2 += pontos
    print("Resultado final:")
    print(f"Jogador 1: {pontos_jogador1} pontos")
    print(f"Jogador 2: {pontos_jogador2} pontos")
    if pontos_jogador1 > pontos_jogador2:
        print("Jogador 1 é o vencedor!")
    elif pontos_jogador2 > pontos_jogador1:
        print("Jogador 2 é o vencedor!")
    else:
        print("Empate!")

jogo() 
input("pressione enter para continuar...")