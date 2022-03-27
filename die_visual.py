from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)
result = []
for roll_num in range(5000):
    result1 = die_1.roll()
    result2 = die_2.roll()
    result.append(result1 + result2)

frequencies = []
for value in range(2, die_1.num_sizes+die_2.num_sizes+1):
    frequencies.append(result.count(value))

x_value = list(range(2, die_1.num_sizes+die_2.num_sizes+1))
data = [Bar(x=x_value, y=frequencies)] # 绘制条形图数据集，需要一个存储x的列表和一个y的列表

x_axis_config = {'title':'结果', 'dtick':1}
y_axis_config= {'title':'频率'}
my_layout= Layout(title='D6_D10 5000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)  # 类Layout 返回一个指定图表布局和配置的对象
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d10.html')  # 函数offline.plot 生成图表，需要一个包含数据和布局的字典对象

