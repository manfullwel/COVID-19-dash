import pandas as pd
import requests
from datetime import datetime
import os

def download_covid_data():
    """
    Download dos dados mais recentes do COVID-19 do Ministério da Saúde
    """
    url = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/HIST_PAINEL_COVIDBR.zip"
    
    try:
        # Download do arquivo
        response = requests.get(url)
        response.raise_for_status()
        
        # Salva o arquivo ZIP
        with open("data/temp.zip", "wb") as f:
            f.write(response.content)
        
        # Extrai e processa os dados
        df = pd.read_csv("data/temp.zip", compression="zip", sep=";")
        
        # Limpeza e processamento dos dados
        df["data"] = pd.to_datetime(df["data"])
        df = df.sort_values("data")
        
        # Calcula métricas adicionais
        df["letalidade"] = (df["obitosAcumulado"] / df["casosAcumulado"]) * 100
        
        # Salva o arquivo processado
        df.to_csv("data/HIST_PAINEL_COVIDBR.csv", index=False)
        
        # Remove arquivo temporário
        os.remove("data/temp.zip")
        
        print(f"Dados atualizados com sucesso em {datetime.now()}")
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar dados: {str(e)}")
        return False

def validate_data():
    """
    Validação básica dos dados
    """
    try:
        df = pd.read_csv("data/HIST_PAINEL_COVIDBR.csv")
        
        # Verifica se há dados recentes (últimos 7 dias)
        latest_date = pd.to_datetime(df["data"]).max()
        days_diff = (datetime.now() - latest_date).days
        
        if days_diff > 7:
            print(f"AVISO: Dados podem estar desatualizados. Última atualização: {latest_date}")
            return False
            
        # Verifica valores negativos
        if (df["casosAcumulado"] < 0).any() or (df["obitosAcumulado"] < 0).any():
            print("ERRO: Detectados valores negativos nos dados")
            return False
            
        print("Validação dos dados concluída com sucesso")
        return True
        
    except Exception as e:
        print(f"Erro na validação dos dados: {str(e)}")
        return False

if __name__ == "__main__":
    # Cria diretório de dados se não existir
    os.makedirs("data", exist_ok=True)
    
    # Download e processamento dos dados
    if download_covid_data():
        # Validação dos dados
        validate_data()
    else:
        raise Exception("Falha na atualização dos dados")
