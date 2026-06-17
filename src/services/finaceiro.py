class SistemaFinanceiro:
  def __init__(self):
    self.transacoes = []
    self.nova_transacao = {}


  def adicionar_transacao(self, valor, categoria, tipo, data):
    from database.json_storage import salvar, carregar
    self.nova_transacao = {
      "valor": valor,
        "categoria": categoria,
          "tipo": tipo,
            "data": data
    }
    self.transacoes.append(self.nova_transacao)
    salvar(self.transacoes)


  def listar_transacoes(self):
    from database.json_storage import carregar
    self.transacoes = carregar()
    print("LISTA DE TRANSAÇÕES:")
    for transacao in self.transacoes:

      print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}")

    
  def calcular_saldo(self):
    receita = 0
    despesa = 0
    saldo = 0
    for t in self.transacoes:
      if t["tipo"] == "receita":
        saldo += t["valor"]
        receita += t["valor"]
      else:
        saldo -= t["valor"]
        despesa -= t["valor"]
    return saldo, receita, despesa
    

  def filtro_por_categoria(self, categoria):
    print(f"CATEGORIA: {categoria}")
    for transacao in self.transacoes:
      if transacao["categoria"] == categoria:
        print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f}")
        


  def total_receitas(self):
    saldo, receita, despesa = self.calcular_saldo()
    print("TRANSAÇÕES:")
    for transacao in self.transacoes:
      if transacao["tipo"] == "receita":
        print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f}")
    print(f"TOTAL DE RECEITA: R${receita:.2f}")

  def total_despesas(self):
    saldo, receita, despesa = self.calcular_saldo()
    print("TRANSAÇÕES:")
    for transacao in self.transacoes:
      if transacao["tipo"] == "despesa":
        print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f}")
    print(f"TOTAL DE DESPESA: R${despesa:.2f}")

  
  def filtrar_por_data(self, inicio, fim):
    transacao_por_data = []
    
    for transacao in self.transacoes:
      
      data_dict = transacao["data"]
      data_dict = data_dict.split("-")
      data_dict = {
        "ano": int(data_dict[0]),
        "mes": int(data_dict[1]),
        "dia": int(data_dict[2])
      }

      transacao = {
        "valor": transacao["valor"],
        "categoria": transacao["categoria"],
        "tipo": transacao["tipo"],
        "data": data_dict
      }
      transacao_por_data.append(transacao)
    
    
    inicio = inicio.split("-")
    inicio = {
      "ano": int(inicio[0]),
      "mes": int(inicio[1]),
      "dia": int(inicio[2])
    }

    fim = fim.split("-")
   
    fim = {
      "ano": int(fim[0]),
      "mes": int(fim[1]),
      "dia": int(fim[2])
    }
    for transacao in transacao_por_data:
      if transacao["data"]["ano"] == inicio["ano"] and transacao["data"]["mes"] >= inicio["mes"] and transacao["data"]["dia"] >= inicio["dia"] and transacao["data"]["mes"] <= fim["mes"] and transacao["data"]["dia"] <= fim["dia"]:
        print(transacao)
  

    """
    SAÍDA:
    {'valor': 1000, 'categoria': 'salário', 'tipo': 'receita', 'data': {'ano': 2026, 'mes': 1, 'dia': 1}}
    {'valor': 200, 'categoria': 'alimentação', 'tipo': 'despesa', 'data': {'ano': 2026, 'mes': 1, 'dia': 2}}
    {'valor': 240, 'categoria': 'alimentação', 'tipo': 'despesa', 'data': {'ano': 2026, 'mes': 1, 'dia': 3}}
    """
      
      
      