import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify


def create_home_link(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )


def create_nav_bar_component():
    return dmc.Header(
        height=70,
        # fixed=True, # uncomment this line if you are using this example in your app
        p="md",
        children=[
            dmc.Container(
                fluid=True,
                children=dmc.Group(
                    position="apart",
                    align="flex-start",
                    children=[
                        dmc.Center(
                            dcc.Link(
                                [
                                    dmc.MediaQuery(
                                        create_home_link("Dash Autumn App Challenge"),
                                        smallerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                    dmc.MediaQuery(
                                        create_home_link("DMC"),
                                        largerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                ],
                                href="/",
                                style={"paddingTop": 5, "textDecoration": "none"},
                            ),
                        ),
                        dmc.Group(
                            position="right",
                            align="center",
                            spacing="xl",
                            children=[
                                html.H3('Here should come link to my website...')

                            ],
                        ),
                    ],
                ),
            )
        ],
    )
