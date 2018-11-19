##import os
#basic game settings
display_width = 639
display_height = 700
fps = 60
acceleration = 0.5
friction = -0.12
gravity = 0.6
jump_vel = 7
font_name = 'freesansbold.ttf'
#generallizing path
##for roots,dirs,files in os.walk('E:\\'):
##    if 'Donkey Kong' in dirs:
##        f_path = os.path.split(os.path.abspath(dirs[dirs.index('Donkey Kong')]))[0]
#button sizes
button_width = 150
button_height = 40



#Mario images
mario_anim = ['..\\Donkey Kong\\Assets\\Mario\\Untitled-1.png',
            '..\\Donkey Kong\\Assets\\Mario\\Untitled-2.png',
            '..\\Donkey Kong\\Assets\\Mario\\Untitled-3.png',
            '..\\Donkey Kong\\Assets\\Mario\\Untitled-2.png']
climb_path = ['..\\Donkey Kong\\Assets\\Mario\\Climb-1.png',
              '..\\Donkey Kong\\Assets\\Mario\\Climb-2.png']

#Donkey images
donkey_path = '..\\Donkey Kong\\Assets\\Donkey\\without barrel.png'
               #'..\\Donkey Kong\\Assets\\Donkey\\with barrel.png',
               #'..\\Donkey Kong\\Assets\\Donkey\\left_pick.png',
               #'..\\Donkey Kong\\Assets\\Donkey\\right_pick.png']

#Barrel images
barrel_path = ['..\\Donkey Kong\\Assets\\Donkey\\barrel.png',
               '..\\Donkey Kong\\Assets\\Donkey\\barrel_rolled.png']

#platform images
plat_path = ['..\\Donkey Kong\\Assets\\Platforms\\ground.png',
             '..\\Donkey Kong\\Assets\\Platforms\\above ground.png',
             '..\\Donkey Kong\\Assets\\Platforms\\below mid-left.png',
             '..\\Donkey Kong\\Assets\\Platforms\\below mid-mid.png',
             '..\\Donkey Kong\\Assets\\Platforms\\below mid-right.png',
             '..\\Donkey Kong\\Assets\\Platforms\\Middle.png',
             '..\\Donkey Kong\\Assets\\Platforms\\above ground.png',
             '..\\Donkey Kong\\Assets\\Platforms\\below mid-right.png']

#ladder co-ordinates
ladds = [(500,display_height-109),
         (58,display_height-220),
         (600,display_height-337),
         (117,display_height-455)]

#non-sprites
big_ladder = ['..\\Donkey Kong\\Assets\\Platforms\\big ladder.png']
mesh = ['..\\Donkey Kong\\Assets\\Platforms\\mesh.png']

#locations of platforms(x-co-ordinate,y-co-ordinate)
plats = [(0,display_height-19),
     (3.5,display_height-140),
     (5,display_height-244),
     (180,display_height-244),
     (494,display_height-244),
     (0,display_height-375),
         (3.5,display_height-486),
         (330,display_height-601)]
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (155,155,155)
