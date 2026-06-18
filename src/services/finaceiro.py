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
    lista_formatada = []
    for transacao in self.transacoes:
      lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}"
      lista_formatada.append(lista)
    return lista_formatada

    
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
    lista_por_categoria = []
    from database.json_storage import carregar
    self.transacoes = carregar()
    for transacao in self.transacoes:
      if transacao["categoria"] == categoria:
        lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f}"
        lista_por_categoria.append(lista)
    return lista_por_categoria

    
        


  def total_receitas(self):
    _, receita, _ = self.calcular_saldo()
    lista_por_receita = []
    for transacao in self.transacoes:
      if transacao["tipo"] == "receita":
        lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}"
        lista_por_receita.append(lista)
    return receita, lista_por_receita

  def total_despesas(self):
    _, _, despesa = self.calcular_saldo()
    lista_por_despesas = []
    for transacao in self.transacoes:
      if transacao["tipo"] == "despesa":
        lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}"
        lista_por_despesas.append(lista)
    return despesa, lista_por_despesas

  
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
    def converter_data(d):
      return(d["ano"], d["mes"], d["dia"])
    
    lista_filtrada = []
    for transacao in transacao_por_data:
      if converter_data(inicio) <= converter_data(transacao["data"])<= converter_data(fim):
        lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}"
        lista_filtrada.append(lista)
    return lista_filtrada
    

    """
    SAÍDA:
    {'valor': 1000, 'categoria': 'salário', 'tipo': 'receita', 'data': {'ano': 2026, 'mes': 1, 'dia': 1}}
    {'valor': 200, 'categoria': 'alimentação', 'tipo': 'despesa', 'data': {'ano': 2026, 'mes': 1, 'dia': 2}}
    {'valor': 240, 'categoria': 'alimentação', 'tipo': 'despesa', 'data': {'ano': 2026, 'mes': 1, 'dia': 3}}
    """
      
      
      