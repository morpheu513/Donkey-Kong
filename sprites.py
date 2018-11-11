import pygame
from settings import *
vector = pygame.math.Vector2
plat_list = [pygame.image.load(i) for i in plat_path]

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
##        self.rect.y += 1
##        collision = pygame.sprite.spritecollide(self,self.game.platforms,False)
##        self.rect.y -= 1
##        if collision:
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
