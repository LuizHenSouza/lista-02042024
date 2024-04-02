def cumprimentar_usuario():
    nomeUsuario = str(input("Digite seu nome:"))
    print(f"Olá, {nomeUsuario}! Seja bem-vindo(a)!")

cumprimentar_usuario()

def somar_numeros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print(f"A soma dos números é: {(numero1+numero2)}")

somar_numeros()


def multiplicar_numeros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print(f"O produto dos números é: {(numero1*numero2)}")

multiplicar_numeros()


def divisao_por_dois():
    numero1 = float(input("Digite um número: "))
    print(f"A divisão do número {numero1} por dois é: {(numero1/2)}")

divisao_por_dois()