import numpy as np
import math
import pandas as pd
import openpyxl as oxl
import matplotlib.pyplot as plt
from PIL import Image
import time
# WYKRESY I LEJBELE
# a = np.arange(666)
# b = a**2
# c = np.arange(40)
# d = c*(3)
# e = np.arange(40)
# f = e
# plt.plot(a , b, 'ro')
# plt.plot(c, d, 'go')
# plt.plot(e, f, 'bo')
# plt.axis([0, 40, 0, 150])
# plt.legend(labels=['kwadratowa', 'szescienna', 'liniowa'])
# plt.xlabel('iksy')
# plt.ylabel('igreki')
# plt.title('wynagrodzenie')
# plt.savefig('obrazek.jpg')
# otworz = pil.image.open()
# plt.show()
# SINUS
# for i in range(0,100):
#     a = np.arange(0,10.1, 0.1)
#     b =np.sin(a)
#     plt.plot(a , b, 'r-')
#     plt.axis([0, 10, -1, 1])
#     plt.legend(labels=['sinus x'])
#     plt.xlabel('x')
#     plt.ylabel('sin(x)')
#     plt.title('Sinus')
#     plt.show()
#     a = np.arange(0,10.1, 0.1)
#     b =np.sin(a)
#     plt.plot(a , b, 'b-')
#     plt.axis([0, 10, -1, 1])
#     plt.legend(labels=['sinus x'])
#     plt.xlabel('x')
#     plt.ylabel('sin(x)')
#     plt.title('Sinus')
#     plt.show()
# KROPKI
# data = {'a':np.arange(50),
#         'c':np.random.randint(0, 50, 50),
#         'd':np.random.randn(50)}
# data['b']=data['a'] +10*np.random.randn(50)
# data['d']=np.abs(data['d'])*453
# plt.scatter('a', 'b', c='c', s= 'd', data=data)
# plt.title('costam')
# plt.axis([0, 50, 0, 80])
# plt.show()
# PLOTS
# a = np.arange(0, 10.1, 0.1)
# c = np.arange(0, 10.1, 0.1)
# e = np.arange(0, 10.1, 0.1)
# b =np.sin(a)
# d =np.tan(c)
# f = e*3
# x = np.arange(0, 10.1, 0.1)
# y = np.cos(x)
# plt.subplot(4, 1, 1)
# plt.plot(a , b, 'r-')
# plt.axis([0, 10, -1, 1])
# plt.legend(labels=['sinus x'])
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sinus')
#
# plt.subplot(4,1,2)
# plt.plot(x, y, 'b-')
# plt.subplots_adjust( hspace=2)
#
#
# plt.subplot(4, 1, 3)
# plt.plot(c , d, 'g-')
# plt.axis([0, 10, -1, 1])
# plt.legend(labels=['sinus x'])
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sinus')
#
# plt.subplot(4, 1, 4)
# plt.plot(e , f, 'c-')
# plt.axis([0, 10, -1, 1])
# plt.legend(labels=['sinus x'])
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sinus')
# plt.show()
# x1 = np.arange(0,30)
# y1 = np.sin(x1)
# y2 = x1*2
# y3 = np.sqrt(x1)
# y4 = x1**2
# y5 = np.cos(x1)
# y6 = np.tan(x1)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, 'g-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('y')
# axs[0, 0].set_title('ajdin')
#
# axs[1, 0].plot(x1, y6, 'g-')
# axs[1, 0].set_xlabel('x')
# axs[1, 0].set_ylabel('y')
# axs[1, 0].set_title('cwaj')
#
# axs[2, 0].plot(x1, y2, 'g-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('y')
# axs[2, 0].set_title('draj')
#
# axs[1, 1].plot(x1, y3, 'g-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('y')
# axs[1, 1].set_title('cztery')
# #
# axs[0, 1].plot(x1, y4, 'g-')
# axs[0, 1].set_xlabel('x')
# axs[0, 1].set_ylabel('y')
# axs[0, 1].set_title('siedem')
#
# axs[2, 1].plot(x1, y5, 'g-')
# axs[0, 1].set_xlabel('x')
# axs[0, 1].set_ylabel('y')
# axs[0, 1].set_title('szesc')
#
# fig.delaxes(axs[2, 0])
# plt.show()
# barowe
# data = {'Kraj':['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica':['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent':['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja':[124234, 235235, 121411, 151361]}
# df = pd.DataFrame(data)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
# plt.bar(etykiety, wartosc, color=['gold', 'orange', 'yellow'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja w mld')
# plt.show()

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
ts.plot()
plt.show()

grupa = df.groupby('Kontynent').agg({'Populacja w mld'})

