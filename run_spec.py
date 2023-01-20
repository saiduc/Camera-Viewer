from instrument_control.spectrometer import *
import matplotlib.pyplot as plt 
import numpy as np
from scipy.signal import savgol_filter as sg
from matplotlib.animation import FuncAnimation

spectrometer = Spectrometer("chamber").initiate()
tlim = spectrometer.get_timelim()
spectrometer.set_time(1e6)

def ave_spec(no_rep, spec):
    all_x = []
    all_y = []
    for i in range(no_rep):
        x, y = spec.get_spec()
        all_x.append(x)
        all_y.append(y)
    return np.mean(np.array(all_x),axis=0), np.mean(np.array(all_y),axis=0)

fig, ax = plt.subplots()
bg_x, bg_y = ave_spec(1, spectrometer)
line, = ax.semilogy(bg_x,bg_y)
# ax.set_xlim(530,700)
ax.set_ylim(1e-6,1e4)
ax.set_title('Time limits are {}'.format(tlim))

def update(i):
    x, y = ave_spec(1, spectrometer)
    line.set_data(x,sg(y-bg_y,51,3))
    # ax.set_ylim(min(y-bg_y), max(y-bg_y))
    return line

ani = FuncAnimation(plt.gcf(), update, frames=range(100), interval=5, blit=False)

plt.show()
