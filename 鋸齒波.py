import matplotlib
import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(-1*np.pi, 1*np.pi, 1000)
y1 = (-2/np.pi)*(np.sin(2*np.pi*1*x)/1)#第一個正弦波
y2 = (2/np.pi)*(np.sin(2*np.pi*2*x)/2)#第二個正弦波
y3 = (-2/np.pi)*(np.sin(2*np.pi*3*x)/3)#第三個正弦波
y4 = (2/np.pi)*(np.sin(2*np.pi*4*x)/4)#第四個正弦波
y5 = (-2/np.pi)*(np.sin(2*np.pi*5*x)/5)#第五個正弦波

y = np.zeros(x.size)
y_2 ,y_3, y_4, y_5= np.zeros(x.size), np.zeros(x.size), np.zeros(x.size), np.zeros(x.size)

for i in range(1, 1000):
    y += (2/np.pi)*(np.power(-1,i)/i)*np.sin(2*np.pi*i*x)

for i in range(1, 2):
    y_2 += (2/np.pi)*(np.power(-1,i)/i)*np.sin(2*np.pi*i*x)    

for i in range(1, 3):
    y_3 += (2/np.pi)*(np.power(-1,i)/i)*np.sin(2*np.pi*i*x)

for i in range(1, 4):
    y_4 += (2/np.pi)*(np.power(-1,i)/i)*np.sin(2*np.pi*i*x)

for i in range(1, 5):
    y_5 += (2/np.pi)*(np.power(-1,i)/i)*np.sin(2*np.pi*i*x)

mp.grid(linestyle='-.')
mp.plot(x, y, linewidth = 1)
mp.plot(x, y_2, linewidth = 1, linestyle='--')
mp.plot(x, y_3, linewidth = 1, linestyle='--')
mp.plot(x, y_4, linewidth = 1, linestyle='--')
mp.plot(x, y_5, linewidth = 1, linestyle='--')
mp.show()