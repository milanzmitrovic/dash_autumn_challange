# import dash
# import dash_mantine_components as dmc
# from dash import Dash, Input, Output, State, dcc, html, callback
# import plotly.express as px
# import pandas as pd
# import plotly.io as pio
#
# pio.renderers.default = 'browser'
#
# df_raw = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv')
#
# df_raw.columns
#
# df_raw['item_description'].unique().__len__()
#
#
# # Bar chart
#
#
# # Line chart
# # date
# #
# # volume_sold_gallons
# # volume_sold_liters
# # sale_dollars
# # bottles_sold
# # state_bottle_retail
# # state_bottle_cost
# # bottle_volume_ml
# # pack
#
#
# # Treemap, Sunburst, Icicle chart
#
#
# # Pie chart
#
#
# def bar_chart(
#         df: pd.DataFrame,
#         x_axis: str,
#         y_axis: str,
#         n_largest=10
# ):
#     print(df)
#     # Aggregating data before plotting
#     dff = df[[
#         x_axis,
#         y_axis
#     ]].groupby(
#         by=[x_axis],
#         as_index=False
#     ).agg('sum')
#
#     print(dff)
#
#     dff.sort_values(by=y_axis, inplace=True, ascending=False)
#
#     dff = dff.nlargest(n=n_largest, columns=y_axis)
#
#     print(dff)
#
#     # Creating figure
#     fig = px.histogram(
#         x=dff[x_axis].astype(str),
#         y=dff[y_axis],
#         template='simple_white'
#     )
#
#     fig.update_layout(
#         margin=dict(t=50, l=25, r=25, b=25),
#         yaxis_title=y_axis,
#         xaxis_title=x_axis
#     )
#     return fig
#
#
# def create_bar_chart(
#         app: Dash,
#         df: pd.DataFrame,
#         x_axis: str,
#         y_axis: str,
#         title: str,
#         n_largest=10
# ):
#     return dmc.Paper([
#
#         dmc.Title(title, style={'textAlign': 'center'}),
#
#         dcc.Graph(
#             figure=bar_chart(
#                 df=df,
#                 x_axis=x_axis,
#                 y_axis=y_axis,
#                 n_largest=n_largest
#             )
#         )
#
#     ],
#         withBorder=True,
#         radius='lg',
#         shadow='xl')
#
#
#
# bar_chart(
#     df=df_raw,
#     x_axis='store_number',
#     y_axis='volume_sold_gallons',
#     n_largest=10
# ).show()
#
#
#
# len(df_raw['store_number'].unique())
#
# # Aggregating data before plotting
# dff = df_raw[[
#     'store_number',
#     'volume_sold_gallons'
# ]].groupby(
#     by=['store_number'],
#     as_index=False
# ).agg('sum')
#
#
# dff = dff.nlargest(n=10, columns='volume_sold_gallons')
#
# dff
#
# # Creating figure
# fig = px.histogram(
#     x=dff['store_number'],
#     y=dff['volume_sold_gallons'],
#     # template='simple_white'
# )
#
# fig.show()
#
#
