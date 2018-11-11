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
        #if pygame.sprite.collide_rect(
        collision = pygame.sprite.spritecollideany(self.player, self.platforms , False)
        if collision:
            self.player.pos.y = collision.rect.top + 1
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
