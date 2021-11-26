__version__ = '0.0.2'
import sys
import pandas as pd


class DescritorTabela:
    """
    Construtor
    """
    def __init__(self, caminho_arq, sep='\t'):
        self.df = pd.read_csv(caminho_arq, sep=sep)
        self.df.columns = ['Data', 'Temp_Media', 'Temp_Min', 'Temp_Max', 'Precipitacao', 'Final_de_semana',
                           'Consumo_em_litros']
        self.df["Data"] = pd.to_datetime(self.df["Data"])
        self.df[["Temp_Media", "Temp_Min", "Temp_Max", "Precipitacao", "Consumo_em_litros"]] = self.df[["Temp_Media",
                                                                                                        "Temp_Min",
                                                                                                        "Temp_Max",
                                                                                                        "Precipitacao",
                                                                                                        "Consumo_em_litros"]].apply(pd.to_numeric)
        self.data = self.df.Data
        self.temp_max = self.df.Temp_Max
        self.temp_min = self.df.Temp_Min
        self.temp_media = self.df.Temp_Media
        self.precipitacao = self.df.Precipitacao
        self.consumo = self.df.Consumo_em_litros
        self.min_int = -sys.maxsize - 1
        self.max_int = sys.maxsize - 1

    def obter_data_temp_max(self):
        """
        Função filtra dados da maior temperatura do ano e sua data.
        """
        maior_temp = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_temp < self.df.iloc[i]['Temp_Max']:
                maior_temp = self.df.iloc[i]['Temp_Max']
                maior_data = self.df.iloc[i]['Data']

        resposta = f"O dia {maior_data} com maior temperatura teve um total de {maior_temp} ºC."
        return resposta

    def obter_data_temp_min(self):
        """
        Função filtra dados de menor temperatura do ano e sua data.
        """
        menor_temp = self.max_int
        maior_data = None

        for i in range(len(self.df)):
            if menor_temp > self.df.iloc[i]['Temp_Min']:
                menor_temp = self.df.iloc[i]['Temp_Min']
                maior_data = self.df.iloc[i]['Data']

        resposta = f"O dia {maior_data} com menor temperatura teve um total de {menor_temp} ºC."
        return resposta

    def obter_data_maior_precipatacao(self):
        """
        Função filtra dados de maior precipitação do ano e sua data.
        """
        maior_preci = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_preci < self.df.iloc[i]['Precipitacao']:
                maior_preci = self.df.iloc[i]['Precipitacao']
                maior_data = self.df.iloc[i]['Data']

        resposta = f"O dia {maior_data} com mais chuvoso teve um total de {maior_preci} mm."
        return resposta

    def obter_data_maior_consumo(self):
        """
        Função filtra dados de maior consumo do ano e sua data.
        """
        maior_consumo = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_consumo < self.df.iloc[i]['Consumo_em_litros']:
                maior_consumo = self.df.iloc[i]['Consumo_em_litros']
                maior_data = self.df.iloc[i]['Data']

        resposta = f"O dia {maior_data} com mais consumo teve um total de {maior_consumo} litros."
        return resposta

    def obter_data_menor_consumo(self):
        """
        Função filtra dados de menor consumo do ano e sua data.
        """
        menor_consumo = self.max_int
        maior_data = None

        for i in range(len(self.df)):
            if menor_consumo > self.df.iloc[i]['Consumo_em_litros']:
                menor_consumo = self.df.iloc[i]['Consumo_em_litros']
                maior_data = self.df.iloc[i]['Data']

        resposta = f"O dia {maior_data} com menor consumo teve um total de {menor_consumo} litros."
        return resposta

    def obter_media_consumo(self):
        """
        Função filtra media de consumo do ano.
        """
        coluna_media_consumo = self.df.Consumo_em_litros
        self.consumo = coluna_media_consumo.mean()
        resposta = f"Média de consumo por dia foi de {self.consumo} litros consumidos."
        return resposta

    def obter_soma_consumo(self):
        """
        Função filtra soma de consumo do ano.
        """
        coluna_soma_consumo = self.df.Consumo_em_litros
        self.consumo = coluna_soma_consumo.sum()
        resposta = f"A soma de consumo do ano foi de {self.consumo} litros consumidos."
        return resposta


dt = DescritorTabela("C:\FrameworkTalitha\Consumo_cerveja2.tsv")
print(dt.obter_media_consumo())
