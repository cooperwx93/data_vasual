import  matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('Solarize_Light2')
    fig, ax = plt.subplots(figsize=(15,9),dpi=128)
    point_number = range(rw.number)
    ax.scatter(rw.x_value, rw.y_value,c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.scatter(0,0,c='green',s=100, edgecolors='none')
    ax.scatter(rw.x_value[-1], rw.y_value[-1],c='red', edgecolors='none', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    keep_running = input('make another walk?(y/n):')
    if keep_running == 'n':
        break

    plt.show()