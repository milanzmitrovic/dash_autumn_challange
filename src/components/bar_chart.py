

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.renderers.default = 'browser'


def bar_chart(
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        n_largest=10
):
    # Aggregating data before plotting
    dff = df[[
        x_axis,
        y_axis
    ]].groupby(
        by=[x_axis],
        as_index=False
    ).agg('sum')

    dff.sort_values(by=y_axis, inplace=True, ascending=False)

    dff = dff.nlargest(n=n_largest, columns=y_axis)

    # Creating figure
    fig = px.histogram(
        x=dff[x_axis].astype(str),
        y=dff[y_axis],
        template='simple_white'
    )

    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        yaxis_title=y_axis,
        xaxis_title=x_axis
    )
    return fig


def create_bar_chart(
        app: Dash,
        df: pd.DataFrame,
        x_axis: str,
        y_axis: str,
        title: str,
        n_largest=10
):
    return dmc.Paper([

        dmc.Title(title, style={'textAlign': 'center'}),

        dcc.Graph(
            figure=bar_chart(
                df=df,
                x_axis=x_axis,
                y_axis=y_axis,
                n_largest=n_largest
            )
        )

    ],
        withBorder=True,
        radius='lg',
        shadow='xl')



