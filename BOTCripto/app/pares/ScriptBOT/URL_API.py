import json
import os
import pandas as pd

def ler_arquivo_endpoint():
    # Obtém o diretório atual do script
    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    # Caminho do arquivo endpoint.json
    caminho_arquivo = os.path.join(diretorio_script, "../endpoint.json")

    try:
        # Abre o arquivo e carrega os dados em formato JSON
        with open(caminho_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o JSON no arquivo {caminho_arquivo}.")
        return None


def montar_endpoints():
    dados_endpoint = ler_arquivo_endpoint()
    def URL_API(base_point, endpoints):
      return base_point + endpoints

    if dados_endpoint:
        # Cria uma lista de dicionários para o DataFrame
        dados_dataframe = [
            {
                'Exchange': par['exchange'],
                'Utilization': par['observation'],
                'URL_API': URL_API(par['base_point'], par['endpoints'])
            }
            for par in dados_endpoint
        ]

        # Cria o DataFrame
        endpoints = pd.DataFrame(dados_dataframe)

        return endpoints
    else:
        return None

def obter_url_por_exchange_utilizacao( exchange, utilizacao):
    endpoints = montar_endpoints()
    filtro = (endpoints['Exchange'] == exchange) & (endpoints['Utilization'] == utilizacao)

    resultados = endpoints.loc[filtro, 'URL_API']

    if not resultados.empty:
        return resultados.iloc[0]  # Retorna a primeira URL encontrada
    else:
        return None  # Retorna None se não houver correspondência
