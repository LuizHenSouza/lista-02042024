def cumprimenta_usuario():
    nomeUsuario = str(input("Digite seu nome:"))
    print(f"Olá, {nomeUsuario}! Seja bem-vindo(a)!")

cumprimenta_usuario()

def soma_numeros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print(f"A soma dos números é: {(numero1+numero2)}")

soma_numeros()


def multiplica_numeros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    print(f"O produto dos números é: {(numero1*numero2)}")

multiplica_numeros()


def divide_por_dois():
    numero1 = float(input("Digite um número: "))
    print(f"A divisão do número {numero1} por dois é: {(numero1/2)}")

divide_por_dois()

def calcula_IMC():
    altura = float(input("Digite sua altura:"))
    peso = float(input("Digite seu peso:"))
    print(f"O seu IMC é: {(peso/(altura*altura))}")

calcula_IMC()