import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.utils import ID

pio.renderers.default = 'browser'


def create_top_n_filter():
    return dmc.NumberInput(
        label="Top N ",
        description="Choose number of elements you want to see",
        value=5,
        min=1,
        step=1,
        max=100,
        style={"width": 250},
        id=ID.top_n_filter
    )
