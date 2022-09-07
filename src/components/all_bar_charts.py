import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.components.bar_chart import create_bar_chart
from src.utils import all_dimensions, ID

pio.renderers.default = 'browser'


def create_all_bar_charts(
        app: Dash,
        df: pd.DataFrame,
):

    @callback(
        Output(component_id=ID.all_bar_charts_container, component_property='children'),
        Input(component_id=ID.top_n_filter, component_property='value'),
        Input(component_id=ID.metric_chooser, component_property='value')
    )
    def update_all_bar_charts(
            top_n,
            metric_chosen
    ):
        if top_n is None:
            return dash.no_update

        if metric_chosen is None:
            return dash.no_update

        container_ = dmc.Container([
            dmc.SimpleGrid(
                spacing='lg',
                cols=2,
                breakpoints=[
                    {"maxWidth": 980, "cols": 3, "spacing": "md"},
                    {"maxWidth": 755, "cols": 2, "spacing": "sm"},
                    {"maxWidth": 600, "cols": 1, "spacing": "sm"},
                ],

                style={
                    "textAlign": "center",
                },

                children=[create_bar_chart(app=app, df=df, n_largest=top_n, y_axis=metric_chosen, x_axis=i, title='') for i in all_dimensions]

            )
        ], fluid=True)

        return container_

    return html.Div(id=ID.all_bar_charts_container)


