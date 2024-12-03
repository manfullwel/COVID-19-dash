# Dashboard COVID-19 Brasil (2019-2023)

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Dash](https://img.shields.io/badge/dash-2.14.1-green.svg)
![Plotly](https://img.shields.io/badge/plotly-5.18.0-red.svg)

## 📋 Sobre o Projeto

Este dashboard foi desenvolvido em 2019, no início da pandemia de COVID-19, com o objetivo de democratizar o acesso à informação e demonstrar como a programação pode ser uma ferramenta poderosa na análise e visualização de dados em momentos críticos.

### 🎯 Propósito Original
Em um momento de incertezas e desinformação, este projeto nasceu da necessidade de:
- Fornecer dados confiáveis e atualizados sobre a COVID-19 no Brasil
- Demonstrar a importância da coleta e análise de dados
- Criar visualizações claras e acessíveis para o público geral
- Utilizar a tecnologia como ferramenta de conscientização

### 💡 Impacto e Aprendizados
O projeto demonstrou como a programação pode:
- Transformar dados brutos em informações úteis
- Auxiliar na tomada de decisões baseada em dados
- Conectar pessoas através da tecnologia
- Contribuir para a transparência e acesso à informação

## 🚀 Features

- Visualização de casos e óbitos por estado
- Mapa interativo com dados por região
- Gráficos temporais de evolução da pandemia
- Interface responsiva e moderna
- Tema dark para melhor visualização
- Filtros por data e região
- Indicadores em tempo real

## 🌐 Acesso Online

O dashboard está disponível em: [COVID-19 Dashboard](https://covid-19-dash-production.up.railway.app/)

### Ambiente de Produção
- Deploy contínuo via Railway
- Monitoramento 24/7
- Alta disponibilidade
- Atualizações automáticas

## 🛠️ Stack Tecnológica

- **Frontend**: 
  - Dash v2.14.1
  - Plotly v5.18.0
  - Dash Bootstrap Components v1.5.0
- **Backend**: 
  - Python 3.9
  - Pandas v2.1.3
  - NumPy v1.26.2
- **Deploy**: 
  - Docker
  - Railway
- **Mapas**: 
  - Mapbox
  - GeoJSON

## 🔧 Desenvolvimento Local

### Pré-requisitos
- Python 3.9+
- Token do Mapbox (opcional, para visualização do mapa)
- Git

### Instalação

1. Clone o repositório:
```bash
git clone [seu-repositorio]
cd COVID-19-dash
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Execute a aplicação:
```bash
python dashboard.py
```

6. Acesse em: `http://localhost:8080`

## 📊 Dados e Metodologia

### Fonte dos Dados
- Ministério da Saúde do Brasil
- Secretarias Estaduais de Saúde
- OpenDataSUS

### Estrutura
```
dados_covid/
├── df_brasil.csv    # Dados agregados do Brasil
└── df_states.csv    # Dados por estado
```

### Metodologia
Os dados são processados seguindo as melhores práticas de análise de dados:
- Limpeza e validação
- Normalização
- Agregação por região
- Cálculo de indicadores

## 🔄 Histórico de Versões

- **v1.0.0** (2019) - Lançamento inicial com dados básicos
- **v1.1.0** (2020) - Adição de filtros e melhorias na visualização
- **v1.2.0** (2021) - Interface dark e otimizações
- **v1.3.0** (2022) - Melhorias de performance
- **v1.4.0** (2023) - Atualizações finais e documentação

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> **Nota Histórica**: Este dashboard foi uma iniciativa para demonstrar como a tecnologia e a programação podem ser utilizadas para enfrentar desafios globais. Mesmo após o fim da fase mais crítica da pandemia, o projeto permanece como um exemplo da importância da análise de dados e da programação na sociedade moderna.
