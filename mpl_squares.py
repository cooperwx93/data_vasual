import matplotlib.pyplot as plt

input_value= list(range(1,6))
squares = [i**2 for i in range(1,6)]

plt.style.use('Solarize_Light2')
fig , ax = plt.subplots()  # 函数可在一张图片中绘制一个或多个图表， 变量fig表示整张图片， 变量ax表示图片中的图表
ax.plot(input_value, squares,linewidth=3)  # 通过给定的数据以有意义的方式绘制图表

ax.set_title("平方数", fontsize=24)  # 设置图表的标题
ax.set_xlabel("值", fontsize=14)  # 设置图表的横坐标
ax.set_ylabel("值的平方", fontsize=14)  # 设置图表的纵坐标

ax.tick_params(axis='both', labelsize=14)  # 设置图表刻度

plt.show() # 显示绘制的图表