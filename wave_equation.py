import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi,sin
import numpy as np

def fura(x,t):
    f=0
    for n in range(1,1000):
        f+=(4/((pi**4)*(n)**4))*sin(2*pi*(n)*t)*sin(n*pi*x)
    return f

fig,ax=plt.subplots()
x=np.linspace(0,1,500)
f2=np.vectorize(fura)

def upgrade(t):
    ax.clear()
    ax.plot(x,f2(x,t))
    ax.set_title(f"t={t}")
    ax.set_xlabel('x')
    ax.set_ylabel('U(x,t)')
    ax.set_ylim(-0.2,0.2)


animation=FuncAnimation(fig,upgrade,frames=np.linspace(0,50,300),interval=20)

plt.show()
