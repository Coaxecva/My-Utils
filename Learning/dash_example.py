import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.graph_objs as go

import pandas
url = 'https://raw.githubusercontent.com/Coaxecva/Data-Science-Analytics-in-Python-Workshop-UoM-CS-Dept/master/data/iris.csv'
df = pandas.read_csv(url)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
	html.H1(children='Iris dataset'),
	html.Div(children='A demo of Dash (Plotly) with Iris'),
	dcc.Graph(
		id = 'iris-graph',
		figure = {
			'data': [
				go.Scatter(
					x = df[ df.Species=='setosa'].SepalWidth,
					y = df[ df.Species=='setosa'].SepalLength,
					mode = 'markers',
					name = 'setosa'
				),
			],
			'layout': go.Layout(title = 'Iris'),
		}
	),
])

if __name__ == '__main__':
	app.run_server(debug=True)