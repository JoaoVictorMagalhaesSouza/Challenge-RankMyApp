import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

def init_app(server):
    app = dash.Dash(
        __name__, 
        suppress_callback_exceptions=True,
        server=server,
        external_stylesheets=[dbc.themes.CERULEAN]
    )
    
    server = app.server
    
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    }

    # padding for the page content
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }
    sidebar = html.Div(
    [
        #html.H2("Bem vindo!", className="display-4"),
        #html.Img(src='data:image/png;base64,{}'.format(test_base64), style={'height':'10%',}),
        html.Hr(),
        # html.P(
        #     "Barra de Navegação", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Basic Analisys", href="/", active="exact"),
                dbc.NavLink("Complementary Analisys", href='/complementary', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
    )
    content = html.Div(id="page-content", children=[], style=CONTENT_STYLE) 
    
    app.layout = html.Div([
        dcc.Location(id="url"),
        #dcc.Store(id='dados_predicao'),
        sidebar,
        content,       
        
    ])
    @app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    )
    def render_page_content(pathname):
        if pathname == "/":
            return[
                dcc.DatePickerRange(
                    clearable=True,
                    with_portal=True,
                    start_date = '2019-08-01',
                    end_date = '2019-10-30',
                    min_date_allowed = '2019-08-01',
                    max_date_allowed = '2019-10-30',
                    display_format = 'DD/MM/YYYY'
                )
                
                ]
    
    return app