import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

from heatmap.helper import geojosn_loader, load_dataset

token = open("../.mapbox_token").read()  # you will need your own token

df = load_dataset('data.csv')
# geojson = geojosn_loader('georef-germany-gemeinde.geojson')
geojson = geojosn_loader('gemeinden_simplify0 (1).geojson')

fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson,
    locations=df.key,
    z=df.value,
    featureidkey="properties.RS_0",
    marker_opacity=0.5,
    zmin=0))
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=4.5,
    mapbox_center={"lat": 51.11, "lon": 10.36},
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox_accesstoken=token)

app = dash.Dash(__name__)

app.layout = html.Div([
    # html.P("Candidate:"),
    dcc.Graph(figure=fig),
])

app.run_server(debug=True)
