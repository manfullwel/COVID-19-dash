# Dashboard COVID-19 Brasil

Dashboard interativo para visualização de dados da COVID-19 no Brasil, construído com Dash e Plotly.

## 🚀 Features

- Visualização de casos e óbitos por estado
- Mapa interativo com dados por região
- Gráficos temporais de evolução da pandemia
- Interface responsiva e moderna
- Tema dark para melhor visualização

## 🛠️ Tecnologias

- Python 3.9
- Dash
- Plotly
- Pandas
- Docker
- Gunicorn

## 📋 Pré-requisitos

- Python 3.9+
- Docker Desktop
- Token do Mapbox (para os mapas)

## 🔧 Instalação Local

1. Clone o repositório:
```bash
git clone [URL_DO_SEU_REPOSITORIO]
cd [NOME_DO_REPOSITORIO]
```

2. Crie um arquivo `.env` baseado no `.env.example`:
```bash
cp .env.example .env
```

3. Configure seu token do Mapbox no arquivo `.env`

4. Execute com Docker:
```bash
docker compose up --build
```

5. Acesse em: `http://localhost:10000`

## 🌐 Deploy no Render

1. Crie uma conta no [Render](https://render.com)
2. Conecte seu repositório GitHub
3. Crie um novo Web Service
4. Configure as variáveis de ambiente:
   - `PORT`: 10000
   - `MAPBOX_TOKEN`: seu_token_do_mapbox
   - `PYTHONUNBUFFERED`: 1

## 📦 Estrutura do Projeto

```
├── app.py              # Aplicação Dash
├── dashboard.py        # Lógica principal do dashboard
├── wsgi.py            # Ponto de entrada para Gunicorn
├── Dockerfile         # Configuração do container
├── docker-compose.yml # Orquestração do container
├── requirements.txt   # Dependências Python
└── .env.example      # Template de variáveis de ambiente
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
