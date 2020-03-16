import matplotlib.pyplot as plt
import numpy as np
import time

x = np.linspace(0, 10*np.pi, 100)
y = np.tan(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')


for phase in np.linspace(0, 10*np.pi, 100):
	line1.set_ydata(np.sin(0.5 * x + phase))
	#line1.set_xdata(phase)
	fig.canvas.draw()
	
	#time.sleep(1)