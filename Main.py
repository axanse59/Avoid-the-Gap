import pyglet # import the library
import util
import random

win= pyglet.window.Window() # create the window
# Create a sprite
img= pyglet.image.load('characters.png')
smol_img = img.get_region(x=0, y=0, width=25, height=16)
spr= pyglet.sprite.Sprite(smol_img, x = 200, y = 300)

tt= pyglet.image.load('sheet.png')
smol_tt = tt.get_region(x=128, y=96, width=32, height=16)
the = pyglet.sprite.Sprite(smol_tt, x = 0, y = 300)

he= pyglet.image.load('parallax-mountain-bg.png')
smol_he = he.get_region(x=0, y=0, width=270, height=160)
bg = pyglet.sprite.Sprite(smol_he, 0, 0)
bg.scale = 3
#two = pyglet.sprite.Sprite(smol_the, x = 200, y = 200)
keys = pyglet.window.key.KeyStateHandler()
hit = False

def makeBlock():
  ss= pyglet.image.load('sheet.png')
  img = ss.get_region(x=128, y=96, width=32, height=16)
  b = pyglet.sprite.Sprite(img, x = random.randint(0,20)*32, y = 200)
  return b

blocks = []

for i in range(20):
  blocks.append(makeBlock())





def update(dt):
  global hit
  win.push_handlers(keys)
  print(str(hit))   
  if spr.x >= 600:
    hit = True
    move = True

  if spr.x <= 0:
    hit = False
  
  

  for b in blocks:
    if spr.x < b.x + 32 and spr.x > b.x and spr.y < b.y + 16 and spr.y > b.x:
      print("Hey")

  if keys[pyglet.window.key.SPACE]:
    if hit:
      spr.x -= 8
    else:
      spr.x += 8

  # two.y += 4
  # if two.y > 480:
  #   two.y = 0
  #   two.x = random.randint(0,800)
  for b in blocks:
    b.y += 4
    if b.y > 480:
      b.y = 0
      b.x = random.randint(0, 20) * 32


  # if keys[pyglet.window.key.LEFT]:
  #   spr.x -= 1
  # if keys[pyglet.window.key.RIGHT]:

  #   spr.x += 1
  # if keys[pyglet.window.key.DOWN]:
  #   spr.y -= 1
  # if keys[pyglet.window.key.UP]:
  #   spr.y += 1

# Start the event loop
@win.event
def on_draw():
  util.pixelScale()
  win.clear()
  bg.draw()
  spr.draw()
  the.draw()
  #smol_the.blit(0,150)
  # smol_the.blit(32,150)
  # smol_the.blit(64,150)
  # smol_the.blit(96,150)
  # smol_the.blit(128,150)
  # smol_the.blit(160,150)
  # smol_the.blit(192,150)
  # smol_the.blit(224,150)
  # smol_the.blit(256,150)
  # smol_the.blit(288,150)
  # smol_the.blit(320,150)
  # smol_the.blit(352,150)
  # smol_the.blit(384,150)
  # smol_the.blit(416,150)
  # smol_the.blit(448,150)
  # smol_the.blit(480,150)
  # smol_the.blit(544,150)
  # smol_the.blit(576,150)
  # smol_the.blit(608,150)
  # smol_the.blit(640,150)
  # smol_the.blit(672,150)
  # smol_the.blit(704,150)
  for b in blocks:
    b.draw()
  
  #two.draw()
  spr.draw()

  #two.draw()
pyglet.clock.schedule(update) 
pyglet.app.run()
