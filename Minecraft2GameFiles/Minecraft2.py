#Warning this code is shit!
#Bugs are a Feature now!
#Mod if you want.
#LOL
#sus
#https://github.com/thunderbolt1003usa
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import choice 
from ursina.shaders import lit_with_shadows_shader
#import pygame
window.vsync = False
window.borderless = False
app = Ursina(icon= "mc22.ico",
             title= "Minecraft2",
             borderless= False,
             development_mode= False,
                        
             )

scene.fog_density = 0.1

#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load("Beast.mp3")
#pygame.mixer.music.play(-1)

grass = load_texture('grass.jpg')
stein = load_texture('stein.jpg')
dirt = load_texture('dirt.png')
wood = load_texture('wood.png')
lol = load_texture('lol.png')
lol2 = load_texture('lol2.png')
mc2 = load_texture('mc2.png')
fenster = load_texture('Fenster.png')
stern = load_texture('stern.png')
lol3 = load_texture('error.png')
water = load_texture('water.png')
lava = load_texture('lava.png')
rainbow = load_texture('rainbow.png')

tür = load_texture('tür.png')
magic = load_texture('magic.png')
magic2 = load_texture('magic2.png')
magic3 = load_texture('magic3.png')
red = load_texture('red.png')
blue = load_texture('blue.png')

#nugget = load_model('nugget.obj')

player = FirstPersonController()
player.gravity = 0.5
gun = Button(parent=camera, model='cube', color=color.black, position=(3,0,3), collider='box', scale=(.1,.1,1))
gun.parent = camera
gun.position = Vec3(.5,-.2,.5)

Sky()

textures = [grass, dirt]
boxes = []
random_texture = choice(textures)

def add_box(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=random_texture
)
 )

def add_wood(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=wood
)
 )

def add_grass(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=grass
)
 )

def add_dirt(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=dirt
)
 )

def add_stone(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=stein
)
 )

def add_lol(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=lol
)
 )

def add_lol2(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=lol2
)
 )

def add_mc2(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=mc2
)
 )

def add_fenster(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=fenster
)
 )

def add_stern(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=stern
)
 )

def add_lol3(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=lol3
)
 )

def add_water(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=water
)
 )

def add_lava(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=lava
)
 )

def add_rainbow(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=rainbow
)
 )

def add_brick(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.red,
    position=position,
    texture='brick'
)
 )

def add_chest(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=tür
)
 )


def add_magic(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=magic
)
 )

def add_magic2(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=magic2
)
 )

def add_magic3(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=magic3
)
 )

def add_red(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=red
)
 )

def add_blue(position):
 boxes.append(
   Button(
    parent=scene,
    model='cube',
    origin=2.0,
    color=color.white,
    position=position,
    texture=blue
)
 )

for x in range(25):
   for y in range(25):
    for z in range(3):
         add_box( (x,z,y) )

def input(key):
    if key == "tab":
               if scene.fog_density == 0.1:
                scene.fog_density = 0
               else:
                scene.fog_density = 0.1
    
    if key == "backspace":
               player.position = (5,30,5)
    if key == "space":
               player.gravity = 0.5
    if key == "scroll up":
               player.mouse_sensitivity += Vec2(1,1)
    if key == "scroll down":
               player.mouse_sensitivity -= Vec2(1,1)
    if key == "right mouse down":
               bullet = Entity(parent=gun, model='cube', scale=.1, color=color.yellow)
               bullet.world_parent = scene
               bullet.animate_position(bullet.position+(bullet.forward*400), curve=curve.linear, duration=1)
               destroy(bullet, delay=1)
    for box in boxes:
        if box.hovered:
            
            if key == "middle mouse down":
               add_box(box.position + mouse.normal)   
            if key == "left mouse down":
                  boxes.remove(box)
                  destroy(box)
            if key == "1":
               add_wood(box.position + mouse.normal), 
            if key == "2":
               add_stone(box.position + mouse.normal) 
            if key == "3":
               add_fenster(box.position + mouse.normal)   
            if key == "4":
               add_grass(box.position + mouse.normal)  
            if key == "5":
               add_dirt(box.position + mouse.normal)   
            if key == "6":
               add_lol2(box.position + mouse.normal)       
            if key == "7":
               add_lol(box.position + mouse.normal)
            if key == "8":
               add_stern(box.position + mouse.normal)   
            if key == "9":
               add_lol3(box.position + mouse.normal)  
            if key == "e":
               add_water(box.position + mouse.normal)  
            if key == "q":
               add_lava(box.position + mouse.normal) 
            if key == "0":
               add_rainbow(box.position + mouse.normal)
            if key == "r":
               add_brick(box.position + mouse.normal)
            if key == "f":
               add_chest(box.position + mouse.normal)  
            if key == "c":
               add_magic(box.position + mouse.normal) 
            if key == "v":
               add_magic2(box.position + mouse.normal)
            if key == "b":
               add_magic3(box.position + mouse.normal)
            if key == "t":
               add_red(box.position + mouse.normal)
            if key == "g":
               add_blue(box.position + mouse.normal)
            
               
            





def update():
  

  if held_keys['control']:
    player.speed = 10
    player.jump_height = 3
  else:
    player.speed = 5
    player.jump_height = 1.5

  if held_keys['up arrow']:
   player.gravity = 0 
   player.y += 0.2
  if held_keys['down arrow']: 
   player.gravity = 0
   player.y -= 0.2

app.run() 