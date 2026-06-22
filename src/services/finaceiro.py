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
    

  def filtro_por_categoria(self, categoria_escolhida):
    lista_por_categoria = []
    from database.json_storage import carregar
    self.transacoes = carregar()
    for transacao in self.transacoes:
      if transacao["categoria"] == categoria_escolhida:
        lista = f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f}"
        lista_por_categoria.append(lista)
    return lista_por_categoria

  
  def filtrar_por_tipo(self, tipo_escolhido):
    transacoes = self.transacoes
    return [transacao for transacao in transacoes if transacao["tipo"] == tipo_escolhido]
        
        
  def listar_tipos_unicos(self):
    transacoes = self.transacoes
    return list({transacao["tipo"] for transacao in transacoes})

  
  def filtrar_por_periodo(self, inicio, fim):
    transacoes = self.transacoes
    from datetime import datetime
    
    data_inicial = datetime.strptime(inicio, "%Y-%m-%d")
    data_final = datetime.strptime(fim, "%Y-%m-%d")

    return [
              f"DATA: {transacao['data']} / "
              f"VALOR: {'-' if transacao['tipo'] == 'despesa' else '+'}R${transacao['valor']:.2f} / "
              f"CATEGORIA: {transacao['categoria']} / "
              f"TIPO: {transacao['tipo']}"
          for transacao in transacoes if data_inicial <= datetime.strptime(transacao["data"], "%Y-%m-%d") <= data_final]
  
  
  
  

