def adicionar_transacao(valor, categoria, tipo, data):
    transacoes = []
    transacao = {
      "valor": valor,
        "categoria": categoria,
          "tipo": tipo,
            "data": data
    }
    transacoes.append(transacao)
    transacao.clear
    return transacoes
transacoes = adicionar_transacao(valor=1000, categoria="salário", tipo="receita", data="2026-01-01")
print(transacoes)