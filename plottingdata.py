import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plt.style.use("mystyle")

# intial weights
init_w11 = .9
init_w12 = .1
init_w21 = .1
init_w22 = .9

np.random.seed(19680801)

x_axis = np.linspace(-2,102,100)
x = np.random.random(100)*100
y = np.random.random(100)*100

# A line with weights
def f(x,w11,w12,w21,w22):
    if w22==w12:
        return [0]*100
    elif w22<w12:
        return (((w11-w21)/-(w22-w12))*x)
    else:
        return (((w11-w21)/(w22-w12))*x)

# col = np.where(x<50,'#829ab1',np.where(y<50,'#CF6679','k'))
col = np.where((y<(-.1*((x-50)*(x-50)) + 75)),'#00008b','r')

regions = f(x_axis,init_w11,init_w12,init_w21,init_w22)

fig, ax = plt.subplots()
ax.scatter(x,y, c=col)
ax.set_title('Random Binary Data', color="white")
ax.axis([-2,102,-2,102])
ax.grid(True,alpha=.2)
line, = ax.plot(x_axis,f(x_axis,init_w11,init_w12,init_w21,init_w22), lw=3, color="#825b97")
b = ax.fill_between(x_axis,regions,102,
                color='#0047ab', alpha=0.15)
r = ax.fill_between(x_axis,regions,
                color='#D22B2b', alpha=0.15)


#make room for sliders
fig.subplots_adjust(right=0.75)

# Make a horizontal slider to control the parameter a.
w11_ax = fig.add_axes([0.765, 0.65, 0.15, 0.01])
w11_slider = Slider(
    ax=w11_ax,
    label='$w_{11}$',
    valmin=-1,
    valmax=1,
    valinit=init_w11,
    valstep=0.1
)
w11_slider.label.set_position((.55,-3.2))
w11_slider.label.set_size(13)

w12_ax = fig.add_axes([0.765, 0.55, 0.15, 0.01])
w12_slider = Slider(
    ax=w12_ax,
    label='$w_{12}$',
    valmin=-1,
    valmax=1,
    valinit=init_w12,
    valstep=0.1
)
w12_slider.label.set_position((.55,-3.2))
w12_slider.label.set_size(13)

w21_ax = fig.add_axes([0.765, 0.45, 0.15, 0.01])
w21_slider = Slider(
    ax=w21_ax,
    label='$w_{21}$',
    valmin=-1,
    valmax=1,
    valinit=init_w21,
    valstep=0.1
)
w21_slider.label.set_position((.55,-3.2))
w21_slider.label.set_size(13)

w22_ax = fig.add_axes([0.765, 0.35, 0.15, 0.01])
w22_slider = Slider(
    ax=w22_ax,
    label='$w_{22}$',
    valmin=-1,
    valmax=1,
    valinit=init_w22,
    valstep=0.1
)
w22_slider.label.set_position((.55,-3.2))
w22_slider.label.set_size(13)


# The function to be called anytime a slider's value changes
def update(val):
    global r
    r.remove()
    global b
    b.remove()
    regions = f(x_axis,w11_slider.val,w12_slider.val,w21_slider.val,w22_slider.val)
    r = ax.fill_between(x_axis,regions,102,
                color='#0047ab', alpha=0.15)
    b = ax.fill_between(x_axis,regions,
                color='#D22B2B', alpha=0.15)
    line.set_ydata(f(x_axis, w11_slider.val,w12_slider.val,w21_slider.val,w22_slider.val))
    fig.canvas.draw_idle()

# register the update function with each slider
w11_slider.on_changed(update)
w12_slider.on_changed(update)
w21_slider.on_changed(update)
w22_slider.on_changed(update)


plt.show()

