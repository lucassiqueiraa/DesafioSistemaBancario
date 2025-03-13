menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: € {valor:.2f}\n"
            print(f" Depósito de € {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de € {limite}.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: € {valor:.2f}\n"
            numero_saques += 1
            print(f" Saque de € {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: € {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por usar nosso banco! Até logo!")
        break

    else:
        print("Operação inválida, tente novamente.")
