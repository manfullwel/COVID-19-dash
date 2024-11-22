import dash
from dash import dcc, html
from dash.dependencies import Input, Output, ClientsideFunction
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import json

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

token = open(".mapbox_token").read()
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
# Configurações de Estilo Global
app = dash.Dash(__name__, 
    external_stylesheets=[
        dbc.themes.CYBORG,
        'https://use.fontawesome.com/releases/v5.15.4/css/all.css'
    ]
)

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
    dbc.Row([
        # Sidebar melhorada
        dbc.Col([
            html.Div([
                # Logo e Título
                html.Div([
                    html.Div([
                        html.I(className="fas fa-virus", 
                             style={
                                 'fontSize': '2.8rem',
                                 'color': '#8B0000',
                                 'marginRight': '15px'
                             }),
                        html.Div([
                            html.H1("COVID-19", 
                                   style={
                                       'fontSize': '2.5rem',
                                       'fontWeight': '700',
                                       'margin': '0',
                                       'color': '#ffffff'
                                   }),
                            html.H2("BRASIL", 
                                   style={
                                       'fontSize': '1.8rem',
                                       'fontWeight': '600',
                                       'margin': '0',
                                       'color': '#8B0000'
                                   })
                        ])
                    ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '30px'}),
                ]),

                # Filtros
                html.Div([
                    html.Label("PERÍODO DE ANÁLISE", 
                             style={
                                 'fontSize': '0.85rem',
                                 'fontWeight': '600',
                                 'color': '#888',
                                 'letterSpacing': '1.5px',
                                 'marginBottom': '10px'
                             }),
                    dcc.DatePickerSingle(
                        id="date-picker",
                        min_date_allowed=df_states["data"].min(),
                        max_date_allowed=df_states["data"].max(),
                        date=df_states["data"].max(),
                        style={"width": "100%"},
                        className="mb-4"
                    ),

                    html.Label("TIPO DE DADOS", 
                             style={
                                 'fontSize': '0.85rem',
                                 'fontWeight': '600',
                                 'color': '#888',
                                 'letterSpacing': '1.5px',
                                 'marginBottom': '10px'
                             }),
                    dcc.Dropdown(
                        id="location-dropdown",
                        options=[{"label": j, "value": i}
                            for i, j in select_columns.items()
                        ],
                        value="casosNovos",
                        className="mb-4"
                    ),

                    html.Label("REGIÃO", 
                             style={
                                 'fontSize': '0.85rem',
                                 'fontWeight': '600',
                                 'color': '#888',
                                 'letterSpacing': '1.5px',
                                 'marginBottom': '10px'
                             }),
                    dcc.Dropdown(
                        id="location-button",
                        options=[
                            {"label": "Brasil", "value": "BRASIL"},
                            {"label": "Estados", "value": "ESTADOS"}
                        ],
                        value="BRASIL",
                        className="mb-4"
                    ),
                ], style={'marginBottom': '40px'}),

                # Cartão de Contato
                html.Div([
                    html.Div([
                        html.I(className="fas fa-user-circle", 
                              style={
                                  'fontSize': '3rem',
                                  'color': '#8B0000',
                                  'marginBottom': '15px'
                              }),
                        html.H3("Igor Soares",
                               style={
                                   'fontSize': '1.4rem',
                                   'fontWeight': '600',
                                   'color': '#ffffff',
                                   'marginBottom': '5px'
                               }),
                        html.H6("Desenvolvedor",
                               style={
                                   'fontSize': '0.9rem',
                                   'color': '#888',
                                   'marginBottom': '20px',
                                   'letterSpacing': '1px'
                               })
                    ], style={'textAlign': 'center'}),
                    
                    # Links de contato
                    html.A([
                        html.I(className="fas fa-envelope", 
                              style={'marginRight': '10px', 'width': '20px'}),
                        "igorofyeshua@gmail.com"
                    ],
                    href="mailto:igorofyeshua@gmail.com",
                    style=CONTACT_LINK_STYLE,
                    className="mb-2"),
                    
                    html.A([
                        html.I(className="fab fa-telegram", 
                              style={'marginRight': '10px', 'width': '20px'}),
                        "@igordostrd"
                    ],
                    href="https://t.me/igordostrd",
                    style=CONTACT_LINK_STYLE)
                ], style=CONTACT_CARD_STYLE)
            ], style=SIDEBAR_STYLE)
        ], md=3),
        
        # Conteúdo Principal
        dbc.Col([
            # Cards Informativos
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Casos Totais", className="card-subtitle text-muted"),
                            html.H3(id="casos-recuperados-text", className="card-title text-success")
                        ])
                    ], style=CARD_STYLE)
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Óbitos", className="card-subtitle text-muted"),
                            html.H3(id="obitos-text", className="card-title text-danger")
                        ])
                    ], style=CARD_STYLE)
                ], md=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H6("Casos Ativos", className="card-subtitle text-muted"),
                            html.H3(id="casos-ativos-text", className="card-title text-warning")
                        ])
                    ], style=CARD_STYLE)
                ], md=4)
            ], className="mb-4"),
            
            # Mapa e Gráfico de Evolução
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Distribuição Geográfica",
                                     style={'background': '#1a1a1a', 'color': '#fff'}),
                        dbc.CardBody([
                            dcc.Loading(
                                id="loading-1",
                                type="default",
                                children=[dcc.Graph(id="choropleth-map", figure=fig, style=GRAPH_STYLE)]
                            )
                        ])
                    ], style=CARD_STYLE)
                ], md=8),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Evolução Temporal",
                                     style={'background': '#1a1a1a', 'color': '#fff'}),
                        dbc.CardBody([
                            dcc.Graph(id="line-graph", style=GRAPH_STYLE)
                        ])
                    ], style=CARD_STYLE)
                ], md=4)
            ], className="mb-4"),
            
            # Novos Gráficos
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Comparativo de Casos por Estado",
                                     style={'background': '#1a1a1a', 'color': '#fff'}),
                        dbc.CardBody([
                            dcc.Graph(id="bar-chart", style=GRAPH_STYLE)
                        ])
                    ], style=CARD_STYLE)
                ], md=6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Taxa de Letalidade",
                                     style={'background': '#1a1a1a', 'color': '#fff'}),
                        dbc.CardBody([
                            dcc.Graph(id="mortality-chart", style=GRAPH_STYLE)
                        ])
                    ], style=CARD_STYLE)
                ], md=6)
            ])
        ], md=9)
    ])
], fluid=True, style={"padding": "20px", "background-color": "#141414"})

# =====================================================================
# Interactivity
@app.callback(
    [
        Output("casos-recuperados-text", "children"),
        Output("obitos-text", "children"),
    ], [Input("date-picker", "date"), Input("location-button", "value")]
)
def display_status(date, location):
    # print(location, date)
    if location == "BRASIL":
        df_data_on_date = df_brasil[df_brasil["data"] == date]
    else:
        df_data_on_date = df_states[(df_states["estado"] == location) & (df_states["data"] == date)]

    casos_acumulados = "-" if df_data_on_date["casosAcumulado"].isna().values[0]  else f'{int(df_data_on_date["casosAcumulado"].values[0]):,}'.replace(",", ".") 
    obitos_acumulado = "-" if df_data_on_date["obitosAcumulado"].isna().values[0]  else f'{int(df_data_on_date["obitosAcumulado"].values[0]):,}'.replace(",", ".") 
    return (
            casos_acumulados, 
            obitos_acumulado, 
            )


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
    [Input("date-picker", "date")]
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
    [Input("date-picker", "date")]
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
    [Input("date-picker", "date")]
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
    app.run_server(debug=False, port=8051)