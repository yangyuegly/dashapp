# -*- coding: utf-8 -*-
import dash
import pandas as pd
import json
import flask
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import render_template
#from bar_chart.py import datelist,counterNoFURLs, counterFURLs
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from url_count import fake_news_accounts, counters, datelist

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#trying to get newsName from the destination url 
app = flask.Flask(__name__)

#get start and end dates
start, end = {},{}
with open('start_end.json','r') as json_file:
        news_dates= (json.load(json_file))
print(news_dates[0])
for i in range(len(news_dates)):
    start[news_dates[i]['AccountName']] = news_dates[i]['Start']
    end[news_dates[i]['AccountName']] = news_dates[i]['End']
    
    
#get real news sources associated with fake accounts
with open('real_news.json','r') as json_file:
        news_urls= (json.load(json_file))
print(news_urls[0])

urls = {}
for account in fake_news_accounts:
    curr_url = []
    for i in range(len(news_urls)):
        if news_urls[i]["fake account name"] == account:
            curr_url.append((news_urls[i]["URL of real websites"],news_urls[i]["Frequency"]))
            #print(curr_url)
    urls[account] = curr_url
#print(urls['TodayPittsburgh'])




@app.route('/home')
def homepage():
    title = "IRA Twitter Research"
    return render_template("account.html", title = title)


@app.route('/<some_fake_account>')
def account_page(some_fake_account):
    return render_template("account.html", title = some_fake_account, start_date = start[some_fake_account], end_date = end[some_fake_account],urls=urls[some_fake_account])

#corresponding account information 



app = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix='/dash/'
)


individual_page_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),

])



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
