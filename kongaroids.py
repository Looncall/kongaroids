import pyglet
from pyglet.window import key
from astroids_kong import Kong

window = pyglet.window.Window()
image = pyglet.resource.image('King-Kong-psd24860.png')

key_states = key.KeyStateHandler()
window.push_handlers(key_states)
SPEED = 200

kong = Kong(window, key_states, image)

@window.event
def on_draw():
	window.clear()
	kong.draw()

def update(dt):
	kong.update(dt)

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()