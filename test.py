import pyglet
from pyglet import image

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
bg = pyglet.graphics.Group(order=0)
characters = pyglet.graphics.Group(order=1)

bf = pyglet.image.load('images/characters/PixelBF.png')
bf_anim = pyglet.sprite.Sprite(bf, batch = batch, group = characters)

text = pyglet.text.Label('Hello World',
	font_name = 'Times New Roman',
	font_size = 30,
	x=10, y=10,
	anchor_x = 'center', anchor_y = 'center')
	
@window.event
def on_draw():
	window.clear()
	label.draw()

pyglet.app.run()


