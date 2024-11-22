import os
import sys
import subprocess
import pandas as pd
import requests
from datetime import datetime
import json

# URLs alternativas para dados COVID-19
BRASIL_IO_URL = "https://api.brasil.io/v1/dataset/covid19/caso/data/"
WCOTA_URL = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"

def create_directories():
    """Cria os diretórios necessários"""
    os.makedirs("data", exist_ok=True)
    os.makedirs("temp", exist_ok=True)
    print("✓ Diretórios criados")

def download_data():
    """Download dos dados do COVID-19"""
    try:
        print("Baixando dados do repositório WCota...")
        response = requests.get(WCOTA_URL)
        response.raise_for_status()
        
        # Salva os dados brutos
        raw_data_path = os.path.join("data", "covid19_raw.csv")
        with open(raw_data_path, "wb") as f:
            f.write(response.content)
        
        print("✓ Download concluído")
        return raw_data_path
    except Exception as e:
        print(f"❌ Erro no download: {str(e)}")
        return None

def process_data(data_path):
    """Processa os dados baixados"""
    try:
        print("Processando dados...")
        df = pd.read_csv(data_path)
        
        # Renomeando colunas para manter compatibilidade
        column_map = {
            'state': 'estado',
            'date': 'data',
            'totalCases': 'casosAcumulado',
            'deaths': 'obitosAcumulado',
            'newCases': 'casosNovos',
            'newDeaths': 'obitosNovos'
        }
        df = df.rename(columns=column_map)
        
        # Convertendo data
        df['data'] = pd.to_datetime(df['data'])
        
        # Calculando métricas adicionais
        df['letalidade'] = (df['obitosAcumulado'] / df['casosAcumulado']) * 100
        
        # Organizando as colunas
        columns_order = [
            'estado', 'data', 'casosAcumulado', 'casosNovos',
            'obitosAcumulado', 'obitosNovos', 'letalidade'
        ]
        df = df[columns_order]
        
        # Salvando dados processados
        output_path = os.path.join("data", "HIST_PAINEL_COVIDBR.csv")
        df.to_csv(output_path, index=False)
        
        # Criando um resumo dos dados
        summary = {
            'última_atualização': df['data'].max().strftime('%Y-%m-%d'),
            'total_casos': int(df['casosAcumulado'].max()),
            'total_obitos': int(df['obitosAcumulado'].max()),
            'estados': len(df['estado'].unique())
        }
        
        with open(os.path.join("data", "summary.json"), 'w') as f:
            json.dump(summary, f, indent=2)
        
        print("✓ Dados processados e salvos")
        print(f"\nResumo dos dados:")
        print(f"Última atualização: {summary['última_atualização']}")
        print(f"Total de casos: {summary['total_casos']:,}")
        print(f"Total de óbitos: {summary['total_obitos']:,}")
        print(f"Estados cobertos: {summary['estados']}")
        
        return True
    except Exception as e:
        print(f"❌ Erro no processamento: {str(e)}")
        return False

def clean_temp():
    """Limpa arquivos temporários"""
    try:
        for file in os.listdir("temp"):
            os.remove(os.path.join("temp", file))
        print("✓ Arquivos temporários removidos")
    except Exception as e:
        print(f"❌ Erro na limpeza: {str(e)}")

def start_dashboard():
    """Inicia o dashboard"""
    try:
        print("\nIniciando o dashboard...")
        subprocess.run([sys.executable, "dashboard.py"])
    except Exception as e:
        print(f"❌ Erro ao iniciar dashboard: {str(e)}")

def run_pipeline():
    """Executa o pipeline completo"""
    print("\n=== Iniciando Pipeline Local ===")
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Cria diretórios
    create_directories()
    
    # Download dos dados
    data_path = download_data()
    if not data_path:
        return False
    
    # Processamento dos dados
    success = process_data(data_path)
    if not success:
        return False
    
    # Limpeza
    clean_temp()
    
    print("\n✓ Pipeline executado com sucesso!")
    return True

if __name__ == "__main__":
    if run_pipeline():
        # Pergunta se deseja iniciar o dashboard
        response = input("\nDeseja iniciar o dashboard agora? (s/n): ")
        if response.lower() == 's':
            start_dashboard()
