import pandas as pd
import requests

def estabelecimentos_credenciados(trimestre: str) -> pd.DataFrame:
    """
    Função para extrair dados de estabelecimentos credenciados do Banco Central do Brasil.

    Atributo:
    String - AAAAQ - A ano e Q - trimestre (1-4)

    Saída:
    DataFrame com os dados de estabelecimentos credenciados.
    """
    # Monta a URL com o parâmetro "trimestre" passado à função
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/EstabCredTransDA(trimestre=@trimestre)?@trimestre='{trimestre}'&$top=100&$format=json&$select=trimestre,bandeira,funcaoCartao,qtdEstabCredenciados,qtdEstabAtivos"

    # Faz a requisição para a API
    req = requests.get(url)

    # Verifica o status da requisição
    print("Status Code: ", req.status_code)

    # Desserializa o JSON
    data = req.json()
    # Normaliza os dados para um DataFrame
    df = pd.json_normalize(data["value"])

    return df
