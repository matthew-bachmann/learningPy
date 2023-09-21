import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# Make the plot look like nice
plt.style.use("mystyle")
""" plt.rcParams.update({
    "font.family": "Verdana",
    "font.weight": 500,
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "373737",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black",
    "mathtext.fontset": "cm"}) """

# A parabola paramaterized by a,b,c
def f(x,a,b,c):
    return a * x * x + b * x + c

x = np.linspace(-50,50,5000)

# Initial parameters
init_a = 1
init_b = 0
init_c = 0

# create the figure
fig, ax = plt.subplots()
rect = fig.patch
rect.set_facecolor('#3c4142')
line, = ax.plot(x,f(x,init_a,init_b,init_c), lw=3, color="#829ab1")
ax.set_title("$ax^2+bx+c$",color="white",size=18)
ax.axis([-50,50,-1000,1000])
ax.grid(True)



#make room for sliders
fig.subplots_adjust(right=0.75)

# Make a horizontal slider to control the parameter a.
a_ax = fig.add_axes([0.765, 0.65, 0.15, 0.01])
a_slider = Slider(
    ax=a_ax,
    label='$a$',
    valmin=-15,
    valmax=15,
    valinit=init_a,
    valstep=0.1
)
a_slider.label.set_position((.55,-3.2))
a_slider.label.set_size(13)

b_ax = fig.add_axes([0.765, 0.55, 0.15, 0.01])
b_slider = Slider(
    ax=b_ax,
    label='$b$',
    valmin=-100,
    valmax=100,
    valinit=init_b,
    valstep=1
)
b_slider.label.set_position((.55,-3.5))
b_slider.label.set_size(13)

c_ax = fig.add_axes([0.765, 0.45, 0.15, 0.01])
c_slider = Slider(
    ax=c_ax,
    label='$c$',
    valmin=-1000,
    valmax=1000,
    valinit=init_c,
    valstep=10
)
c_slider.label.set_position((.55,-3.2))
c_slider.label.set_size(13)


# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(x, a_slider.val,b_slider.val,c_slider.val))
    fig.canvas.draw_idle()

# register the update function with each slider
a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

plt.show()