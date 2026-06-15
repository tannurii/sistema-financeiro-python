class Transacao:
  def __init__(self, valor, categoria, tipo, data):
    self.valor = valor
    self.categoria = categoria
    self.tipo = tipo #receita ou despesa
    self.data = data

  def __repr__(self):
    return f"{self.tipo.upper()} | {self.categoria} | R${self.valor} | {self.data}"
  
