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
import os

# Inicialização do app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server  # Expondo o servidor para o Gunicorn

# Importando o layout e callbacks do dashboard original
from dashboard import *

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run_server(host="0.0.0.0", port=port, debug=False)
