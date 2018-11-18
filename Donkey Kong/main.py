import pygame
import random
from settings import *
from sprites import *


class game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption("Donkey Kong")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        self.playing =True
        while self.playing:
            self.clock.tick(fps)
            self.x = random.randint(0,539)
            print("printing rand value",self.x)
            self.events()
            self.update()
            self.draw()

#making a new player and setting platforms
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        self.player = Player(self)
        self.donkey = Donkey(self)
        for i in range(len(plats)):
            p = Platform(i,*plats[i])
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(len(ladds)):
            l = Ladder(*ladds[i])
            self.all_sprites.add(l)
            self.ladders.add(l)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.donkey)
        self.run()

#updating the position of the sprites
    def update(self):
        self.all_sprites.update()
        collision = pygame.sprite.spritecollideany(self.player, self.platforms , False)
        if collision:
##            if collision.rect.top >= self.player.rect.bottom:
            self.player.pos.y = collision.rect.top + 1
            self.player.vel.y = 0
#drawing objects onto the screen
    def draw(self):
        self.display.fill(black)
        self.display.blit(barrel_pile,(3.5,display_height-586))
        self.all_sprites.draw(self.display)
        pygame.display.update()

#handling the events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()
##            collision = pygame.sprite.spritecollideany(self.player,self.ladders,False)
##            if collision:
##                self.player.acc = vector(0,0)
##                if event.type == pygame.KEYDOWN:
##                    if event.key == pygame.K_UP:
##                        self.player.climb('up')
##                    if event.key == pygame.K_DOWN:
##                        self.player.climb('down')
##            else:
##                self.player.acc = vector(0,gravity)
            #self.acc = vector(0, gravity)
    def show_start_screen(self):
        pass
    def show_end_screen(self):
        pass

g = game()
g.show_start_screen()

#game loop
while g.running:
    g.new()
    g.show_end_screen()

pygame.quit()
