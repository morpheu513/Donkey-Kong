import pygame
from settings import *
import random
import time
vector = pygame.math.Vector2
plat_list = [pygame.image.load(i) for i in plat_path]
climb_list = [pygame.image.load(i) for i in climb_path]
ladder = pygame.image.load('..\\Donkey Kong\\Assets\\Platforms\\ladder.png')
donkey_list = [pygame.image.load(i) for i in donkey_path]
barrel_pile = pygame.image.load('..\\Donkey Kong\\Assets\\Donkey\\barrel_pile.png')
#player class
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.images = [pygame.image.load(i) for i in mario_anim]
        self.image_index = 0
        self.image = self.images[self.image_index]
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (22,display_height-40)
        self.pos = pygame.math.Vector2(22,display_height-40)
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
#function to make the player jump
    def jump(self):
        self.rect.y += 1
        collision = pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.y -= 1
        if collision:
            self.vel.y = -jump_vel

#climbing the ladder
    def climb(self,check):
       # self.acc.y = 0
        count = 0
        if check == 'up':
            if count<fps//8:
                count+=1
                self.acc.y=-0.01
                self.image = climb_list[count//5]
            else:
                count = 0
        else:
            if count<fps//8:
                count+=1
                self.acc.y=+0.01
                self.image = climb_list[count//5]
            else:
                count = 0

#updating the co-ordinates of the player
    def update(self):
        self.acc = vector(0, gravity)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            temp = [pygame.transform.flip(image, True, False) for image in self.images]
            self.acc.x = -acceleration
            self.image_index+=1
            if self.image_index<fps//2:
                self.image = temp[self.image_index//10]
            else:
                self.image_index = 0
        if keys[pygame.K_RIGHT]:
            temp = self.images
            self.acc.x = acceleration
            self.image_index+=1
            if self.image_index<fps//2:
                self.image = temp[self.image_index//10]
            else:
                self.image_index = 0
        collision = pygame.sprite.spritecollideany(self,self.game.ladders,False)
        if collision:
            self.acc.y = 0
            if keys[pygame.K_UP]:
                self.climb('up')
            if keys[pygame.K_DOWN]:
                self.climb('down')

        self.acc.x += self.vel.x * (friction)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x - 22 < 0:
            self.pos.x = 22
        elif self.pos.x + 22 > display_width:
            self.pos.x = display_width - 22


        self.rect.midbottom  = self.pos

#class to create a platform
class Platform(pygame.sprite.Sprite):
    def __init__(self,index,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = plat_list[index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#class to create Ladders
class Ladder(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ladder
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#class to create Donkey
class Donkey(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image_index = 0
        self.image = donkey_list[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = display_width/2 - 50
        self.rect.bottom = display_height-486
        self.pos = pygame.math.Vector2(display_width/2,display_height-486)
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
    def update(self):
        #acc = [-acceleration,+acceleration]
        #x = random.randint(0,539)
        if self.image == donkey_list[0]:
            self.acc.x = -acceleration
            if self.rect.left < 155.5:
                self.acc.x = 0
##                self.image = donkey_list[2]
##                time.sleep(2)
                self.image = donkey_list[1]
        else:
            self.acc.x = ((self.game.x-self.rect.x)/(abs(self.game.x-self.rect.x)+1))*acceleration
            if self.acc.x == 0:
                #self.throw()
                print("Hey")

        self.acc.x += self.vel.x * (friction)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom  = self.pos
##    def throw(self):
