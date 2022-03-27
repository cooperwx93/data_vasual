import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    high_tem,date, lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high_tem.append(int(row[5]))
        lows.append(int(row[6]))
        date.append(current_date)

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(date,high_tem, c='red',alpha=0.5)
ax.plot(date,lows, c='blue', alpha=0.5)
ax.fill_between(date,high_tem,lows,facecolor='blue', alpha=0.1)  # 

ax.set_title('2018年每日最高/最低温度', fontsize=24)
ax.set_xlabel('日期', fontsize=16,)
fig.autofmt_xdate()  # 将日期倾斜绘制
ax.set_ylabel('温度（F）', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()



