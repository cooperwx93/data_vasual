import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = r'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, tmaxs, tmins = [], [], []

    for rows in reader:
        current_date = datetime.strptime(rows[2], '%Y-%m-%d')
        try:
            high = int(rows[4])
            low = int(rows[5])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            tmaxs.append(high)
            tmins.append(low)

title = '2018年死亡谷最高和最低温度表'
plt.style.use('Solarize_Light2')
fig , ax = plt.subplots()
ax.plot(dates, tmaxs, c='red', alpha=0.5)
ax.plot(dates, tmins, c='blue', alpha=0.5)
ax.fill_between(dates, tmaxs, tmins, facecolor='blue', alpha=0.1)

ax.set_title(title, fontsize=26)
ax.set_xlabel('日期', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()





