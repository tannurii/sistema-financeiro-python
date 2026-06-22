import pandas as pd

class AnaliseFinanceira:
  def __init__(self, transacoes):
    self.df = pd.DataFrame(transacoes)
  
  def resumo_por_categoria(self):
    return self.df.groupby("categoria")["valor"].sum()
  
  def total_por_tipo(self):
    return self.df.groupby("tipo")["valor"].sum()