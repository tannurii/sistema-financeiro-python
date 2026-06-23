from models.transacao import *
from services.finaceiro import *
from analytics.analise import *


  
def menu():
    print(" 1 > LISTAR TODAS AS TRANSAÇÕES\n" \
          " 2 > LISTAR TRANSAÇÕES POR CATEGORIA\n" \
          " 3 > LISTAR TRANSAÇÕES POR TIPO\n" \
          " 4 > LISTAR TRANSAÇÕES POR PERÍODO\n" \
          " 5 > CONSULTAR SALDO\n" \
          " 6 > RESUMO POR CATEGORIA\n" \
          " 7 > TOTAL POR TIPO\n" \
          " 8 > RANKING DE TRANSAÇÕES\n" \
          " 9 > GASTOS POR MÊS\n" \
          "10 > RECEITA POR MÊS\n" \
          "11 > RECEITA E DESPESA\n" \
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
   
   inicio = input("Digite a data inicial(utilize o formato YYYY-MMM-DD): ").strip()
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


def opcao_8(sistema):
  analise = AnaliseFinanceira(sistema.transacoes)
  resultado =  analise.ranking_transacoes()
  print(f"RANKING: ")
  print(resultado)


def opcao_9(sistema):
   analise = AnaliseFinanceira(sistema.transacoes)
   resultado = analise.gastos_por_mes()
   print("GASTOS POR MÊS: ")
   print(resultado)


def opcao_10(sistema):
   analise = AnaliseFinanceira(sistema.transacoes)
   resultado = analise.receita_por_mes()
   print("RECEITA POR MÊS:")
   print(resultado)
  

def opcao_11(sistema):
   analise = AnaliseFinanceira(sistema.transacoes)
   resultado = analise.receita_e_despesa()
   print("COMPARAÇÃO RECEITA E DESPESA: ")
   print(resultado)


def main():
  sistema = SistemaFinanceiro()
  transacoes_fake = [
    # Janeiro
    {"valor": 1200, "categoria": "salário", "tipo": "receita", "data": "2026-01-05"},
    {"valor": 300, "categoria": "alimentação", "tipo": "despesa", "data": "2026-01-10"},
    {"valor": 150, "categoria": "transporte", "tipo": "despesa", "data": "2026-01-15"},

    # Fevereiro
    {"valor": 2000, "categoria": "freelance", "tipo": "receita", "data": "2026-02-03"},
    {"valor": 400, "categoria": "alimentação", "tipo": "despesa", "data": "2026-02-08"},
    {"valor": 220, "categoria": "lazer", "tipo": "despesa", "data": "2026-02-12"},

    # Março
    {"valor": 1800, "categoria": "salário", "tipo": "receita", "data": "2026-03-01"},
    {"valor": 500, "categoria": "moradia", "tipo": "despesa", "data": "2026-03-05"},
    {"valor": 320, "categoria": "alimentação", "tipo": "despesa", "data": "2026-03-10"},

    # Abril
    {"valor": 2100, "categoria": "salário", "tipo": "receita", "data": "2026-04-01"},
    {"valor": 450, "categoria": "alimentação", "tipo": "despesa", "data": "2026-04-12"},
    {"valor": 350, "categoria": "lazer", "tipo": "despesa", "data": "2026-04-07"},

    # Maio
    {"valor": 800, "categoria": "freelance", "tipo": "receita", "data": "2026-05-03"},
    {"valor": 600, "categoria": "moradia", "tipo": "despesa", "data": "2026-05-06"},
    {"valor": 200, "categoria": "lazer", "tipo": "despesa", "data": "2026-05-10"},

    # Junho
    {"valor": 3000, "categoria": "salário", "tipo": "receita", "data": "2026-06-01"},
    {"valor": 500, "categoria": "alimentação", "tipo": "despesa", "data": "2026-06-05"},
    {"valor": 700, "categoria": "investimento", "tipo": "receita", "data": "2026-06-08"},

    # Julho
    {"valor": 2500, "categoria": "salário", "tipo": "receita", "data": "2026-07-01"},
    {"valor": 480, "categoria": "alimentação", "tipo": "despesa", "data": "2026-07-06"},
    {"valor": 300, "categoria": "transporte", "tipo": "despesa", "data": "2026-07-09"},

    # Agosto
    {"valor": 1200, "categoria": "freelance", "tipo": "receita", "data": "2026-08-02"},
    {"valor": 650, "categoria": "moradia", "tipo": "despesa", "data": "2026-08-05"},
    {"valor": 350, "categoria": "lazer", "tipo": "despesa", "data": "2026-08-11"},

    # Setembro
    {"valor": 2800, "categoria": "salário", "tipo": "receita", "data": "2026-09-01"},
    {"valor": 520, "categoria": "alimentação", "tipo": "despesa", "data": "2026-09-04"},
    {"valor": 270, "categoria": "transporte", "tipo": "despesa", "data": "2026-09-09"},

    # Outubro
    {"valor": 1400, "categoria": "freelance", "tipo": "receita", "data": "2026-10-03"},
    {"valor": 700, "categoria": "moradia", "tipo": "despesa", "data": "2026-10-06"},
    {"valor": 330, "categoria": "lazer", "tipo": "despesa", "data": "2026-10-10"},

    # Novembro
    {"valor": 3100, "categoria": "salário", "tipo": "receita", "data": "2026-11-01"},
    {"valor": 550, "categoria": "alimentação", "tipo": "despesa", "data": "2026-11-05"},
    {"valor": 400, "categoria": "extra", "tipo": "receita", "data": "2026-11-10"},

    # Dezembro
    {"valor": 3500, "categoria": "salário", "tipo": "receita", "data": "2026-12-01"},
    {"valor": 800, "categoria": "presentes", "tipo": "despesa", "data": "2026-12-20"},
    {"valor": 600, "categoria": "lazer", "tipo": "despesa", "data": "2026-12-25"},
]
  
  for transacao in transacoes_fake:
     sistema.adicionar_transacao(
        valor=transacao["valor"],
          categoria=transacao["categoria"],
              tipo=transacao["tipo"],
                  data=transacao["data"]
                                  )

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

          case 8:
            opcao_8(sistema=sistema)

          case 9:
            opcao_9(sistema=sistema)

          case 10:
            opcao_10(sistema=sistema)
          
          case 11:
            opcao_11(sistema=sistema)

         
          case 0:
            print()
            print("Encerrando...")
            break
               
                  


main()