
# Carregar a base_varejo.csv com pandas e mostrar: número de registros,colunas e tipos de dados.


import pandas as pd
from IPython.display import display

df = pd.read_csv("base_varejo.csv", sep=";")
print("Quantidade de registros:")
print(df.shape[0])
print("\nQuantidade de colunas:")
print(df.shape[1])
print("\nColunas:")
print(df.columns.tolist())
print("\nTipos de dados:")
print(df.dtypes)




display(df.head())
display(df.shape)
display(type(df))



# Verificar e reportar ao menos dois problemas básicos: As ultimas 4 colunas estavam totalmente vazias e foram removidas 

# Remove colunas que possuem todos os valores vazios 
df = df.dropna(axis=1, how="all")

print("\nColunas após remover as colunas vazias:") 
print(df.columns.tolist())


print("\nQuantidade de colunas:", df.shape[1])
print("\nColunas:")
print(df.columns.tolist())






