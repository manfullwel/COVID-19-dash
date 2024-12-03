import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, ClientsideFunction
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import json
import datetime as dt

# Otimizações de memória
pd.options.mode.chained_assignment = None

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

CENTER_LAT, CENTER_LON = -14.272572694355336, -51.25567404158474

# =====================================================================
# Data Generation
# df = pd.read_csv("HIST_PAINEL_COVIDBR_13mai2021.csv", sep=";")
# df_states = df[(~df["estado"].isna()) & (df["codmun"].isna())]
# df_brasil = df[df["regiao"] == "Brasil"]
# df_states.to_csv("df_states.csv")
# df_brasil.to_csv("df_brasil.csv")

# =====================================================================
# Data Load
df_states = pd.read_csv("df_states.csv")
df_brasil = pd.read_csv("df_brasil.csv")

df_states['data'] = pd.to_datetime(df_states['data'])
df_brasil['data'] = pd.to_datetime(df_brasil['data'])

min_date = df_states['data'].min()
max_date = df_states['data'].max()

token = os.getenv("MAPBOX_TOKEN", "")  # Valor default vazio caso não encontre
brazil_states = json.load(open("geojson/brazil_geo.json", "r"))

brazil_states["features"][0].keys()

df_states_ = df_states[df_states["data"] == "2020-05-13"]
select_columns = {"casosAcumulado": "Casos Acumulados", 
                "casosNovos": "Novos Casos", 
                "obitosAcumulado": "Óbitos Totais",
                "obitosNovos": "Óbitos por dia"}

SIDEBAR_STYLE = {
    'background': 'linear-gradient(180deg, #1a1a1a 0%, #0D0D0D 100%)',
    'box-shadow': '2px 0 20px rgba(0, 0, 0, 0.4)',
    'padding': '25px',
    'height': '100vh',
    'position': 'sticky',
    'top': '0',
    'border-right': '1px solid #333'
}

TITLE_CONTAINER_STYLE = {
    'background': 'linear-gradient(to right, #8B0000, #590000)',
    'padding': '25px 20px',
    'border-radius': '10px',
    'margin-bottom': '30px',
    'box-shadow': '0 4px 15px rgba(0, 0, 0, 0.2)',
}

AUTHOR_CONTAINER_STYLE = {
    'background-color': '#242424',
    'padding': '20px',
    'border-radius': '10px',
    'margin-top': 'auto',
    'border': '1px solid #333',
    'box-shadow': '0 2px 10px rgba(0, 0, 0, 0.1)'
}

CARD_STYLE = {
    'background-color': '#1a1a1a',
    'border': '1px solid #333',
    'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
    'border-radius': '10px',
    'margin-bottom': '15px',
    'transition': 'all 0.3s ease'
}

EMERGENCY_TITLE_STYLE = {
    'background': 'linear-gradient(45deg, #8B0000, #FF0000)',
    'padding': '15px',
    'border-radius': '10px',
    'margin-bottom': '20px',
    'box-shadow': '0 4px 15px rgba(255, 0, 0, 0.2)',
    'animation': 'pulse 2s infinite'
}

CONTACT_STYLE = {
    'background-color': '#2d2d2d',
    'padding': '15px',
    'border-radius': '10px',
    'margin-top': '20px',
    'border': '1px solid #444'
}

GRAPH_STYLE = {
    'background-color': '#2C3E50',
    'padding': '15px',
    'border-radius': '10px',
    'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
}

CONTACT_CARD_STYLE = {
    'background': 'linear-gradient(45deg, #1a1a1a, #2d2d2d)',
    'border': '1px solid #444',
    'border-radius': '10px',
    'padding': '20px',
    'margin-top': '30px',
    'box-shadow': '0 4px 15px rgba(0, 0, 0, 0.2)'
}

CONTACT_LINK_STYLE = {
    'color': '#ffffff',
    'text-decoration': 'none',
    'padding': '10px 15px',
    'border-radius': '8px',
    'background': 'rgba(255, 255, 255, 0.05)',
    'margin-bottom': '10px',
    'display': 'flex',
    'align-items': 'center',
    'transition': 'all 0.3s ease'
}

# =====================================================================
# Configuração inicial do app
app = dash.Dash(__name__, 
                external_stylesheets=[
                    dbc.themes.CYBORG,
                    'https://use.fontawesome.com/releases/v5.15.4/css/all.css',
                    'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap'
                ])

# Rota de healthcheck simples
@app.server.route('/health')
def health_check():
    return 'OK', 200

server = app.server

# =====================================================================
# Configuração do mapa com estilo melhorado
fig = px.choropleth_mapbox(df_states_, 
    locations="estado",
    geojson=brazil_states, 
    center={"lat": -16.95, "lon": -47.78},
    zoom=4, 
    color="casosNovos",
    color_continuous_scale="Viridis",
    opacity=0.7,
    hover_data={
        "estado": True,
        "casosAcumulado": True,
        "casosNovos": True,
        "obitosNovos": True
    }
)

fig.update_layout(
    paper_bgcolor="#1E1E1E",
    plot_bgcolor="#1E1E1E",
    mapbox_style="carto-darkmatter",
    margin=dict(l=0, r=0, t=0, b=0),
    hoverlabel=dict(
        bgcolor="#2C3E50",
        font_size=14,
        font_family="Arial"
    )
)

df_data = df_states[df_states["estado"] == "RO"]

fig2 = go.Figure(layout={"template":"plotly_dark"})
fig2.add_trace(go.Scatter(x=df_data["data"], y=df_data["casosAcumulado"]))
fig2.update_layout(
    paper_bgcolor="#242424",
    plot_bgcolor="#242424",
    autosize=True,
    margin=dict(l=10, r=10, b=10, t=10),
    )

# =====================================================================
# Layout principal com melhorias
app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("COVID-19 Dashboard Analytics", className='cyber-text text-center mb-3'),
                html.P("Análise Avançada de Dados da Pandemia no Brasil", 
                      className='text-center text-light mb-4 lead')
            ], className='glass-container p-4 hover-glow')
        ])
    ], className='mb-4'),

    # Info Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    html.I(className="fas fa-chart-line fa-2x mb-3", style={'color': '#00F3FF'}),
                    html.H3("Análise de Dados", className='cyber-text'),
                    html.P("Visualização interativa de tendências e padrões", className='text-light')
                ], className='text-center p-4')
            ], className='hover-scale mb-4')
        ], md=4),
        dbc.Col([
            dbc.Card([
                html.Div([
                    html.I(className="fas fa-map-marked-alt fa-2x mb-3", style={'color': '#FF00E5'}),
                    html.H3("Mapeamento", className='cyber-text'),
                    html.P("Distribuição geográfica dos casos", className='text-light')
                ], className='text-center p-4')
            ], className='hover-scale mb-4')
        ], md=4),
        dbc.Col([
            dbc.Card([
                html.Div([
                    html.I(className="fas fa-brain fa-2x mb-3", style={'color': '#8B40BF'}),
                    html.H3("Insights", className='cyber-text'),
                    html.P("Descobertas baseadas em dados", className='text-light')
                ], className='text-center p-4')
            ], className='hover-scale mb-4')
        ], md=4),
    ]),

    # Controles
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H4("Controles de Visualização", className='cyber-text mb-3'),
                dbc.Row([
                    dbc.Col([
                        html.Label("PERÍODO DE ANÁLISE", className='text-light mb-2'),
                        dcc.DatePickerRange(
                            id="date-picker",
                            min_date_allowed=min_date,
                            max_date_allowed=max_date,
                            start_date=max_date - pd.Timedelta(days=30),
                            end_date=max_date,
                            display_format='DD/MM/YYYY',
                            className='neon-border'
                        ),
                    ], md=6),
                    dbc.Col([
                        html.Label("TIPO DE DADOS", className='text-light mb-2'),
                        dcc.Dropdown(
                            id="location-button",
                            options=[
                                {"label": "BRASIL", "value": "BRASIL"},
                                {"label": "ESTADOS", "value": "ESTADOS"},
                            ],
                            value="BRASIL",
                            className='neon-border'
                        ),
                    ], md=6),
                ])
            ], className='glass-container p-4 mb-4')
        ])
    ]),

    # Indicadores
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Div([
                    html.H5("CASOS RECUPERADOS", className='text-light mb-3'),
                    html.H3(id="casos-recuperados-text", className='cyber-text pulse')
                ], className='text-center p-3')
            ], className='hover-glow mb-4')
        ], md=6),
        dbc.Col([
            dbc.Card([
                html.Div([
                    html.H5("ÓBITOS", className='text-light mb-3'),
                    html.H3(id="obitos-text", className='cyber-text pulse')
                ], className='text-center p-3')
            ], className='hover-glow mb-4')
        ], md=6),
    ]),

    # Gráficos
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id="choropleth-map", className='neon-border')
            ], className='glass-container p-4 mb-4')
        ], md=12),
    ]),

    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id="bar-chart", className='neon-border')
            ], className='glass-container p-4 mb-4')
        ], md=6),
        dbc.Col([
            html.Div([
                dcc.Graph(id="mortality-chart", className='neon-border')
            ], className='glass-container p-4 mb-4')
        ], md=6),
    ]),

    # Footer
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P([
                    "Desenvolvido com ",
                    html.I(className="fas fa-heart", style={'color': '#FF00E5'}),
                    " e Python"
                ], className='text-center text-light mb-0')
            ], className='glass-container p-3')
        ])
    ])
], fluid=True, className='py-4')

# =====================================================================
# Interactivity
@app.callback(
    [
        Output("casos-recuperados-text", "children"),
        Output("obitos-text", "children"),
    ], [Input("date-picker", "end_date"), Input("location-button", "value")]
)
def display_status(date, location):
    try:
        if location == "BRASIL":
            df_data_on_date = df_brasil[df_brasil["data"] == date]
        else:
            df_data_on_date = df_states[(df_states["estado"] == location) & (df_states["data"] == date)]

        if df_data_on_date.empty:
            return "-", "-"

        casos_acumulados = "-"
        obitos_acumulado = "-"

        if not df_data_on_date["casosAcumulado"].empty and not df_data_on_date["casosAcumulado"].isna().all():
            casos = df_data_on_date["casosAcumulado"].iloc[0]
            casos_acumulados = f'{int(casos):,}'.replace(",", ".") if not pd.isna(casos) else "-"

        if not df_data_on_date["obitosAcumulado"].empty and not df_data_on_date["obitosAcumulado"].isna().all():
            obitos = df_data_on_date["obitosAcumulado"].iloc[0]
            obitos_acumulado = f'{int(obitos):,}'.replace(",", ".") if not pd.isna(obitos) else "-"

        return casos_acumulados, obitos_acumulado
    except Exception as e:
        print(f"Erro em display_status: {str(e)}")
        return "-", "-"


@app.callback(
        Output("line-graph", "figure"),
        [Input("location-dropdown", "value"), Input("location-button", "value")]
)
def plot_line_graph(plot_type, location):
    if location == "BRASIL":
        df_data_on_location = df_brasil.copy()
    else:
        df_data_on_location = df_states[(df_states["estado"] == location)]
    fig2 = go.Figure(layout={"template":"plotly_dark"})
    bar_plots = ["casosNovos", "obitosNovos"]

    if plot_type in bar_plots:
        fig2.add_trace(go.Bar(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    else:
        fig2.add_trace(go.Scatter(x=df_data_on_location["data"], y=df_data_on_location[plot_type]))
    
    fig2.update_layout(
        paper_bgcolor="#242424",
        plot_bgcolor="#242424",
        autosize=True,
        margin=dict(l=10, r=10, b=10, t=10),
        )
    return fig2


@app.callback(
    Output("choropleth-map", "figure"), 
    [Input("date-picker", "end_date")]
)
def update_map(date):
    df_data_on_states = df_states[df_states["data"] == date]

    fig = px.choropleth_mapbox(df_data_on_states, locations="estado", geojson=brazil_states, 
        center={"lat": CENTER_LAT, "lon": CENTER_LON},  # https://www.google.com/maps/ -> right click -> get lat/lon
        zoom=4, color="casosAcumulado", color_continuous_scale="Redor", opacity=0.55,
        hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": False}
        )

    fig.update_layout(paper_bgcolor="#1E1E1E", mapbox_style="carto-darkmatter", autosize=True,
                    margin=go.layout.Margin(l=0, r=0, t=0, b=0), showlegend=False)
    return fig


@app.callback(
    Output("location-button", "value"),
    [Input("choropleth-map", "clickData"), Input("location-button", "n_clicks")]
)
def update_location(click_data, n_clicks):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if click_data is not None and changed_id != "location-button.n_clicks":
        state = click_data["points"][0]["location"]
        return "{}".format(state)
    
    else:
        return "BRASIL"


@app.callback(
    Output("bar-chart", "figure"),
    [Input("date-picker", "end_date")]
)
def update_bar_chart(date):
    df_date = df_states[df_states["data"] == date].sort_values("casosAcumulado", ascending=True)
    
    fig = go.Figure(data=[
        go.Bar(
            y=df_date["estado"],
            x=df_date["casosAcumulado"],
            orientation='h',
            marker_color='#8B0000'
        )
    ])
    
    fig.update_layout(
        plot_bgcolor="#1a1a1a",
        paper_bgcolor="#1a1a1a",
        font=dict(color="#ffffff"),
        margin=dict(l=10, r=10, t=10, b=10),
        yaxis=dict(showgrid=False),
        xaxis=dict(showgrid=True, gridcolor="#333333")
    )
    
    return fig

@app.callback(
    Output("mortality-chart", "figure"),
    [Input("date-picker", "end_date")]
)
def update_mortality_chart(date):
    df_date = df_states[df_states["data"] == date]
    df_date["letalidade"] = (df_date["obitosAcumulado"] / df_date["casosAcumulado"]) * 100
    
    fig = go.Figure(data=[
        go.Scatter(
            x=df_date["estado"],
            y=df_date["letalidade"],
            mode='lines+markers',
            marker=dict(size=8, color='#ff4444'),
            line=dict(color='#8B0000', width=2)
        )
    ])
    
    fig.update_layout(
        plot_bgcolor="#1a1a1a",
        paper_bgcolor="#1a1a1a",
        font=dict(color="#ffffff"),
        margin=dict(l=10, r=10, t=10, b=10),
        yaxis=dict(
            title="Taxa de Letalidade (%)",
            showgrid=True,
            gridcolor="#333333"
        ),
        xaxis=dict(
            title="Estados",
            showgrid=False,
            tickangle=45
        )
    )
    
    return fig

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run_server(debug=False, host="0.0.0.0", port=port)