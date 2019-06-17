# -*- coding: utf-8 -*-
import dash
import dash_flexbox_grid as dfx
import dash_html_components as html
    
import json
from url_count import fake_news_accounts, counters, datelist
import dash_core_components as dcc
import dash_html_components as html
# -*- coding: utf-8 -*-
import pandas as pd
import json
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
    
app = dash.Dash('')
app.scripts.config.serve_locally = True

#------------------Get data code-------------------------


#get start and end dates
start, end = {},{}
with open('start_end.json','r') as json_file:
        news_dates= (json.load(json_file))
#print(news_dates[0])
for i in range(len(news_dates)):
    start[news_dates[i]['AccountName']] = news_dates[i]['Start']
    end[news_dates[i]['AccountName']] = news_dates[i]['End']
#print(start,end)
    
    
#get real news sources associated with fake accounts
with open('real_news.json','r') as json_file:
        news_urls= (json.load(json_file))
#print(news_urls[0])

urls = {}
for account in fake_news_accounts:
    curr_url = []
    for i in range(len(news_urls)):
        if news_urls[i]["fake account name"] == account:
            curr_url.append((news_urls[i]["URL of real websites"],news_urls[i]["Frequency"]))
            #print(curr_url)
    urls[account] = curr_url
#print(urls['TodayPittsburgh'])


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



my_css_urls = [
  "https://codepen.io/rmarren1/pen/mLqGRg.css",
]

for url in my_css_urls:
    app.css.append_css({
        "external_url": url
    })
    
fake_news_accounts = [
'NewOrleansON',
'ElPasoTopNews',
'DailySanJose',
'ChicagoDailyNew',
'DailySanFran',
'DetroitDailyNew',
'TodayCincinnati',
'MinneapolisON',
'KansasDailyNews',
'TodayBostonMA',
'TodayPittsburgh',
'Seattle_Post',
'PhiladelphiaON',
'DailyLosAngeles',
'HoustonTopNews',
'DailySanDiego',
'DallasTopNews',
'WashingtOnline',
'TodayNYCity',
'OnlineCleveland',
'SanAntoTopNews',
'PhoenixDailyNew',
'TodayMiami',
'Atlanta_Online',
'Baltimore0nline',
'OaklandOnline',
'StLouisOnline']

print(len(fake_news_accounts))
app.layout = dfx.Grid(id='grid', fluid=True, children=[
        dfx.Row(children=[
            dfx.Col(xs=12, lg=3, children=[
                html.Div(dcc.Graph(id='bar_plot2',              
              figure=go.Figure(data=[traces['NewOrleansON1'], traces['NewOrleansON2']],
                               layout=go.Layout({"title":'NewOrleansON' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])
))
    
            )), html.Div(dcc.Graph(id='bar_plot3',              
              figure=go.Figure(data=[traces['TodayNYCity1'], traces['TodayNYCity2']],
                               layout=go.Layout({"title":'TodayNYCity' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )), 
            
            html.Div(dcc.Graph(id='bar_plot6',              
              figure=go.Figure(data=[traces['Baltimore0nline1'], traces['Baltimore0nline2']],
                               layout=go.Layout({"title":'Baltimore0nline' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),
                
            ]),
            dfx.Col(xs=12, lg=3, children=[html.Div(dcc.Graph(id='bar_plot14',              
              figure=go.Figure(data=[traces['HoustonTopNews1'], traces['HoustonTopNews2']],
                               layout=go.Layout({"title":'HoustonTopNews' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot17',              
              figure=go.Figure(data=[traces['DailySanJose1'], traces['DailySanJose2']],
                               layout=go.Layout({"title":'DailySanJose' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot18',              
              figure=go.Figure(data=[traces['ChicagoDailyNew1'], traces['ChicagoDailyNew2']],
                               layout=go.Layout({"title":'ChicagoDailyNew' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))]), dfx.Col(xs=12, lg=3, children=[html.Div(dcc.Graph(id='bar_plot19',              
              figure=go.Figure(data=[traces['DailySanDiego1'], traces['DailySanDiego2']],
                               layout=go.Layout({"title":'DailySanDiego' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot20',              
              figure=go.Figure(data=[traces['DetroitDailyNew1'], traces['DetroitDailyNew2']],
                               layout=go.Layout({"title":'DetroitDailyNew' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot21',              
              figure=go.Figure(data=[traces['TodayCincinnati1'], traces['TodayCincinnati2']],
                               layout=go.Layout({"title":'TodayCincinnati' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))]), dfx.Col(xs=12, lg=3, children=[html.Div(dcc.Graph(id='bar_plot5',              
              figure=go.Figure(data=[traces['MinneapolisON1'], traces['MinneapolisON2']],
                               layout=go.Layout({"title":'MinneapolisON' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot22',              
              figure=go.Figure(data=[traces['KansasDailyNews1'], traces['KansasDailyNews2']],
                               layout=go.Layout({"title":'KansasDailyNews' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),html.Div(dcc.Graph(id='bar_plot23',              
              figure=go.Figure(data=[traces['TodayBostonMA1'], traces['TodayBostonMA2']],
                               layout=go.Layout({"title":'TodayBostonMA' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))])
        ]),dfx.Row(children=[
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot11',              
              figure=go.Figure(data=[traces['OnlineCleveland1'], traces['OnlineCleveland2']],
                               layout=go.Layout({"title":'OnlineCleveland' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot10',              
              figure=go.Figure(data=[traces['SanAntoTopNews1'], traces['SanAntoTopNews2']],
                               layout=go.Layout({"title":'SanAntoTopNews' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),#2nd column
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot7',              
              figure=go.Figure(data=[traces['Atlanta_Online1'], traces['Atlanta_Online2']],
                               layout=go.Layout({"title":'Atlanta_Online' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),
            dfx.Col(xs=12, lg=3, children=[html.Div(dcc.Graph(id='bar_plot16',              
              figure=go.Figure(data=[traces['ElPasoTopNews1'], traces['ElPasoTopNews2']],
                               layout=go.Layout({"title":'ElPasoTopNews' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))])
            
        ]),
        dfx.Row(id='row1', children=[
            dfx.Col(id='col1', xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot4',              
              figure=go.Figure(data=[traces['StLouisOnline1'], traces['StLouisOnline2']],
                               layout=go.Layout({"title":'StLouisOnline' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot9',              
              figure=go.Figure(data=[traces['PhoenixDailyNew1'], traces['PhoenixDailyNew2']],
                               layout=go.Layout({"title":'PhoenixDailyNew' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            )),),#2nd column
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot8',              
              figure=go.Figure(data=[traces['TodayMiami1'], traces['TodayMiami2']],
                               layout=go.Layout({"title":'TodayMiami' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot24',              

              figure=go.Figure(data=[traces['TodayPittsburgh1'], traces['TodayPittsburgh2']],

                               layout=go.Layout({"title":'TodayPittsburgh' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))

    

            )))
            
        ]),
        dfx.Row(id='row2', children=[
            dfx.Col(id='col2', xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot1',              
              figure=go.Figure(data=[traces['DailySanFran1'], traces['DailySanFran2']],
                               layout=go.Layout({"title":'DailySanFran' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
    ))),
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot12',              
              figure=go.Figure(data=[traces['WashingtOnline1'], traces['WashingtOnline2']],
                               layout=go.Layout({"title":'WashingtOnline' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),#2nd column
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot13',              
              figure=go.Figure(data=[traces['DallasTopNews1'], traces['DallasTopNews2']],
                               layout=go.Layout({"title":'DallasTopNews' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot25',              

              figure=go.Figure(data=[traces['Seattle_Post1'], traces['Seattle_Post2']],

                               layout=go.Layout({"title":'Seattle_Post' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))

    

            )))
            
        ]),dfx.Row(id='row5', children=[
            dfx.Col(id='lol', xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot26',              
              figure=go.Figure(data=[traces['PhiladelphiaON1'], traces['PhiladelphiaON2']],
                               layout=go.Layout({"title":'PhiladelphiaON' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
    ))),
            dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot27',              
              figure=go.Figure(data=[traces['PhiladelphiaON1'], traces['PhiladelphiaON2']],
                               layout=go.Layout({"title":'PhiladelphiaON' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))
    
            ))),#2nd column
           dfx.Col(xs=12, lg=3, children=html.Div(dcc.Graph(id='bar_plot0',              

              figure=go.Figure(data=[traces['DailyLosAngeles1'], traces['DailyLosAngeles2']],

                               layout=go.Layout({"title":'DailyLosAngeles' , "barmode":'stack'},yaxis=dict(autorange=False, range=[0, 4000])))

    

            )))
            
        ])
    ])

if __name__ == "__main__":
    app.run_server(debug=True)