import this


def imprimiTutorial():
    print("----------------------------------------------")
    print("------------------TUTORIAL--------------------")
    print("----------------------------------------------")
    print("Irá aparecer suas notas na ordem e você irá colocar \n a nota e apertar enter após colocar a nota no fim irá aparecer seu resultado")
    print("----------------------------------------------")

    
def notas():
    matematica = int(input("Digite sua nota de Matematica: "))
    portugues = int(input("Digite sua nota de Português: "))
    fisica = int(input("Digite sua nota de Fisica: "))
    filosofia = int(input("Digite sua nota de Filosofia: "))
    
    media = (portugues + matematica + filosofia + fisica) / 4

    if media >= 7 and media < 10:
        print("----------------------------------------------")
        print("APROVADO!!!")
    elif media == 10:
        print("----------------------------------------------")
        print("APROVADO COM DISTINÇÃO!!!")
    else:
        print("----------------------------------------------")
        print("REPROVADO!!!")

    return media

    

print("----------------------------------------------")
print()
print("Olá seja bem-vindo ao sistema de notas!")
print()
print("----------------------------------------------")

nome = input("Por Favor Digite Seu Nome: ")
print("----------------------------------------------")
print("Olá " + nome + " Vamos analisar sua situação no nosso sistema")
print("----------------------------------------------")


while(True):
    entrada = input("Gostaria de seguir um tutoria y/n: ").upper()

    if entrada == 'y'.upper():
        print("----------------------------------------------")
        imprimiTutorial()
        break
    elif entrada == 'n'.upper():
        print("----------------------------------------------")
        print("Certinho")
        print("----------------------------------------------")
        break
    else:
        print("Resposta não invalida!!! \n vamos tentar novamente")
        print("----------------------------------------------")


notas()


