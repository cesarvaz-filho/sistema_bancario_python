menu = """
    ############ MENU ############
    Digite uma opção

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] = Sair
==>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não tem saldo suficiente")
        elif excedeu_limite:
            print("Você excedeu o limite")
        elif excedeu_saldo:
            print("Número máximo de saques excedidos")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Valor informado inválido")
    elif opcao == "e":
        print("\n###########Extrato###########")
        print("Não foram realizadas movimentações" if not extrato else extrato) 
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida. por favor selecione novamente")
