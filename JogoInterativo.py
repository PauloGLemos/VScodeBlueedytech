print()

print( '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
print( '                      ┃        Jogo da Vida        ┃                      ')
print( '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
print( '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

nome = (input("Digite o Nome do seu Personagem? : "))

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 8 or (self.horas == 8 and self.minutos > 0))


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.exercicio = True
        self.comida_thor = True
        self.humor = 100

    def __str__(self):
        return f"{nome} está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome, "+("e deve escolher entre fazer seus exercicios ou não" if self.exercicio else f"{nome} fez seus exercicios") + " e "+("esqueceu" if self.comida_thor else "lembrou")+" de alimentar seu cachorro."+ f"\n o humor de {nome} esta em " + str(self.humor) + "% ."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.exercicio = True


if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    while True:
        print("-=-""-=-""-=-""-=-""-=-""-=-""-=-""-=-""-=-")
        print("São "+str(relogio)+" do Dia "+str(dia) +
              f". {nome} tem que sair pro trabalho até às 08:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Tomar café da manhã")
        print("3 - Fazer exercicios ")
        print("4 - Dar comida para o cachorro")
        print("5 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:") 
        if(opcao == "1"):
            print( '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print( '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
            print( '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
            print( '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
            print( '┃       _|___                _______  _______               _          ┃')
            print( '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
            print( '┃       || ||               |___o___||___o___|          ___| |         ┃')
            print( '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
            print( '┃       || ||                ||   ||  ||   ||           )__(           ┃')
            print( '┃══════════════════════════════════════════════════════════════════════┃')
            print( '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
            print()

            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == '2'): 
            print( '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print( '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
            print( '┃                      ┃    Tomando Café da manhã...┃                  ┃')
            print( '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
            print( '┃                        ;)( ;                                         ┃')
            print( '┃                       :----:     o8Oo./                              ┃')
            print( '┃                      C|====| ._o8o8o8Oo_.                            ┃')
            print( '┃                       |    |  \========/                             ┃')
            print( '┃                       `----‘   ‘------‘                              ┃')
            print( '┃══════════════════════════════════════════════════════════════════════┃')
            print( '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
            print()

            personagem.fome = False
            relogio.avancaTempo(30)
        elif(opcao == '3'):
            print( '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print( '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
            print( '┃                      ┃       Fazendo exercicios...┃                  ┃')
            print( '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
            print( '┃     █━━━━━█                                                          ┃')
            print( '┃      \ ◙ /                                      _/█                  ┃')
            print( '┃       \█/                                         ║                  ┃')
            print( '┃       / \                                         ║                  ┃')
            print( '┃      /   \           █━━━━━█           oo═════════oo                 ┃')
            print( '┃══════════════════════════════════════════════════════════════════════┃')
            print( '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
            print()

            personagem.exercicio = False
            personagem.sujo
            relogio.avancaTempo(60)
        elif(opcao == '4'):
            print( '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print( '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
            print( '┃                      ┃ Dando comida ao Cachorro...┃                   ┃')
            print( '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
            print( '┃                                 __      _                            ┃')
            print( '┃                               ○‘‘)}____//                            ┃')
            print( '┃                                `_/      )                            ┃')
            print( '┃           ║■■■■║   ║■■■■║       (_(_/-(_/                            ┃')
            print( '┃                                                                      ┃')
            print( '┃══════════════════════════════════════════════════════════════════════┃')
            print( '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
            print()

            personagem.comida_thor = False
            relogio.avancaTempo(10)
        elif(opcao == '5'):

            print( '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
            print( '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
            print( '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
            print( '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
            print( '┃                                                               ■■■■■■■┃')
            print( '┃                           ____________                     ╔═════════┃')
            print( '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
            print( '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
            print( '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
            print( '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
            print( '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
            print()

            if personagem.fome == True:
                personagem.humor -= 10
            if personagem.sujo == True:
                personagem.humor -= 10
            if personagem.exercicio == True:
                personagem.humor -= 10
                personagem.sujo == True
            if personagem.comida_thor == True:
                personagem.humor -= 10
            if relogio.atrasado():
                personagem.humor -= 15
            print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("Você foi trabalhar.")
            print(personagem)
            print("-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")

        elif(opcao == "0"):
            print( '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print( '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
            print( '                      ┃      Obrigado Por Jogar    ┃                      ')
            print( '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
            print( '                                                                          ')
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
