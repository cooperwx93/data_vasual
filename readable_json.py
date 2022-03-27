import json
import plotly.express as px  # plotly的高级接口
import pandas as pd

filename = r'eq_data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dict = all_eq_data['features']
mags,titles, lons, lats = [], [],[], []
for num in all_eq_dict:
    mags.append(num["properties"]['mag'])
    titles.append(num["properties"]['title'])
    lons.append(num["geometry"]["coordinates"][0])
    lats.append(num["geometry"]["coordinates"][1])
data = pd.DataFrame(
    data=zip(lons, lats, titles,mags), columns=['经度', '纬度', '位置', '震级']
)
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x':'纬度', 'y':'经度'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',

)
fig.write_html('global_earthquakes.html')
fig.show()


