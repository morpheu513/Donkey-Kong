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
        self.font = pygame.font.match_font(font)

    def run(self):
        self.playing =True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

#making a new player and setting platforms
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for platform in plats:
            p = Platform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

#updating the position of the sprites
    def update(self):
        self.all_sprites.update()
        collision = pygame.sprite.spritecollide(self.player, self.platforms , False)
        if collision:
            self.player.pos.y = collision[0].rect.top + 1
            self.player.vel.y = 0
            

#drawing objects onto the screen
    def draw(self):
        self.display.fill(white)
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

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.display.blit(text_surface, text_rect)
    def key_press(self):
        wait =True
        while wait:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        wait = False
                    elif event.key == pygame.K_q:
                        wait = False
                        self.running = False
    def show_start_screen(self):
        self.display.fill(green)
        self.draw_text("Donkey Kong", fontsize, black, display_width/2, display_height/3)
        self.draw_text("Press p to play ", fontsize - 10,red, display_width/2 , display_height*0.60)
        self.draw_text("Press q to quit ", fontsize - 10,red, display_width/2 , display_height*0.75)
        pygame.display.update()
        self.key_press()
    def show_end_screen(self):
        if self.running == False:
            return
        self.display.fill(green)
        self.draw_text("GAME OVER", fontsize, black, display_width/2, display_height/3)
        self.draw_text("Press p to play again", fontsize - 10,red, display_width/2 , display_height*0.60)
        self.draw_text("Press q to quit ", fontsize - 10,red, display_width/2 , display_height*0.75)
        pygame.display.update()
        self.key_press()

g = game()
g.show_start_screen()

#game loop
while g.running:
    g.new()
    g.show_end_screen()

pygame.quit()
