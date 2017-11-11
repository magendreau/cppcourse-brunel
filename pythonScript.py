import numpy as np
import matplotlib.pyplot as pl

fig = pl.figure()

ax1 = fig.add_subplot(211)
data = np.genfromtxt('spikes.gdf')

select= np.array([d for d in data if d[1] < 30])
data1= select.transpose()
pl.scatter(0.1*data1[0],data1[1],alpha=0.8, edgecolors='none');
ax1.set_xlim([400, 500])

select2= np.array([d for d in data])
data2= select2.transpose()
ax2 = fig.add_subplot(212)
n, bins, patches = ax2.hist(0.1*data2[0], 1000, normed=0, alpha=0.75)
ax2.set_xlim([400, 500])
ax2.set_ylim([0, 800])
pl.show();
