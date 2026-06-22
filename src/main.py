from models.transacao import *
from services.finaceiro import *
from analytics.analise import *


  
def menu():
    print("1 > LISTAR TODAS AS TRANSAÇÕES\n" \
          "2 > LISTAR TRANSAÇÕES POR CATEGORIA\n" \
          "3 > LISTAR TRANSAÇÕES POR TIPO\n" \
          "4 > LISTAR TRANSAÇÕES POR PERÍODO\n" \
          "5 > CONSULTAR SALDO\n" \
          "6 > RESUMO POR CATEGORIA\n" \
          "7 > TOTAL POR TIPO\n" \
          "0 > ENCERRAR")
    

def opcao_1(sistema):
    lista = sistema.listar_transacoes()
    print(f"LISTA DE TRANSAÇÕES: ")
    for transacao in lista:
        print(transacao)


def opcao_2(sistema):
    from database.json_storage import carregar

    transacoes = carregar()
    
    print(f"Categorias dispoíveis:")
   
    categorias_unicas = {transacao["categoria"] for transacao in transacoes}

    mapa = {i: categoria for i, categoria in enumerate(categorias_unicas, 1)}
    for i, categoria in mapa.items():
       print(f"{i} > {categoria}")

    try:
      operador = input("Qual categoria você gostaria de consultar: ")
      operador = int(operador)
      categoria_escolhida = mapa.get(operador)

    except (ValueError, KeyboardInterrupt):
      print("Valor inválido. Navague apenas com números!")
      
    else:
      print(f"CATEGORIA ESCOLHIDA: {categoria_escolhida}")
      
      lista_filtrada = sistema.filtro_por_categoria(categoria_escolhida)
      for transacao in lista_filtrada:
         print(transacao)


def opcao_3(sistema):
    tipos_filtrados = sistema.listar_tipos_unicos()
    
    mapa = {i: tipo for i, tipo in enumerate(tipos_filtrados, 1)}
    for i, tipo in mapa.items():
      print(f"{i} > {tipo}")

    try:
      operador = input("Qual dos tipos quer consultar: ")
      operador = int(operador)
      tipo_escolhido = mapa.get(operador)

    except (ValueError, KeyboardInterrupt):
      print("Valor inválido. Navegue apenas com números!")
      
    else:
      lista_filtrada = sistema.filtrar_por_tipo(tipo_escolhido)
      for transacao in lista_filtrada:
        
        print(
            f"DATA: {transacao['data']} / "
            f"VALOR: {'-' if transacao['tipo'] == 'despesa' else '+'}R${transacao['valor']:.2f} / "
            f"CATEGORIA: {transacao['categoria']} / "
            f"TIPO: {transacao['tipo']}"
        )
  

def opcao_4(sistema):
   inicio = input("Digite a data inicial: ").strip()
   fim = input("Digite a data final: ").strip()
   lista_filtrada = sistema.filtrar_por_periodo(inicio, fim)
   for transacao in lista_filtrada:
      print(transacao) 

def opcao_5(sistema):
    saldo, receita, despesa = sistema.calcular_saldo()
    print(f"RECEITA TOTAL: R${receita:.2f}")
    print(f"DESPESA TOTAL: R${despesa:.2f}")
    print(f"SALDO FINAL: R${saldo:.2f}")


def opcao_6(sistema):
   analise = AnaliseFinanceira(sistema.transacoes)
   resultado = analise.resumo_por_categoria()
   print("\nRESUMO POR CATEGORIA")
   print(resultado)


def opcao_7(sistema):
   analise = AnaliseFinanceira(sistema.transacoes)
   resultado = analise.total_por_tipo()
   print(f"TOTAL POR TIPO: ")
   print(resultado)


def main():
  sistema = SistemaFinanceiro()
  sistema.adicionar_transacao(valor=1000, categoria="salário", tipo="receita", data="2026-01-01")
  sistema.adicionar_transacao(valor=200, categoria="alimentação", tipo="despesa", data="2026-01-02")
  sistema.adicionar_transacao(valor=240, categoria="alimentação", tipo="despesa", data="2026-01-03")
  sistema.adicionar_transacao(valor=370, categoria="alimentação", tipo="despesa", data="2026-01-04")
  sistema.adicionar_transacao(valor=1000, categoria="extra", tipo="receita", data="2026-01-04")
  while True:
      print()
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
            opcao_1(sistema=sistema)
          
          case 2:
            opcao_2(sistema=sistema)

          case 3:
            opcao_3(sistema=sistema)

          case 4:
            opcao_4(sistema=sistema)
          
          case 5:
            opcao_5(sistema=sistema)

          case 6:
            opcao_6(sistema=sistema)
          
          case 7:
            opcao_7(sistema=sistema)
          case 0:
            print()
            print("Encerrando...")
            break
               
                  


main()