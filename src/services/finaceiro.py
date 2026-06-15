class SistemaFinanceiro:
  def __init__(self):
    self.transacoes = []
    self.transacao = {}

  def adicionar_transacao(self, valor, categoria, tipo, data):
    self.transacao = {
      "valor": valor,
        "categoria": categoria,
          "tipo": tipo,
            "data": data
    }
    self.transacoes.append(self.transacao)
    self.transacao.clear

  def listar_transacoes(self):
    for t in self.transacoes:
      print(t)
  
  def calcular_saldo(self):
    saldo = 0
    for t in self.transacoes:
      if t["tipo"] == "receita":
        saldo += t["valor"]
      else:
        saldo -= t["valor"]
    return saldo