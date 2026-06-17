from models.transacao import *
from services.finaceiro import *

sistema = SistemaFinanceiro()

# Exemplos
sistema.adicionar_transacao(valor=1000, categoria="salário", tipo="receita", data="2026-01-01")
sistema.adicionar_transacao(valor=200, categoria="alimentação", tipo="despesa", data="2026-01-02")
sistema.adicionar_transacao(valor=240, categoria="alimentação", tipo="despesa", data="2026-01-03")

#sistema.listar_transacoes()

"""
print()
sistema.filtro_por_categoria("alimentação")
print()
sistema.total_receitas()
print()
sistema.total_despesas()
print()
saldo,_,_ = sistema.calcular_saldo()
print(f"SALDO TOTAL: R${saldo:.2f}")
"""
sistema.filtrar_por_data(inicio="2026-01-02", fim="2026-05-10")