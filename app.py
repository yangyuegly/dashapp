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

traces ={}
for news in fake_news_accounts:
    traces[news+str(1)] = go.Bar(
        x=datelist,
        y=counters[news][0],
        name='with URLs'
    )
    traces[news+str(2)] = go.Bar(
        x=datelist,
        y=counters[news][1],
        name='without URLs'
    )

#html and graph components

app.layout = html.Div([
    html.H1('Fake Twitter Username'),

    html.Div(children='''
        Select a fake twitter account to view the number of tweets that contains urls vs the number of ones that don't
    '''),
    html.Div(
    [
            dcc.Dropdown(
                id="AccountNames",
                options=[{
                    'label': i,
                    'value': i
                } for i in fake_news_accounts],
                value='NewOrleansON'),
    ],
    style={'width': '25%',
               'display': 'inline-block'}),
    

    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=[traces['NewOrleansON1'], traces['NewOrleansON2']],
                               layout=go.Layout(barmode='stack'))
    
    )
])


#updating 
@app.callback(
    dash.dependencies.Output('bar_plot', 'figure'),
    [dash.dependencies.Input('AccountNames', 'value')])
def update_output(value):
    return {
            #dcc.Graph(id='bar_plot',
            'data':[traces[value+str(1)], traces[value+str(1)]],
            'layout':
                go.Layout(barmode='stack')

        #)    
    }
        
    

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
