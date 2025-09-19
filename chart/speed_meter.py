import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=65,
        title={'text':"speed"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':'darkblue'},
            'steps':[
                {'range':[0,50],'color':'lightgray'},
                {'range':[50,100],'color':'gray'}
            ],
            'threshold':{'line':{'color':"red",'width':4},'thickness':0.75,'value':80}
        }
    )
)

fig.show()

""" 
https://www.clcoding.com/

 """