# Dashboard COVID-19 Brasil

Um dashboard interativo para monitoramento de casos de COVID-19 no Brasil, desenvolvido com Dash e Plotly.

## Funcionalidades

- **Visualização de Dados em Tempo Real**
  - Mapa coroplético do Brasil
  - Gráfico de evolução temporal
  - Comparativo de casos por estado
  - Taxa de letalidade por estado

- **Filtros Interativos**
  - Seleção de data
  - Tipo de dados (casos, óbitos)
  - Visualização por estado ou país

- **Interface Responsiva**
  - Design adaptativo para diferentes dispositivos
  - Sidebar interativa
  - Cards informativos animados

## Tecnologias

- Python 3.8+
- Dash
- Plotly
- Pandas
- NumPy

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/igorsoarespy/covid19.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o dashboard:
```bash
python dashboard.py
```

## Estrutura do Projeto

```
covid-dashboard/
├── assets/
│   └── style.css        # Estilos do dashboard
├── data/
│   └── HIST_PAINEL_COVIDBR.csv  # Dados COVID
├── dashboard.py         # Aplicação principal
├── requirements.txt     # Dependências
└── README.md           # Documentação
```

## Pipeline de Atualização

1. **Coleta de Dados**
   - Download automático dos dados do Ministério da Saúde
   - Validação e limpeza dos dados

2. **Processamento**
   - Agregação por estado/região
   - Cálculo de métricas (taxa de letalidade, etc.)
   - Formatação para visualização

3. **Visualização**
   - Atualização dos gráficos
   - Recálculo de estatísticas
   - Cache de dados processados

## Contato

- **Desenvolvedor**: Igor Soares
- **Email**: igorofyeshua@gmail.com
- **Telegram**: @igordostrd

## Atualizações Recentes

### v2.0.0
- Novo design responsivo
- Adição de novos gráficos comparativos
- Melhorias na performance
- Interface mais moderna e profissional

### v1.0.0
- Lançamento inicial
- Funcionalidades básicas de visualização
- Mapa do Brasil interativo
