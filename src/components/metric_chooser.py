from typing import get_type_hints

import dash
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html, callback
import plotly.express as px
import pandas as pd
import plotly.io as pio

from src.utils import ID, Metrics, all_metrics


def create_metric_chooser():
    return dmc.Select(
        label="Select Metric",
        placeholder="Please select metric",
        id=ID.metric_chooser,
        value=all_metrics[0],
        data=all_metrics,
        style={"width": 200, "marginBottom": 10},
    )
