# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#from bar_chart.py import datelist,counterNoFURLs, counterFURLs
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from url_count import fake_news_accounts, counters, datelist

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#trying to get newsName from the destination url 



#traces for the stack bar


trace1 = go.Bar(
        x=datelist,
        y=counters['NewOrleansON'],
        name='with URLs'
    )
trace2 = go.Bar(
        x=datelist,
        y=counters['NewOrleansON'],
        name='without URLs'
    )


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[trace1, trace2],
                               layout=go.Layout(barmode='stack'))
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    #
    
        
'''
    labels = 'WithURLs','WithoutURLs'
    trace1 = go.Bar(
        x=datelist,
        y=counterFURLs,
        name='with URLs'
    )
    trace2 = go.Bar(
        x=datelist,
        y=counterNoFURLs,
        name='without URLs'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='stack'
    )
    layout = go.Layout(
    yaxis=dict(
            range=[0, 5000]
        )
    )
    fig = go.Figure(data=data, layout=layout)
    iplot(fig, filename='stacked-bar')
 '''
