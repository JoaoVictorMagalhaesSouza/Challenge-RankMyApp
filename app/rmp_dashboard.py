import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from backend import BackEndDashboard

def init_app(server):
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
    app = dash.Dash(
        __name__, 
        suppress_callback_exceptions=True,
        server=server,
        external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME]
    )
    backend = BackEndDashboard()
    server = app.server
    
    card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
    }
    def create_card_views(start_date='2019-08-01',end_date='2019-10-30'):
        card_views = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Total Views", className="card-title"),
                        html.P(backend.get_app_views(start_date,end_date), className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-primary",
                style={"maxWidth": 75},
            ),
        ],
        className="mt-4 shadow",
        )
        return card_views
    
    def create_card_installations(start_date='2019-08-01',end_date='2019-10-30'):
        card_installations = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5("Total Installations", className="card-title"),
                        html.P(backend.get_app_installations(start_date,end_date), className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_installations
    
    def create_card_day_more_views(start_date='2019-08-01',end_date='2019-10-30'):
        
        dados = backend.get_weekday_with_more_views(start_date,end_date)
        card_more_vis = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('More accum. views', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} views', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow"
        )
        
        return card_more_vis

    def create_card_day_less_views(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_weekday_with_less_views(start_date,end_date)
        card_less_vis = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Less accum. views', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} views', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-danger",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_less_vis

    def create_card_day_more_downs(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_weekday_with_more_installers(start_date,end_date)
        card_more_downs = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('More accum. installs', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} installs', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75, 'background-color':'#00a000 !important'},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_more_downs
    
    def create_card_day_less_downs(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_weekday_with_less_installers(start_date,end_date)
        card_less_downs = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Less accum. installs', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} installs', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-danger",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_less_downs
    
    def create_card_average_views(start_date='2019-08-01',end_date='2019-10-30'):
        """
        quantidade de dias com visualizações acima da média
        """
        card_boom_views = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Boom view days', className="card-title"),
                        html.P(f'{backend.get_number_of_days_with_above_average_views(start_date,end_date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_boom_views
    
    def create_card_average_installs(start_date='2019-08-01',end_date='2019-10-30'):
        """
        quantidade de dias com instalações acima da média
        """
        card_boom_installs = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Boom installs days', className="card-title"),
                        html.P(f'{backend.get_number_of_days_with_above_average_installs(start_date,end_date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_boom_installs
    
    def create_card_total_days(start_date='2019-08-01',end_date='2019-10-30'):
        
        card_total_days = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Total days', className="card-title"),
                        html.P(f'{backend.get_total_days(start_date,end_date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-calendar", style=card_icon),
                className="bg-warning",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_total_days
    
    def create_card_best_views_day(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_best_view_day()
        card_best_views_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Best views day', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} views', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_best_views_day
    
    def create_card_worst_views_day(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_worst_view_day()
        card_worst_views_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Worst views day', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} views', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-danger",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_worst_views_day
    
    def create_card_best_installs_day(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_best_installs_day()
        card_best_installs_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Best installs day', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} installs', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-success",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_best_installs_day
    
    def create_card_worst_installs_day(start_date='2019-08-01',end_date='2019-10-30'):
        dados = backend.get_worst_installs_day()
        card_worst_installs_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Worst installs day', className="card-title"),
                        html.P(f'{dados[0]}: {dados[1]} installs', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-download", style=card_icon),
                className="bg-danger",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card_worst_installs_day
    


    
    
    
    
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
                dbc.NavLink("Periodic Analisys", href="/", active="exact"),
                dbc.NavLink("Individual Analisys", href='/individual', active="exact"),
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
    # @app.callback(
    #     Output("div-cards",'children'),
    #     [Input('date-picker', 'start_date'),
    #     Input('date-picker', 'end_date')],
    # )
    # def update_metrics(start_date,end_date):
    #     return dbc.Container()
        
    
    @app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    )
    def render_page_content(pathname):
        if pathname == "/":
            return[
                html.Div(id='div-date',children=[
                html.Div(id='div-label-date',children=['Analysis Period'],
                         style={'font-family':'Roboto, sans-serif',
                                'font-size':'25px'}
                         ),
                
                dcc.DatePickerRange(
                    id='date-picker',
                    clearable=True,
                    with_portal=True,
                    start_date = '2019-08-01',
                    end_date = '2019-10-30',
                    min_date_allowed = '2019-08-01',
                    max_date_allowed = '2019-10-30',
                    display_format = 'DD/MM/YYYY',
                    style={'color':'red'}
                )
                ],
                    #style={'border':'1px solid #d3d3d3'}
                        ),
                
                html.Div(id='div-cards',children=[
                    dbc.Container(dbc.Row(
                        [
                        dbc.Col([create_card_views(), create_card_installations(), create_card_total_days()], md=4),
                        dbc.Col([create_card_day_more_views(),create_card_day_more_downs(),create_card_average_views(),create_card_best_views_day(),create_card_worst_views_day()], md=4),
                        dbc.Col([create_card_day_less_views(),create_card_day_less_downs(),create_card_average_installs(),create_card_best_installs_day(),create_card_worst_installs_day()], md=4),
                        ]
                        )),
                ])
                
                ]
    
    return app