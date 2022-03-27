import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = r'data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, tmax, tmin = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = round(int((row[8])))
            low = round(int((row[9])))
        except ValueError:
            print(f"Missing data {current_date}.")
        else:
            dates.append(current_date)
            tmax.append(high)
            tmin.append((low))

title = '2018全年死亡谷最高/最低温度表'
plt.style.use('Solarize_Light2')
fig , ax = plt.subplots()
ax.plot(dates,tmax,c='red',alpha=0.5)
ax.plot(dates,tmin,c='blue',alpha=0.5)
ax.fill_between(dates,tmax,tmin,facecolor='blue',alpha=0.1)

ax.set_title(title, fontsize=26)
ax.set_xlabel('日期', fontsize=16)
ax.set_ylabel('温度', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
