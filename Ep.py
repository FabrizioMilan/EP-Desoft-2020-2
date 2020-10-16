#Este é o codigo completo criado para rodar o jogo de Bacará
#As 9 primeiras linhas mostram algumas definições de bibliotecas e classes que usamos para aperfeiçoar tanto a performance quanto a estética do código
class cor:
    vermelho="\033[91m"
    azul="\033[94m"
    verde="\033[92m"
    negrito="\033[1m"
    fim="\033[0m"
import random
import time

print(cor.vermelho + "BACARÁ" + cor.fim)
time.sleep (2)
print(cor.vermelho + "ATENÇÃO" + cor.fim )
time.sleep (1)
print(cor.azul + "É recomendado que se leia o arquivo README.md pois nele contém as regras para este jogo. \nDivirta-se :)" + cor.fim)
time.sleep (4)

bacara=True
fichas=100
#Todo o código do jogo está dentro desse while
while bacara:
    print ("Você possui", cor.verde +  "{} fichas.".format (fichas) + cor.fim)
    print ("Para jogar, digite", cor.azul + "J" + cor.fim,"\nPara sair do jogo, digite", cor.vermelho + "S" + cor.fim)
    jogo=str(input("-"))
    #caso o jogador não queira jogar
    if jogo=="S":
        bacara=False
        print ("Obrigado por jogar. Você iniciou o jogo com 100 fichas e saiu dele com {}.".format (fichas))
        time.sleep (2)
        if fichas>100:
            print (cor.verde + "Parabéns! Você lucrou {} fichas.".format(fichas-100) + cor.fim)
        elif fichas<100:
            print (cor.vermelho + "Que pena! Infelizmente, voce perdeu {} fichas. :(".format(100-fichas) + cor.fim)
        elif fichas==100:
            print ("Parece até que não jogou.")
    #O jogo propriamente dito está dentro deste if
    elif jogo=="J":
        print ("Você tem {} fichas.".format (fichas))
        time.sleep (1)
        print("A sua aposta será no Jogador(J), no banco(B) ou em um empate(E)?")
        aposta = str(input("-"))
        
        #a bloquear_aposta foi justamente feita para não haver apostas impossiveis 
        bloquear_aposta = True
        while bloquear_aposta:
            print(cor.azul + "Quantas fichas você aposta?" + cor.fim)
            valor_aposta = int(input("-"))
            if valor_aposta > fichas or valor_aposta < 0:
                print (cor.vermelho + "Aposta inválida.\nVocê possui {} fichas".format (fichas) + cor.fim)
            elif valor_aposta>0:
                fichas=fichas-valor_aposta
                bloquear_aposta=False
                print ("Você agora tem {} fichas.".format (fichas))
            else:
                bloquear_aposta = False

        #Os varios ifs são para acertar as somas das cartas
        carta_banco1=random.randint (0,9)
        carta_banco2=random.randint (0,9)
        carta_jogador1=random.randint (0,9)
        carta_jogador2=random.randint (0,9)
        soma_banco=carta_banco1 + carta_banco2
        soma_jogador=carta_jogador1 + carta_jogador2
        if 9 < soma_jogador < 20 and 9 < soma_banco < 20:
            soma_jogador = soma_jogador - 10
            soma_banco = soma_banco -10
        elif 9 < soma_jogador < 20 and 19 < soma_banco < 28:
            soma_jogador = soma_jogador - 10
            soma_banco = soma_banco - 20
        elif 9 < soma_banco < 20 and 19 < soma_jogador < 28:
            soma_banco = soma_banco - 10
            soma_jogador = soma_jogador - 20
        elif 19 < soma_banco < 28 and 19 < soma_jogador < 28:
            soma_banco = soma_banco - 20
            soma_jogador = soma_jogador - 20
        elif 9 < soma_banco < 20:
            soma_banco = soma_banco - 10
        elif 19 < soma_banco < 28:
            soma_banco = soma_banco - 20
        elif 9 < soma_jogador < 20:
            soma_jogador = soma_jogador - 10
        elif 19 < soma_jogador < 28:
           Jsoma_jogador = soma_jogador - 20
        
    #Os usos constantes do time.sleep são bons para dar um ar de tensão na hora de ver as cartas
        time.sleep (1)
        print (cor.negrito + "Valores das cartas do Banco: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(carta_banco1) + cor.fim)
        time.sleep (1)
        print (cor.verde + "{}".format(carta_banco2) + cor.fim)
        time.sleep (1)
        print (cor.negrito + "Valores das cartas do Jogador: " + cor.fim)
        time.sleep (3)
        print (cor.verde + "{}".format(carta_jogador1) + cor.fim)
        time.sleep (1)
        print (cor.verde + "{}".format(carta_jogador2) + cor.fim)
        time.sleep (1)
        print (cor.vermelho + "Somas" + cor.fim)
        time.sleep (2)
        print ("Soma do banco")
        time.sleep (1)
        print (cor.verde + "{}" .format(soma_banco) + cor.fim)
        time.sleep (2)
        print ("Soma do jogador")
        time.sleep (1)
        print (cor.verde + "{}" .format(soma_jogador) + cor.fim)
        #Abaixo estão os possiveis finais da partida
        if 8 <= soma_jogador <= 9 or 8 <= soma_banco <= 9:
            print ("Fim de jogo!")
            time.sleep (2)
            if soma_jogador > soma_banco:
                print("O jogador venceu")
                time.sleep (2)
                if aposta == "J":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 2
                else:
                    print("Você errou a aposta")
            elif soma_banco > soma_jogador:
                print ("O banco venceu")
                time.sleep (2)
                if aposta == "B":
                    print ("Você acertou a aposta")
                    fichas = fichas + valor_aposta  + valor_aposta*0.95
                    fichas = int(fichas)
                else:
                    print("Você errou a aposta")
            elif soma_jogador == soma_banco:
                print ("o jogo empatou")
                time.sleep (2)
                if aposta == "E":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 8
                else:
                    print("Você errou a aposta")
        
        elif 6 <= soma_jogador <= 7 and 6 <= soma_banco <= 7:
            print ("Fim de jogo!")
            time.sleep (2)
            if soma_jogador > soma_banco:
                print("O jogador venceu")
                time.sleep (2)
                if aposta == "J":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 2
                else:
                    print("Você errou a aposta")
            elif soma_banco > soma_jogador:
                print ("O banco venceu")
                time.sleep (2)
                if aposta == "B":
                    print ("Você acertou a aposta")
                    fichas = fichas + valor_aposta  + valor_aposta*0.95
                    fichas = int(fichas)
                else:
                    print("Você errou a aposta")
            elif soma_jogador == soma_banco:
                print ("o jogo empatou")
                time.sleep (2)
                if aposta == "E":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 8
                else:
                    print("Você errou a aposta")

        elif soma_jogador <= 5 and soma_banco <= 5:
            carta_jogador3 = random.randint (0,9)
            soma_jogador = soma_jogador + carta_jogador3
            carta_banco3 = random.randint (0,9)
            soma_banco = soma_banco + carta_banco3
            if 9 < soma_jogador < 20 and 9 < soma_banco < 20:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco -10
            elif 9 < soma_jogador < 20 and 19 < soma_banco < 28:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco - 20
            elif 9 < soma_banco < 20 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 10
                soma_jogador = soma_jogador - 20
            elif 19 < soma_banco < 28 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 20
                soma_jogador = soma_jogador - 20
            elif 9 < soma_banco < 20:
                soma_banco = soma_banco - 10
            elif 19 < soma_banco < 28:
                soma_banco = soma_banco - 20
            elif 9 < soma_jogador < 20:
                soma_jogador = soma_jogador - 10
            elif 19 < soma_jogador < 28:
                soma_jogador = soma_jogador - 20

            print ("Terceira carta do banco")
            time.sleep (2)
            print (cor.verde + "{}" .format(carta_banco3) + cor.fim)
            time.sleep (1)
            print ("Nova soma do banco")
            time.sleep (2)
            print (cor.verde + "{}" .format(soma_banco) + cor.fim) 
            print ("Terceira carta do jogador")
            time.sleep (2)
            print (cor.verde + "{}" .format(carta_jogador3) + cor.fim)
            time.sleep (1)
            print ("Nova soma do jogador")
            time.sleep (2)
            print (cor.verde + "{}" .format(soma_jogador) + cor.fim) 
            time.sleep (2)
            print ("Fim de jogo!")
            time.sleep (2)
            if soma_jogador > soma_banco:
                print("O jogador venceu")
                time.sleep (2)
                if aposta == "J":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 2
                else:
                    print("Você errou a aposta")
            elif soma_banco > soma_jogador:
                print ("O banco venceu")
                time.sleep (2)
                if aposta == "B":
                    print ("Você acertou a aposta")
                    fichas = fichas + valor_aposta  + valor_aposta*0.95
                    fichas = int(fichas)
                else:
                    print("Você errou a aposta")
            elif soma_jogador == soma_banco:
                print ("o jogo empatou")
                time.sleep (2)
                if aposta == "E":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 8
                else:
                    print("Você errou a aposta")
        
        elif soma_banco <= 5:
            carta_banco3 = random.randint (0,9)
            soma_banco = soma_banco + carta_banco3
            if 9 < soma_jogador < 20 and 9 < soma_banco < 20:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco -10
            elif 9 < soma_jogador < 20 and 19 < soma_banco < 28:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco - 20
            elif 9 < soma_banco < 20 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 10
                soma_jogador = soma_jogador - 20
            elif 19 < soma_banco < 28 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 20
                soma_jogador = soma_jogador - 20
            elif 9 < soma_banco < 20:
                soma_banco = soma_banco - 10
            elif 19 < soma_banco < 28:
                soma_banco = soma_banco - 20
            elif 9 < soma_jogador < 20:
                soma_jogador = soma_jogador - 10
            elif 19 < soma_jogador < 28:
                soma_jogador = soma_jogador - 20

            print ("Terceira carta do banco")
            time.sleep (2)
            print (cor.verde + "{}" .format(carta_banco3) + cor.fim)
            time.sleep (1)
            print ("Nova soma do banco")
            time.sleep (2)
            print (cor.verde + "{}" .format(soma_banco) + cor.fim)
            time.sleep (2)

            print ("Fim de jogo!")
            time.sleep (2)
            if soma_jogador > soma_banco:
                print("O jogador venceu")
                time.sleep (2)
                if aposta == "J":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 2
                else:
                    print("Você errou a aposta")
            elif soma_banco > soma_jogador:
                print ("O banco venceu")
                time.sleep (2)
                if aposta == "B":
                    print ("Você acertou a aposta")
                    fichas = fichas + valor_aposta  + valor_aposta*0.95
                    fichas = int(fichas)
                else:
                    print("Você errou a aposta")
            elif soma_jogador == soma_banco:
                print ("o jogo empatou")
                time.sleep (2)
                if aposta == "E":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 8
                else:
                    print("Você errou a aposta") 
        
        elif soma_jogador <= 5:
            carta_jogador3 = random.randint (0,9)
            soma_jogador = soma_jogador + carta_jogador3
            if 9 < soma_jogador < 20 and 9 < soma_banco < 20:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco -10
            elif 9 < soma_jogador < 20 and 19 < soma_banco < 28:
                soma_jogador = soma_jogador - 10
                soma_banco = soma_banco - 20
            elif 9 < soma_banco < 20 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 10
                soma_jogador = soma_jogador - 20
            elif 19 < soma_banco < 28 and 19 < soma_jogador < 28:
                soma_banco = soma_banco - 20
                soma_jogador = soma_jogador - 20
            elif 9 < soma_banco < 20:
                soma_banco = soma_banco - 10
            elif 19 < soma_banco < 28:
                soma_banco = soma_banco - 20
            elif 9 < soma_jogador < 20:
                soma_jogador = soma_jogador - 10
            elif 19 < soma_jogador < 28:
                soma_jogador = soma_jogador - 20

            print ("Terceira carta do jogador")
            time.sleep (2)
            print (cor.verde + "{}" .format(carta_jogador3) + cor.fim)
            time.sleep (1)
            print ("Nova soma do jogador")
            time.sleep (2)
            print (cor.verde + "{}" .format(soma_jogador) + cor.fim)
            time.sleep (2)

            print ("Fim de jogo!")
            time.sleep (2)
            if soma_jogador > soma_banco:
                print("O jogador venceu")
                time.sleep (2)
                if aposta == "J":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 2
                else:
                    print("Você errou a aposta")
            elif soma_banco > soma_jogador:
                print ("O banco venceu")
                time.sleep (2)
                if aposta == "B":
                    print ("Você acertou a aposta")
                    fichas = fichas + valor_aposta  + valor_aposta*0.95
                    fichas = int(fichas)
                else:
                    print("Você errou a aposta")
            elif soma_jogador == soma_banco:
                print ("o jogo empatou")
                time.sleep (2)
                if aposta == "E":
                    print("Você acertou a aposta")
                    fichas = fichas + valor_aposta * 8
                else:
                    print("Você errou a aposta")

            

        
 
        


















































































