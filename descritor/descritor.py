__version__ = '0.0.1'

import sys
import pandas as pd
import requests
import io


class DescritorTabela:
    """
    Construtor
    """

    def __init__(self):
        self.min_int = -sys.maxsize - 1
        self.max_int = sys.maxsize - 1

    def preparar_df(self):
        """
        Método edita o DataFrame, modificas o nome das colunas e o tipo numerico.
        """
        self.df.columns = ['Data', 'Temp_Media', 'Temp_Min', 'Temp_Max', 'Precipitacao', 'Final_de_semana',
                           'Consumo_em_litros']
        self.df["Data"] = pd.to_datetime(self.df["Data"])
        self.df[["Temp_Media", "Temp_Min", "Temp_Max", "Precipitacao", "Consumo_em_litros"]] = self.df[["Temp_Media",
                                                                                                        "Temp_Min",
                                                                                                        "Temp_Max",
                                                                                                        "Precipitacao",
                                                                                                        "Consumo_em_litros"]].apply(
            pd.to_numeric)
        self.data = self.df.Data
        self.temp_max = self.df.Temp_Max
        self.temp_min = self.df.Temp_Min
        self.temp_media = self.df.Temp_Media
        self.precipitacao = self.df.Precipitacao
        self.consumo = self.df.Consumo_em_litros

    def pesquisar_por_data(self, data_especifica):
        """
        Método pesquisa data específica que o usuário solicitar.
        Args:
            -data_especifica: Data especifica que o usuario quer pesquisar
        """
        try:
            col_data = self.df['Data']
            resultado = self.df.loc[col_data == data_especifica]
        except (TypeError):
            print("Coloque a data")
        else:
            return resultado

    def obter_data_temp_max(self):
        """
        Método filtra dados da maior temperatura do ano e sua data.
        """
        maior_temperatura = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_temperatura < self.df.iloc[i]['Temp_Max']:
                maior_temperatura = self.df.iloc[i]['Temp_Max']
                maior_data = self.df.iloc[i]['Data']
        return maior_temperatura, maior_data

    def obter_data_temp_min(self):
        """
        Método filtra dados de menor temperatura do ano e sua data.
        """
        menor_temperatura = self.max_int
        maior_data = None

        for i in range(len(self.df)):
            if menor_temperatura > self.df.iloc[i]['Temp_Min']:
                menor_temperatura = self.df.iloc[i]['Temp_Min']
                maior_data = self.df.iloc[i]['Data']
        return menor_temperatura, maior_data

    def obter_data_maior_precipatacao(self):
        """
        Método filtra dados de maior precipitação do ano e sua data.
        """
        maior_precipatacao = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_precipatacao < self.df.iloc[i]['Precipitacao']:
                maior_precipatacao = self.df.iloc[i]['Precipitacao']
                maior_data = self.df.iloc[i]['Data']
        return maior_precipatacao, maior_data

    def obter_data_maior_consumo(self):
        """
        Método filtra dados de maior consumo do ano e sua data.
        """
        maior_consumo = self.min_int
        maior_data = None

        for i in range(len(self.df)):
            if maior_consumo < self.df.iloc[i]['Consumo_em_litros']:
                maior_consumo = self.df.iloc[i]['Consumo_em_litros']
                maior_data = self.df.iloc[i]['Data']
        return maior_consumo, maior_data

    def obter_data_menor_consumo(self):
        """
        Método filtra dados de menor consumo do ano e sua data.
        """
        menor_consumo = self.max_int
        maior_data = None

        for i in range(len(self.df)):
            if menor_consumo > self.df.iloc[i]['Consumo_em_litros']:
                menor_consumo = self.df.iloc[i]['Consumo_em_litros']
                maior_data = self.df.iloc[i]['Data']
        return menor_consumo, maior_data

    def obter_media_consumo(self):
        """
        Método filtra media de consumo do ano.
        """
        coluna_media_consumo = self.df.Consumo_em_litros
        self.consumo = coluna_media_consumo.mean()
        return self.consumo

    def obter_soma_consumo(self):
        """
        Método filtra soma de consumo do ano.
        """
        coluna_soma_consumo = self.df.Consumo_em_litros
        self.consumo = coluna_soma_consumo.sum()
        return self.consumo

    def df(self):
        """
        Método projeta tabela do Dataframe.
        """
        return self.df


class DescritorLocal(DescritorTabela):

    def __init__(self, caminho_arq=None):
        super().__init__()

        caminho_arq = "C:\FrameworkTalitha\dados\consumo_cerveja.tsv" if not caminho_arq else caminho_arq
        try:
            self.df = pd.read_csv(caminho_arq, sep='\t')
        except (FileNotFoundError):
            raise ExceçãoDatasetNãoEncontrado("Passe o Dataset certo!")

        self.preparar_df()


class DescritorRemoto(DescritorTabela):

    def __init__(self, url_base_dados=None):
        super().__init__()

        url_base_dados = "https://raw.githubusercontent.com/Dauerrr/FrameworkConsumo/main/dados/consumo_cerveja.tsv" if not url_base_dados else url_base_dados
        conteudo = requests.get(url_base_dados).content
        conteudo_utf8 = io.StringIO(conteudo.decode('utf-8'))
        self.df = pd.read_csv(conteudo_utf8, sep='\t')
        self.preparar_df()


class ExceçãoDatasetNãoEncontrado(Exception):
    pass
