#basic game settings
display_width = 639
display_height = 730
fps = 80
acceleration = 0.5
friction = -0.12
gravity = 0.6
jump_vel = 12

#importing the images
mario_anim = ['/Users/Admin/Desktop/Untitled-1.png',
            '/Users/Admin/Desktop/Untitled-2.png',
            '/Users/Admin/Desktop/Untitled-3.png',
            '/Users/Admin/Desktop/Untitled-2.png']

#platform images
plat_path = ['/Users/Admin/Desktop/Platforms/ground.png',
             '/Users/Admin/Desktop/Platforms/above ground.png',
             '/Users/Admin/Desktop/Platforms/below mid-left.png',
             '/Users/Admin/Desktop/Platforms/below mid-mid.png',
             '/Users/Admin/Desktop/Platforms/below mid-right.png',
             '/Users/Admin/Desktop/Platforms/Middle.png',
             '/Users/Admin/Desktop/Platforms/above ground.png',
             '/Users/Admin/Desktop/Platforms/below mid-right.png']


#non-sprites
ladder = ['/Users/Admin/Desktop/Platforms/ladder.png']
big_ladder = ['/Users/Admin/Desktop/Platforms/big ladder.png']
mesh = ['/Users/Admin/Desktop/Platforms/mesh.png']

#locations of platforms(x-co-ordinate,y-co-ordinate)
plats = [(0,display_height-19),
     (3.5,display_height-130),
     (5,display_height-224),
     (192,display_height-224),
     (494,display_height-224),
     (0,display_height-345),
         (3.5,display_height-446),
         (330,display_height-551)]
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
