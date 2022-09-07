
import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


df_raw = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv')







