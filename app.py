import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objects as go 
import dash_daq as daq
import pandas as pd
import plotly.graph_objects as go

"""graphs"""
df1 = pd.read_csv('https://raw.githubusercontent.com/uiy123/covData/master/covdata.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/uiy123/covData/master/rigions.csv')
tda = []
tee = []
tt = []
re = []
de = []
def enc(t, l):
    for i in t:
        if i == 0 :
            l.append(None)
        else:
            l.append(i)

enc(df1.date, tda)
enc(df1.total_effected, tee)
enc(df1.recovered, re)
enc(df1.death, de)
enc(df1.total_tests, tt)
ae = []
for i in df1.active:
    ae.append(i)
maxact = max(ae)
minact = min(ae)
fig= go.Figure()
fig.add_trace(go.Scatter(x= tda, y= ae, name= 'ac'))
fig.add_trace(go.Scatter(x= tda, y= tee, name= 't eff'))
fig.add_trace(go.Scatter(x= tda, y= re, name= 'rec'))
fig.add_trace(go.Scatter(x= tda, y= de, name= 'dea'))
fig.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                    "hovermode": "x",
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "legend_orientation":"h",
                    "xaxis": dict(
                                showline=False,
                                showgrid=True,
                                zeroline=False,
                                showticklabels=False,)
                })
fig.update_traces(mode="markers+lines")
sos = []
bni = []
dra = []
casa = []
da = []
fas =[]
gl = []
lay = []
mra = []
ori = []
rb = []
tan = []
def data(target, l):
    for i in target:
        l.append(i)
data(df2.BeniMellal_Khénifra, bni)
data(df2.souss_massa, sos)
data(df2.Casa_Settat, casa)
data(df2.Daraa_tafilalet, dra)
data(df2.Dakhla_Oued_EdDahab, da)
data(df2.Fès_meknes, fas)
data(df2.Guelmim_OuedNoun, gl)
data(df2.Laâyoune_Sakia_ElHamra, lay)
data(df2.Marrakech_Safi, mra)
data(df2.Oriental, ori)
data(df2.Rabat_SaléKenitra, rb)
data(df2.TangerTetouan_AlHoceima, tan)
def newCases(l):
    
    if l[-1] == l[-2]:
        return f'(0 cases for {l.count(l[-1])}days)'
    else:
        return f'(+{l[-1]-l[-2]})'
labels = [f'BeniMellal_Khénifra {newCases(bni)}', f'Casa_Settat {newCases(casa)}', f'souss_massa {newCases(sos)}', f'TangerTetouan_AlHoceima {newCases(tan)}', f'Rabat_SaléKenitra {newCases(rb)} ', f'Oriental {newCases(ori)}', f'Daraa_tafilalet {newCases(dra)}', f'Dakhla_Oued_EdDahab {newCases(da)}', f'Fès_meknes {newCases(fas)}', f'Guelmim_OuedNoun {newCases(gl)}', f'Marrakech_Safi {newCases(mra)}', f'Laâyoune_Sakia_ElHamra {newCases(lay)}']       
values = [bni[-1], casa[-1], sos[-1], tan[-1], rb[-1], ori[-1], dra[-1], da[-1], fas[-1], gl[-1], mra[-1], lay[-1] ]
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label',insidetextorientation='radial', textposition='inside')])
fig2.update_layout(showlegend=False)
fig2.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                })
fig3 = go.Figure(data=[go.Pie(labels=[i for i in df1.columns if i[0] == 'a'or i[0] == 'r' or i[0:2]=='de'], values=[ae[-1], re[-1], de[-1]], textinfo='percent+label',insidetextorientation='radial', textposition='inside', hole=.3)])
fig3.update_layout(showlegend=False)
fig3.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                })



app = dash.Dash(meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
app.title = 'Covid-19'

#functions
def title(title):
    return html.Div(className="section-banner", children=title)
def value(v, d):
    c = ''
    if int(d) > 0:
        c = 'red'
    elif int(d) <= 0:
        c='green'
    
    return html.P(className='value-holder', children=[html.Div(className='value', children=v),html.Div(className=c, children=d)] )
def recov(v, d):
    c = ''
    if int(d) > 0:
        c = 'green'
    elif int(d) <= 0:
        c='red'
    
    return html.P(className='value-holder', children=[html.Div(className='value', children=v),html.Div(className=c, children=d)] )
    dcc.Graph(
        id='sparkline_graph_id',
        style={"width": "100%", "height": "95%"},
        config={
            "staticPlot": False,
            "editable": False,
            "displayModeBar": False,
        },
        figure=fig,
        
            
            
        
    ),


#banner
banner = html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("COVID-19 OVERVIEW"),
                    html.P("Data from official sources"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.A(
                        id="learn-more-button", children="Collab", href='#'
                    ),
                ],
            ),
        ],
    )


app.layout = html.Div(
    id="big-app-container",
    children=[
        banner,
        html.Div(
            id="app-container",
            children=[
                
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className='three columns flex',
                            children=[
                                title('Total Actives'),
                                value(ae[-1], -15),

                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total effected'),
                                value(tee[-1], 15)
                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total recovered'),
                                recov(re[-1], 54)
                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total death'),
                                value(de[-1], 0)
                            ]
                        ),
                    ]
                ),
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className='twelve columns',
                            children=[title('Overview')]),
                        html.Div(
                            className='twelve columns',
                            children=[
                                title('Overview'),
                                dcc.Graph(
                                    id='sparkline_graph_id',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig,
                                ),
                                

                            ]
                        )
                    ]
                ),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='six columns',
                            children=[
                                title('Rigions'),
                                dcc.Graph(
                                    id='rigions',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig2,
                                ),
                                
                            ]
                        ),
                        html.Div(
                            className='six columns flex',
                            children=[
                                title('Today'),
                                dcc.Graph(
                                    id='today',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig3,
                                ),
                            ]
                        ),
                    ]   
                ),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='twelve columns',
                            children=[
                                html.P('something here')
                            ], style ={'text-align':'center'}
                        )
                    ]
                )
            ]
            )
    ],
)
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
