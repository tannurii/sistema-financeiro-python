from models.transacao import *
from services.finaceiro import *

sistema = SistemaFinanceiro()

# Exemplos
sistema.adicionar_transacao(valor=1000, categoria="salario", tipo="receita", data="2026-01-01")
sistema.adicionar_transacao(valor=200, categoria="alimentação", tipo="despesa", data="2026-01-02")
sistema.adicionar_transacao(valor=240, categoria="farmácia", tipo="despesa", data="2026-01-03")

sistema.listar_transacoes()

saldo = sistema.calcular_saldo()
print(saldo)