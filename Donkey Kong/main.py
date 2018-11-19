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
        self.playing = True

    '''def run(self):
        self.playing =True
        while self.playing:
            self.clock.tick(fps)
            self.x = random.randint(0,539)
            #print("printing rand value",self.x)
            self.events()
            self.update()
            self.draw()'''

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
    #    self.run()

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


    def drawtxt(self,text,fsize,color,x,y):
        font = pygame.font.Font(font_name,fsize)
        text_surf = font.render(text,True,color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surf,text_rect)

    def show_start_screen(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False
            self.display.fill(black)
            self.drawtxt("Donkey Kong" , 80 , grey, 319 , 100)

            mouse = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if (245+button_width) > mouse[0] > 245 and (550+button_height) > mouse[1] > 550:
                pygame.draw.rect(self.display , grey ,(245,550,button_width,button_height))
                if mouse_click[0] == 1:
                    waiting = False
            else:
                pygame.draw.rect(self.display , white ,(245,550,button_width,button_height))

            self.drawtxt('START', 20 , black,320 , 570)
            pygame.display.update()

    def show_end_screen(self):
        pass

g = game()
g.show_start_screen()

#game loop
while g.running:
    g.new()
    g.playing =True
    while g.playing:
        g.clock.tick(fps)
        g.x = random.randint(0,539)
        #print("printing rand value",self.x)
        g.events()
        g.update()
        g.draw()
    g.show_end_screen()

pygame.quit()
