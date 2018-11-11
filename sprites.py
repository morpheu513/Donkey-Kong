import pygame
from settings import *
vector = pygame.math.Vector2
#importing the images
img_list = ['/Users/Admin/Desktop/Untitled-1.png','/Users/Admin/Desktop/Untitled-2.png','/Users/Admin/Desktop/Untitled-3.png','/Users/Admin/Desktop/Untitled-2.png']

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.images = [pygame.image.load(i) for i in img_list]
        self.image_index = 0
        self.image = self.images[self.image_index]
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (0,display_height-20)
        self.pos = pygame.math.Vector2(10,display_height-20)
        self.vel = pygame.math.Vector2(0,0)
        self.acc = pygame.math.Vector2(0,0)
#function to make the player jump
    def jump(self):
        self.rect.y += 1
        collision = pygame.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.y -= 1
        if collision:
            self.vel.y = -jump_vel
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
        if keys[pygame.K_UP]:
            self.jump()
            


        self.acc.x += self.vel.x * (friction)
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x - 10 < 0:
            self.pos.x = 10
        elif self.pos.x + 10 > display_width:
            self.pos.x = display_width - 10

        self.rect.midbottom  = self.pos
#class to create a platform
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
