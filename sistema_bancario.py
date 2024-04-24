saldo: int = 0
quantidade_saques: int = 0
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIA = 3
EXTRATO = [] 

def main():

  menu()

def menu():
  print("Bem vindo ao Banco da DIO".center(50, "-"))
  print("Selecione uma opção abaixo:")
  print("1 - Depositar")
  print("2 - Sacar")
  print("3 - Extrato")
  print("4 - Sair")

  escolha = input("Escolha uma opção: ")

  match escolha:

    case "1":
      deposito()

    case "2":
      saque()

    case "3":
      extrato()
    
    case "4":
      print("Obrigado por utilizar o Banco da DIO")
      quit()

    case _:
      print("Opção inválida")
      menu()

def deposito():
  global saldo, EXTRATO
  print("digite o valor do deposito: ")
  valor_deposito = int(input())
  if valor_deposito > 0:
    saldo += valor_deposito
    EXTRATO.append(f"Depósito de R$ {valor_deposito}")
    print("Deposito realizado com sucesso")
  else:
    print("Valor inválido")
  menu()
  
def saque():  # Removido o argumento saldo
  global saldo, quantidade_saques, EXTRATO, LIMITE_SAQUES_DIA
  
  print("digite o valor do saque: ")
  valor_saque = int(input())
  if quantidade_saques < LIMITE_SAQUES_DIA:
    if valor_saque > 0 and valor_saque <= 500 and valor_saque <= saldo:
      quantidade_saques += 1
      saldo -= valor_saque
      EXTRATO.append(f"Saque de R$ {valor_saque}")
      print("Saque realizado com sucesso")
    else:
      print("Valor inválido ou saldo insuficiente")
  else:
    print("Limite de saques diários atingido")
  menu()

def extrato(): # mostrar todas as operações realizadas na conta e no fim mostrar o saldo em conta
  global saldo, EXTRATO
  print("Extrato".center(50, "-"))
  print("Operações realizadas: ")
  for operacao in EXTRATO:
    print(operacao)
  
  menu()

main()