import pyglet # import the library
import util
win= pyglet.window.Window() # create the window

# Create a sprite
img= pyglet.image.load('characters.png')
smol_img = img.get_region(x=0, y=0, width=25, height=16)
spr= pyglet.sprite.Sprite(smol_img, x = 200, y = 200)

the= pyglet.image.load('sheet.png')
smol_the = the.get_region(x=128, y=96, width=32, height=16)
#two = pyglet.sprite.Sprite(smol_the, x = 200, y = 200)

he= pyglet.image.load('parallax-mountain-bg.png')
smol_he = he.get_region(x=0, y=0, width=270, height=160)
bg = pyglet.sprite.Sprite(smol_he, 0, 0)
bg.scale = 3
#two = pyglet.sprite.Sprite(smol_the, x = 200, y = 200)
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
  win.push_handlers(keys)
  if keys[pyglet.window.key.LEFT]:
    spr.x -= 1
  if keys[pyglet.window.key.RIGHT]:

    spr.x += 1
  if keys[pyglet.window.key.DOWN]:
    spr.y -= 1
  if keys[pyglet.window.key.UP]:
    spr.y += 1

# Start the event loop
@win.event
def on_draw():
  util.pixelScale()
  win.clear()
  bg.draw()
  spr.draw()
  smol_the.blit(0,150)
  smol_the.blit(32,150)
  smol_the.blit(64,150)
  smol_the.blit(96,150)
  smol_the.blit(128,150)
  smol_the.blit(160,150)
  smol_the.blit(192,150)
  smol_the.blit(224,150)
  smol_the.blit(256,150)
  smol_the.blit(288,150)
  smol_the.blit(320,150)
  smol_the.blit(352,150)
  smol_the.blit(384,150)
  smol_the.blit(416,150)
  smol_the.blit(448,150)
  smol_the.blit(480,150)
  smol_the.blit(544,150)
  smol_the.blit(576,150)
  smol_the.blit(608,150)
  smol_the.blit(640,150)
  smol_the.blit(672,150)
  smol_the.blit(704,150)
  spr.draw()
  
  #two.draw()



pyglet.clock.schedule(update) 
pyglet.app.run()