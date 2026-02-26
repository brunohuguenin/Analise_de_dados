import pandas as pd

dados = {
  'cargos': ["Assistente", "Analista", "Gerente", "Diretor"],
  'salários': [1000,2000,3000,4000]
}

dados_resultado = pd.DataFrame(dados)
dados_resultado.index = dados_resultado.index+1

print(dados_resultado)