# Dashboard COVID-19 Brasil

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Dash](https://img.shields.io/badge/dash-2.14.1-green.svg)
![Plotly](https://img.shields.io/badge/plotly-5.18.0-red.svg)

Dashboard interativo para visualização de dados da COVID-19 no Brasil, construído com Dash e Plotly.

![Dashboard Preview](docs/dashboard-preview.png)

## 🚀 Features

- Visualização de casos e óbitos por estado
- Mapa interativo com dados por região
- Gráficos temporais de evolução da pandemia
- Interface responsiva e moderna
- Tema dark para melhor visualização
- Filtros por data e região
- Indicadores em tempo real

## 🛠️ Stack Tecnológica

- **Frontend**: 
  - Dash v2.14.1
  - Plotly v5.18.0
  - Dash Bootstrap Components v1.5.0
- **Backend**: 
  - Python 3.9
  - Pandas v2.1.3
  - NumPy v1.26.2
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

## 📊 Dados

Os dados são atualizados regularmente e incluem:
- Casos confirmados por estado
- Óbitos por estado
- Taxa de mortalidade
- Evolução temporal
- Distribuição geográfica

### Estrutura dos Dados
```
dados_covid/
├── df_brasil.csv    # Dados agregados do Brasil
└── df_states.csv    # Dados por estado
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🔄 Versionamento

- **v1.0.0** - Versão inicial com funcionalidades básicas
- **v1.1.0** - Adição de filtros por data
- **v1.2.0** - Melhorias na interface e tema dark
- **v1.3.0** - Otimizações de performance
- **v1.4.0** - Correções de bugs e melhorias na visualização de dados
