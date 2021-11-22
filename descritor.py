__version__ = '0.0.1'
import pandas as pd


df = pd.read_csv("C:\FrameworkTalitha\Consumo_cerveja2.tsv", sep='\t')
df.columns = ['Data', 'Temp_Media', 'Temp_Min', 'Temp_Max', 'Precipitacao', 'Final_de_semana', 'Consumo_em_litros']
df["Data"] = pd.to_datetime(df["Data"])
df[["Temp_Media", "Temp_Min", "Temp_Max", "Precipitacao", "Consumo_em_litros"]] = df[["Temp_Media", "Temp_Min","Temp_Max", "Precipitacao","Consumo_em_litros"]].apply(pd.to_numeric)


class DescritorTabela:
    def __init__(self):
        self.df = df
        self.data = df.Data
        self.temp_max = df.Temp_Max
        self.temp_min = df.Temp_Min
        self.temp_media = df.Temp_Media
        self.precipitacao = df.Precipitacao
        self.consumo = df.Consumo_em_litros

    def dataset(self):
        self.df = df
        return df

    def temperatura_max(self):
        coluna_max = df.Temp_Max
        self.temp_max = coluna_max.max()
        coluna_data = df.Data
        self.data = coluna_data
        resposta = f"O dia {self.data} com maior temperatura teve um total de {self.temp_max}ºC."
        return resposta

    def temperatura_min(self):
        coluna_min = df.Temp_Min
        self.temp_min = coluna_min.min()
        resposta = f"O dia com menor temperatura teve um total de {self.temp_min}ºC."
        return resposta

    def dia_mais_chuvoso(self):
        coluna_precipitacao = df.Precipitacao
        self.precipitacao = coluna_precipitacao.max()
        resposta = f"O dia com mais chuva teve um total de {self.precipitacao} mm."
        return resposta

    def dia_com_maior_consumo(self):
        coluna_maior_consumo = df.Consumo_em_litros
        self.consumo = coluna_maior_consumo.max()
        resposta = f"O dia com maior consumo teve um total de {self.consumo} litros consumidos."
        return resposta

    def dia_com_menor_consumo(self):
        coluna_menor_consumo = df.Consumo_em_litros
        self.consumo = coluna_menor_consumo.min()
        resposta = f"O dia com menor consumo teve um total de {self.consumo} litros consumidos."
        return resposta

    def media_consumo(self):
        coluna_media_consumo = df.Consumo_em_litros
        self.consumo = coluna_media_consumo.mean()
        resposta = f"Média de consumo por dia foi de {self.consumo} litros consumidos."
        return resposta

    def soma_consumo(self):
        coluna_soma_consumo = df.Consumo_em_litros
        self.consumo = coluna_soma_consumo.sum()
        resposta = f"A soma de consumo do ano foi de {self.consumo} litros consumidos."
        return resposta
