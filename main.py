

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback

from src.components.all_bar_charts import create_all_bar_charts
from src.components.bar_chart import create_bar_chart
from src.components.metric_chooser import create_metric_chooser
from src.components.nav_bar import create_nav_bar_component
from src.components.top_n_filter import create_top_n_filter
from src.data.etl import df_raw

app = Dash(__name__)


app.layout = html.Div([

    create_nav_bar_component(),

    create_top_n_filter(),

    create_metric_chooser(),

    html.H1('Welcome to Dash!'),

    create_all_bar_charts(
        app=app,
        df=df_raw,
    )

])


if __name__ == '__main__':
    app.run_server(debug=True)
