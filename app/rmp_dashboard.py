import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from backend import BackEndDashboard
import plotly.express as px
import datetime

def init_app(server):
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
    app = dash.Dash(
        __name__, 
        suppress_callback_exceptions=True,
        title="Rank My App Challenge - João Victor Magalhães Souza",
        server=server,
        
        external_stylesheets=[dbc.themes.CERULEAN,dbc.themes.BOOTSTRAP, FONT_AWESOME]
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
        dados = backend.get_best_view_day(start_date,end_date)
        card_best_views_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Best views day', className="card-title"),
                        html.P(f'{datetime.datetime.strptime(dados[0][0:10],"%Y-%m-%d").strftime("%d/%m/%Y")}: {dados[1]} views', className="card-text",),
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
        dados = backend.get_worst_view_day(start_date,end_date)
        card_worst_views_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Worst views day', className="card-title"),
                        html.P(f'{datetime.datetime.strptime(dados[0][0:10],"%Y-%m-%d").strftime("%d/%m/%Y")}: {dados[1]} views', className="card-text",),
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
        dados = backend.get_best_installs_day(start_date,end_date)
        card_best_installs_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Best installs day', className="card-title"),
                        html.P(f'{datetime.datetime.strptime(dados[0][0:10],"%Y-%m-%d").strftime("%d/%m/%Y")}: {dados[1]} installs', className="card-text",),
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
        dados = backend.get_worst_installs_day(start_date,end_date)
        card_worst_installs_day = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Worst installs day', className="card-title"),
                        html.P(f'{datetime.datetime.strptime(dados[0][0:10],"%Y-%m-%d").strftime("%d/%m/%Y")}: {dados[1]} installs', className="card-text",),
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
    
    def create_card_visitors_day(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Total visitors', className="card-title"),
                        html.P(f'{backend.get_visitors_day(date)} visitors', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-eye", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card
    
    def create_card_installs_day(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Total installs', className="card-title"),
                        html.P(f'{backend.get_installs_day(date)} installs', className="card-text",),
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
        
        return card

    def create_card_week_day_correspondent(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Referred Week Day', className="card-title"),
                        html.P(f'{backend.get_referent_week_day(date)}', className="card-text",),
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
        
        return card
    
    def create_card_percentage_visitors_installs(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('% Visit. that installs', className="card-title"),
                        html.P(f'{backend.get_percentage_visitors_installs(date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-percent", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card

    def create_card_retained_1d(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Installs retained 1d', className="card-title"),
                        html.P(f'{backend.get_retained_1d(date)}', className="card-text",),
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
        
        return card

    def create_card_retained_1d_rate(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('% Installs retained 1d', className="card-title"),
                        html.P(f'{backend.get_retained_1d_rate(date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-percent", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card
    
    def create_card_retained_7d(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Installs retained 7d', className="card-title"),
                        html.P(f'{backend.get_retained_7d(date)}', className="card-text",),
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
        
        return card

    def create_card_retained_7d_rate(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('% Installs retained 7d', className="card-title"),
                        html.P(f'{backend.get_retained_7d_rate(date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-percent", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card
    
    def create_card_retained_30d(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('Installs retained 30d', className="card-title"),
                        html.P(f'{backend.get_retained_30d(date)}', className="card-text",),
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
        
        return card

    def create_card_retained_30d_rate(date='2019-08-01'):
        card = dbc.CardGroup(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H5('% Installs retained 30d', className="card-title"),
                        html.P(f'{backend.get_retained_30d_rate(date)}', className="card-text",),
                    ]
                )
            ),
            dbc.Card(
                html.Div(className="fa fa-percent", style=card_icon),
                className="bg-info",
                style={"maxWidth": 75},
            ),
        ],className="mt-4 shadow",
        )
        
        return card
    
    
    
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
    
   

    @app.callback(
        Output("div-cards",'children'),
        Output("scatter",'figure'),
        Output("barplot1", 'figure'),
        Output("barplot2", 'figure'),
        [Input('date-picker', 'start_date'),
        Input('date-picker', 'end_date')],
    )
    def update_metrics(start_date,end_date):
        # print(f"Start: {start_date}")
        # print(f'End: {end_date}')
        df = backend.get_dataframe_graph1(start_date,end_date)
        dados2 = backend.get_dataframe_graph2(start_date, end_date)
        dados3 = backend.get_dataframe_graph3(start_date, end_date)
        return (dbc.Container(dbc.Row(
                        [
                        dbc.Col([create_card_views(start_date,end_date), create_card_installations(start_date,end_date),create_card_average_views(start_date,end_date),create_card_best_installs_day(start_date,end_date)], md=4),
                        dbc.Col([create_card_day_more_views(start_date,end_date),create_card_day_more_downs(start_date,end_date),create_card_average_installs(start_date,end_date),create_card_worst_views_day(start_date,end_date)], md=4),
                        dbc.Col([create_card_day_less_views(start_date,end_date),create_card_day_less_downs(start_date,end_date),create_card_best_views_day(start_date,end_date),create_card_worst_installs_day(start_date,end_date)], md=4),
                        ]
                        )),px.scatter(df,y='Installers',x='Store Listing Visitors',color='Referent Week Day',
                        title='Relation between Visitors x Installers x Week Day').update_layout({
                                                                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                                                    }),
                        px.bar(dados2,x=dados2.index,y='Store Listing Visitors',
                    title='Comparisson between accum. visitors in week days'
                ).update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    }),
                    px.bar(dados3,x=dados3.index,y='Installers',
                    title='Comparisson between accum. installs in week days'
                ).update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    }),
                    
                    )
                        
                        
    
    @app.callback(
        Output('div-individual-cards','children'),
        Input('date-single', 'date'),
        
    )
    def update_individual_metrics(date):
        return dbc.Container(dbc.Row(
                        [
                        dbc.Col([create_card_visitors_day(date),create_card_percentage_visitors_installs(date),create_card_retained_7d(date)], md=4),
                        dbc.Col([create_card_installs_day(date),create_card_retained_1d(date),create_card_retained_7d_rate(date),create_card_retained_30d_rate(date)], md=4),
                        dbc.Col([create_card_week_day_correspondent(date),create_card_retained_1d_rate(date),create_card_retained_30d(date)], md=4),
                        ]
                        ))
        
    
    @app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    )
    def render_page_content(pathname):
        if pathname == "/":
            dados = backend.get_dataframe_graph1()
            dados2 = backend.get_dataframe_graph2()
            dados3 = backend.get_dataframe_graph3()
            return[
                html.Div(id='div-date',children=[
                html.Div(id='div-label-date',children=['Analize a period'],
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
                        dbc.Col([create_card_views(), create_card_installations(),create_card_average_views(),create_card_best_installs_day()], md=4),
                        dbc.Col([create_card_day_more_views(),create_card_day_more_downs(),create_card_average_installs(),create_card_worst_views_day()], md=4),
                        dbc.Col([create_card_day_less_views(),create_card_day_less_downs(),create_card_best_views_day(),create_card_worst_installs_day()], md=4),
                        ]
                        )),
                    
                ]),
                dcc.Graph(id='scatter',figure=px.scatter(dados,
                        y='Installers',x='Store Listing Visitors',color='Referent Week Day',
                        title='Relation between Visitors x Installers x Week Day'
                    ).update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    })),
                dcc.Graph(id='barplot1',figure=px.bar(dados2,x=dados2.index,y='Store Listing Visitors',
                    title='Comparisson between accum. visitors in week days'
                ).update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    })),
                dcc.Graph(id='barplot2',figure=px.bar(dados3,x=dados3.index,y='Installers',
                    title='Comparisson between accum. installs in week days'
                ).update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                    }))
            ]
        elif pathname=='/individual':
            return [
                html.Div(id='div-individual-date',children=[
                html.Div(id='div-label-date',children=['Analize a day'],
                         style={'font-family':'Roboto, sans-serif',
                                'font-size':'25px'}
                         ),
                
                dcc.DatePickerSingle(
                    id='date-single',
                    clearable=True,
                    with_portal=True,
                    date = '2019-08-01',
                    min_date_allowed = '2019-08-01',
                    max_date_allowed = '2019-10-30',
                    display_format = 'DD/MM/YYYY',
                )
                ],
                    #style={'border':'1px solid #d3d3d3'}
                        ),
                html.Div(id='div-individual-cards',children=[
                    dbc.Container(dbc.Row(
                        [
                        dbc.Col([create_card_visitors_day(),create_card_percentage_visitors_installs(),create_card_retained_7d()], md=4),
                        dbc.Col([create_card_installs_day(),create_card_retained_1d(),create_card_retained_7d_rate(),create_card_retained_30d_rate()], md=4),
                        dbc.Col([create_card_week_day_correspondent(),create_card_retained_1d_rate(),create_card_retained_30d()], md=4),
                        ]
                        )),
                    
                ])


            ]

                
    
    return app