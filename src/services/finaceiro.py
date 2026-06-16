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
    for transacao in self.transacoes:

      print(f"DATA: {transacao["data"]} / VALOR: {"-" if transacao["tipo"] == "despesa" else "+"}R${transacao["valor"]:.2f} / CATEGORIA: {transacao["categoria"]}")

    
  
  def calcular_saldo(self):
    saldo = 0
    for t in self.transacoes:
      if t["tipo"] == "receita":
        saldo += t["valor"]
      else:
        saldo -= t["valor"]
    return saldo
    