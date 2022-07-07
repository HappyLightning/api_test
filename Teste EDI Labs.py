import requests
import pandas as pd


# Fiz a request
r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/")
print(r.status_code) # Status e abaixo reforcei o 'utf-8'.
r.encoding = 'utf-8'
json = r.json() # Se o decode falhar, uma exceção ocorre. Posso verificar se 'r' é mesmo um JSON.
print(json, '\n')
# Usei o pandas para normalizar o JSON e visualizar melhor o que estou fazendo. Também mudei o nome de duas colunas para usar posteriormente.
norm_json = pd.json_normalize(json).rename(columns= {'regiao.nome':'Regiao', 'nome': 'Qtd. Estados'})
print(norm_json, '\n')
qtd_total = norm_json.groupby(['Regiao']).count()# Agrupei pela região e contei as incidências.
qtd_estados = pd.DataFrame(qtd_total, columns=['Qtd. Estados']) # Para se enquadrar no modelo do CSV.
print(qtd_estados, '\n')
# Criar o CSV
qtd_estados.to_csv("CSV", sep="|")