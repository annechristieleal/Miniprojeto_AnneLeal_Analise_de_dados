
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

# Procura valores nulos e reporta a quantidade de valores nulos por coluna.
print("\nValores nulos por coluna:")
print(df.isnull().sum())




# Verificar e reportar ao menos dois problemas básicos: As ultimas 4 colunas estavam totalmente vazias e foram removidas, 
# #N/D  3650 categorias vazias

# Remove colunas que possuem todos os valores vazios 
df = df.dropna(axis=1, how="all")

print("\nColunas após remover as colunas vazias:") 
print(df.columns.tolist())


print("\nQuantidade de colunas:", df.shape[1])
print("\nColunas:")
print(df.columns.tolist())


#Fazer as três etapas de limpeza mínima necessária: remover ou imputar nulos, 
# Ajustar tipos de dados (ex.: converter coluna DATA para datetime).

# tratamento da data utilizando o módulo datetime

df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")

print(df["DATA"].dtype)


# Procura valores nulos e reporta a quantidade de valores nulos por coluna.
print("\nValores nulos por coluna:")
print(df.isnull().sum())


print("\nExemplos da coluna DATA:")
print(df["DATA"].head(20))

print("\nQuantidade de valores vazios em DATA:")
print(df["DATA"].isnull().sum())


print("\nPrimeiros registros sem data:")
print(df[df["DATA"].isna()].head(20))


print("\nDatas válidas:")
print(df["DATA"].notna().sum())

print("\nDatas vazias:")
print(df["DATA"].isna().sum())

print(df[df["DATA"].isna()].head(20))


# Verifica quantas datas diferentes existem dentro de cada compra
datas_por_compra = df.groupby("CO_ID")["DATA"].nunique()

print("\nCompras com mais de uma data diferente:")
print((datas_por_compra > 1).sum())

print("\nCompras com apenas uma data:")
print((datas_por_compra == 1).sum())

print("\nCompras sem nenhuma data:")
print((datas_por_compra == 0).sum())


# Preenche as datas ausentes utilizando a data existente para o mesmo número de compra (CO_ID)

df["DATA"] = df.groupby("CO_ID")["DATA"].transform(
    lambda x: x.ffill().bfill()
)

print("\nValores nulos em DATA após o tratamento:")
print(df["DATA"].isnull().sum())


# Encontra a primeira data válida de cada compra
data_da_compra = df.groupby("CO_ID")["DATA"].transform("first")

# Preenche as datas vazias usando a data da mesma compra
df["DATA"] = df["DATA"].fillna(data_da_compra)

# Verifica quantos valores continuam vazios
print("\nValores nulos em DATA após o tratamento:")
print(df["DATA"].isnull().sum())


print("\nQuantidade de compras sem data:")
print(df.groupby("CO_ID")["DATA"].first().isnull().sum())

print("\nTotal de valores nulos em DATA:")
print(df["DATA"].isnull().sum())


# Quantidade de linhas sem DATA
sem_data = df["DATA"].isnull().sum()

# Quantidade de compras que possuem pelo menos uma DATA
com_data = df.groupby("CO_ID")["DATA"].transform("count")

# Linhas sem DATA, mas cuja compra possui alguma DATA
recuperaveis = ((df["DATA"].isnull()) & (com_data > 0)).sum()

print("Linhas sem DATA:", sem_data)
print("Linhas sem DATA que poderiam ser recuperadas:", recuperaveis)



# Verifica se existem valores nulos em DATA
print("\nValores nulos em DATA:")
print(df["DATA"].isnull().sum())

# Verifica se existem registros sem DATA que poderiam ser recuperados
com_data = df.groupby("CO_ID")["DATA"].transform("count")
recuperaveis = ((df["DATA"].isnull()) & (com_data > 0)).sum()

print("\nRegistros sem DATA que poderiam ser recuperados:")
print(recuperaveis)



#Procura duplicatas
print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())
print(df.duplicated())  


# Mostra algumas linhas que são duplicadas

duplicadas = df[df.duplicated(keep=False)]

print("\nExemplos de linhas duplicadas:")
print(duplicadas.head(20))


print("\nLinhas duplicadas mais frequentes:")
print(
    df.value_counts()
      .loc[lambda x: x > 1]
      .head(10)
)


# Quantidade de linhas duplicadas
print("Total de linhas duplicadas:", df.duplicated().sum())

# Quantidade de compras que possuem linhas duplicadas
compras_com_duplicatas = df[df.duplicated()]["CO_ID"].nunique()

print("Compras envolvidas em duplicatas:", compras_com_duplicatas)



# Verifica se existem categorias vazias 
print("\nPR_CAT:")
print(df["PR_CAT"].value_counts(dropna=False))

if df["PR_CAT"].isnull().sum() > 0:
    df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
    print("Existem categorias vazias.")
else:
    print("Não existem categorias vazias.")

# Transformar #N/D em "Sem Categoria" na coluna PR_CAT
if (df["PR_CAT"] == "#N/D").any():
    df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "Sem Categoria")
    print("Categorias vazias e valores #N/D foram tratados.")
else:
    print("Não existem categorias vazias ou #N/D.")

# Verifica se existem categorias vazias após o tratamento
print("\nPR_CAT:")
print(df["PR_CAT"].value_counts(dropna=False))


if df["PR_CAT"].isnull().sum() > 0:
    df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
else:
    print("Não existem categorias vazias.")
    








