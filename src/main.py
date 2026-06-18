from models.transacao import *
from services.finaceiro import *

sistema = SistemaFinanceiro()

# Exemplos
sistema.adicionar_transacao(valor=1000, categoria="salário", tipo="receita", data="2026-01-01")
sistema.adicionar_transacao(valor=200, categoria="alimentação", tipo="despesa", data="2026-01-02")
sistema.adicionar_transacao(valor=240, categoria="alimentação", tipo="despesa", data="2026-01-03")
sistema.adicionar_transacao(valor=370, categoria="alimentação", tipo="despesa", data="2026-01-04")
sistema.adicionar_transacao(valor=1000, categoria="extra", tipo="receita", data="2026-01-04")
"""
#SISTEMA PRINICPAL
lista = sistema.listar_transacoes()
print('LISTA DE TRANSAÇÕES')
for transacao in lista:
  print(transacao)

print()
categoria = "alimentação"
lista_por_categoria = sistema.filtro_por_categoria(categoria)
print(f"LISTA POR CATEGORIA: {categoria}")
for transacao in lista_por_categoria:
  print(transacao)

print()
receita, lista_por_receita = sistema.total_receitas()

print("LISTA DE RECEITAS:")
for transacao in lista_por_receita:
  print(transacao)
print(f"SALDO DE RECEITA: R${receita:.2f}")

print()

despesa, lista_por_despesa = sistema.total_despesas()
print(f"LISTA DE DESPESAS:")
for transacao in lista_por_despesa:
  print(transacao)
print(f"SALDO DE DESPESA: R${despesa:.2f}")

print()

lista_por_data = sistema.filtrar_por_data("2026-01-02", "2026-04-10")
print("LISTA POR PERÍODO: ")
for transacao in lista_por_data:
  print(transacao)

print()
saldo,_,_ = sistema.calcular_saldo()
print(f"SALDO FINAL: R${saldo:.2f}")
"""
#-------------------------------------------
#MENU
while True:
  print("Bem vindo ao seu controle financeiro!")
  print("1-LISTAR TODAS AS TRANSAÇÕES\n" \
  "2-LISTAR TRANSAÇÕES POR CATEGORIA\n" \
  "3-LISTAR TRANSAÇÕES POR TIPO\n" \
  "4-LISTAR TRANSAÇÕES POR PERÍODO\n" \
  "5-CONSULTAR SALDO")
  operador = input("O que gostaria de fazer(navegue por números!): ")
  try:
    operador = int(operador)
  except ValueError:
    print("Valor inválido. Digite apenas número para navegação!")
    continue
  
  else:
    print("Muito bem!")
    