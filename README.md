# Dashboard COVID-19 Brasil

[![Deploy on Railway](https://railway.app/button.svg)](https://covid-19-dash-production.up.railway.app/)
![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Dash](https://img.shields.io/badge/dash-latest-green.svg)
![Docker](https://img.shields.io/badge/docker-latest-blue.svg)

Dashboard interativo para visualização de dados da COVID-19 no Brasil, construído com Dash e Plotly. Acesse o dashboard em produção: [COVID-19 Dashboard](https://covid-19-dash-production.up.railway.app/)

![Dashboard Preview](docs/dashboard-preview.png)

## 🚀 Features

- Visualização de casos e óbitos por estado
- Mapa interativo com dados por região
- Gráficos temporais de evolução da pandemia
- Interface responsiva e moderna
- Tema dark para melhor visualização
- Deploy automático via Railway
- Monitoramento em tempo real

## 🛠️ Stack Tecnológica

- **Frontend**: Dash, Plotly
- **Backend**: Python 3.9, Gunicorn
- **Dados**: Pandas, NumPy
- **Deploy**: Docker, Railway
- **Mapas**: Mapbox

## 🌐 Acesso Online

O dashboard está disponível em: https://covid-19-dash-production.up.railway.app/

Features do ambiente de produção:
- Deploy automático via GitHub
- HTTPS/SSL
- Monitoramento 24/7
- Auto-scaling
- Logs em tempo real

## 🔧 Desenvolvimento Local

### Pré-requisitos
- Python 3.9+
- Docker Desktop
- Token do Mapbox

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/manfullwel/COVID-19-dash.git
cd COVID-19-dash
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. Execute com Docker:
```bash
docker compose up --build
```

4. Acesse em: `http://localhost:10000`

## 📊 Dados

Os dados são atualizados regularmente e incluem:
- Casos confirmados por estado
- Óbitos por estado
- Taxa de mortalidade
- Evolução temporal
- Distribuição geográfica

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📫 Contato

Seu Nome - [Seu Email]

Link do Projeto: [https://github.com/manfullwel/COVID-19-dash](https://github.com/manfullwel/COVID-19-dash)
