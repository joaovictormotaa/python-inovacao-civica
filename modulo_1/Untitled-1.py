import pandas as pd
import glob

lista_arquivos = glob.glob('modulo_1\conjunto_dados/*.csv')
#print(lista_arquivos)

lista_df = []

for csv in lista_arquivos:
    df = pd.read_csv(csv, sep=';', encoding='latin_1')
    lista_df.append(df)

#print(lista_df)

candidaturas_PE_RN = pd.concat(lista_df, axis=0, ignore_index=True)

