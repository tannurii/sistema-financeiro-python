import pandas as pd

class AnaliseFinanceira:
  def __init__(self, transacoes):
    self.df = pd.DataFrame(transacoes)
    self.df["data"] = pd.to_datetime(self.df["data"])
    self.df["mes"] = self.df["data"].dt.month

  def resumo_por_categoria(self):
    return self.df.groupby("categoria")["valor"].sum()
  
  def total_por_tipo(self):
    return self.df.groupby("tipo")["valor"].sum()
  
  def ranking_transacoes(self):
    return self.df.sort_values(by="valor", ascending=False)

  def gastos_por_mes(self):
    df_despesas = self.df[self.df["tipo"] == "despesa"]
    return df_despesas.groupby("mes")["valor"].sum()
  
  def receita_por_mes(self):
    df_receita = self.df[self.df["tipo"] == "receita"]
    return df_receita.groupby("mes")["valor"].sum()

  def receita_e_despesa(self):
    return self.df.pivot_table(
      index= "mes",
      columns="tipo",
      values="valor",
      aggfunc="sum"
    )
  


    
    