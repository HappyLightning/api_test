import requests
import pandas as pd


# Fiz a request
r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/")
print(r.status_code)  # Status e abaixo reforcei o 'utf-8'.
r.encoding = 'utf-8'
json = r.json()  # Se o decode falhar, uma exceção ocorre. Posso verificar se 'r' é mesmo um JSON.
print(json, '\n')

# Usei o pandas para normalizar o JSON e visualizar melhor o que estou fazendo.
norm_json = pd.json_normalize(json)
print(norm_json, '\n')

# Agrupei pela região e contei as incidências. Usei 'as_index= False' para não "perder" a coluna 'regiao.nome'.
qtd_total = norm_json.groupby(['regiao.nome'], as_index=False).count()
print(qtd_total)

# Criei um DF vazio com as colunas nomeadas.
qtd_estados = pd.DataFrame(columns=['Regiao', 'Qtd. Estados'])

# Passei os valores para essas colunas criadas.
qtd_estados['Regiao'] = qtd_total['regiao.nome']
qtd_estados['Qtd. Estados'] = qtd_total['regiao.sigla']
print(qtd_estados, '\n')

# Por último, criar o 'estados.csv'. Usei 'index=False' pois o 'qtd_estados' possuí índice.
qtd_estados.to_csv("CSV/estados.csv", index=False, sep="|")
