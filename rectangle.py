import matplotlib
import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = 4*np.pi*np.sin(x)
y2 = 4/3*np.pi*np.sin(3*x)
y3 = 4/5*np.pi*np.sin(5*x)
y4 = 4/7*np.pi*np.sin(7*x)
y5 = 4/9*np.pi*np.sin(9*x)
y = np.zeros(x.size)
y_2 ,y_3, y_4, y_5= np.zeros(x.size), np.zeros(x.size), np.zeros(x.size), np.zeros(x.size)
for i in range(1, 1000):
    y += 4/(2*i-1)*np.pi*np.sin((2*i-1)*x)
for i in range(1, 2):
    y_2 += 4/(2*i-1)*np.pi*np.sin((2*i-1)*x)
for i in range(1, 5):
    y_3 += 4/(2*i-1)*np.pi*np.sin((2*i-1)*x)
for i in range(1, 10):
    y_4 += 4/(2*i-1)*np.pi*np.sin((2*i-1)*x)
for i in range(1, 50):
    y_5 += 4/(2*i-1)*np.pi*np.sin((2*i-1)*x)

mp.grid(linestyle='-.')
mp.plot(x, y, linewidth = 1)
mp.plot(x, y_2, linewidth = 1, linestyle='--')
mp.plot(x, y_3, linewidth = 1, linestyle='--')
mp.plot(x, y_4, linewidth = 1, linestyle='--')
mp.plot(x, y_5, linewidth = 1, linestyle='--')
mp.show()