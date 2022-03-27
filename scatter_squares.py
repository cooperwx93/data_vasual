import matplotlib.pyplot as plt

x_value = list(range(1,1000))
y_value = [i**2 for i in x_value]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# 颜色映射的网址 https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
#cmaps = [('Perceptually Uniform Sequential', [
         #    'viridis', 'plasma', 'inferno', 'magma', 'cividis']),
         # ('Sequential', [
         #    'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
         #    'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
         #    'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']),
         # ('Sequential (2)', [
         #    'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
         #    'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
         #    'hot', 'afmhot', 'gist_heat', 'copper']),
         # ('Diverging', [
         #    'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
         #    'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']),
         # ('Cyclic', ['twilight', 'twilight_shifted', 'hsv']),
         # ('Qualitative', [
         #    'Pastel1', 'Pastel2', 'Paired', 'Accent',
         #    'Dark2', 'Set1', 'Set2', 'Set3',
         #    'tab10', 'tab20', 'tab20b', 'tab20c']),
         # ('Miscellaneous', [
         #    'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
         #    'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
         #    'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
         #    'gist_ncar'])]
ax.scatter(x_value,y_value, c=y_value, cmap=plt.cm.viridis, s=10)

ax.set_title('平方数', fontsize=24)
ax.set_xlabel('值', fontsize=14)
ax.set_ylabel('值的平方', fontsize=14)

ax.tick_params(axis='both', which='major',labelsize=14) # which : 可选{‘major’, ‘minor’, ‘both’} 选择对主or副坐标轴进行操作

ax.axis([0,1001, 0, 1000001])

plt.show()