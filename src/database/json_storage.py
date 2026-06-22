def salvar(transacoes):
  import json
  with open(r"data\transacoes.json", "w") as f:
    json.dump(transacoes, f, indent=4) 

def carregar():
  import json
  with open(r"data\transacoes.json", "r") as f:
    dados = json.load(f)
  
