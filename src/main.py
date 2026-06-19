from models.transacao import *
from services.finaceiro import *

sistema = SistemaFinanceiro()


def menu():
  print("1 > LISTAR TODAS AS TRANSAÇÕES\n" \
        "2 > LISTAR TRANSAÇÕES POR CATEGORIA\n" \
        "3 > LISTAR TRANSAÇÕES POR TIPO\n" \
        "4 > LISTAR TRANSAÇÕES POR PERÍODO\n" \
        "5 > CONSULTAR SALDO")
  

def opcao_1():
  lista = sistema.listar_transacoes()
  print(f"LISTA DE TRANSAÇÕES: ")
  for transacao in lista:
      print(transacao)


def opcao_2():
  from database.json_storage import carregar

  lista = carregar()
  categorias_unicas = set()
  lista_de_categorias = []
  cont = 0

  print(f"Categorias dispoíveis:")
  for transacao in lista:
    categoria = transacao["categoria"]
    if categoria not in categorias_unicas:
      cont += 1
      print(f"{cont} > {categoria}")
      dict_de_categorias = {cont: categoria}
      lista_de_categorias.append(dict_de_categorias)
      categorias_unicas.add(categoria)

  operador = input("Qual categoria você gostaria de consultar: ")

  try:
    operador = int(operador)
  except ValueError or KeyboardInterrupt:
    print("Valor inválido. Navague apenas com números!")
    pass
  else:
    for categoria in lista_de_categorias:
      for valor, chave in categoria.items():
        if valor == operador:
          lista_filtrada = sistema.filtro_por_categoria(chave)
          titulo_categoria = chave
          break

  print(f"TRANSAÇÕES POR CATEGORIA: {titulo_categoria}")
  for transacoes in lista_filtrada:
    print(transacoes)


def opcao_3():
  tipos_filtrados = sistema.listar_tipos_unicos()
  lista_de_tipos = []
  cont = 0
  for cont, tipo in enumerate(tipos_filtrados, cont):
    cont += 1
    print(f"{cont} > {tipo}")
    dict_tipos = {cont: tipo}
    lista_de_tipos.append(dict_tipos)
  
  operador = input("Qual dos tipos quer consultar: ")

  try:
    operador = int(operador)
  
  except ValueError or KeyboardInterrupt:
    print("Valor inválido. Navegue apenas com números!")
    pass
  else:
    for tipo in lista_de_tipos:
      for valor, chave in tipo.items():
        if operador == valor:
          lista_filtrada = sistema.filtrar_por_tipo(chave)
          for transacao in lista_filtrada:
            print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]} / TIPO: {transacao["tipo"]}")
      
      









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
    menu()
    try:
      operador = input("O que gostaria de fazer(navegue por números!): ")
    except (KeyboardInterrupt, EOFError):
      print('\nInterrupção recebida. Encerrando o programa.')
      break

    try:
      operador = int(operador)
    except ValueError:
      print("Valor inválido. Navegue apenas com números!")
      pass

    match operador:

        case 1:
          opcao_1()
        
        case 2:
          opcao_2()

        case 3:
          opcao_3()
        
               
                  

               

      