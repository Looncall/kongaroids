import pyglet
from pyglet.window import key
from pong_kong import Kong
from paddle import Paddle

window = pyglet.window.Window()
kong_image = pyglet.resource.image('King-Kong-psd24860.png')
paddle_image = pyglet.resource.image('empire_state_building.jpg')

key_states = key.KeyStateHandler()
window.push_handlers(key_states)

kong = Kong(window, key_states, kong_image)
paddleA = Paddle(window, key_states, paddle_image, 'A')
paddleB = Paddle(window, key_states, paddle_image, 'B')

@window.event
def on_draw():
	window.clear()
	paddleA.draw()
	paddleB.draw()
	kong.draw()

def update(dt):
	a_position = paddleA.update()
	b_position = paddleB.update()
	kong.update(dt, a_position, b_position)

pyglet.clock.schedule_interval(update, 1/120)
pyglet.app.run()