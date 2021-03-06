from random import *
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
        self.flag = True


#making a new player and setting up the sprites
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        self.barrels = pygame.sprite.Group()
        self.player = Player(self)
        self.donkey = Donkey(self)
        self.barrel = Barrel()
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
        self.barrels.add(self.barrel)
        self.all_sprites.add(self.barrel)


#updating the position of the sprites
    def update(self):
        self.all_sprites.update()
        collision = pygame.sprite.spritecollideany(self.player, self.platforms , False)
        if collision:

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
                    pygame.quit()
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()

    def update_rand_x(self):
        self.rand_x = randrange(0,589,100)

#functionn to draw text onto the screen
    def drawtxt(self,text,fsize,color,x,y):
        font = pygame.font.Font(font_name,fsize)
        text_surf = font.render(text,True,color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surf,text_rect)


#the start screen of the game
    def show_start_screen(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False

            self.display.fill(black)

            bcg = pygame.image.load(bg)
            self.display.blit(bcg,(0,0))
            kong = pygame.image.load(kong_start_screen)
            self.display.blit(kong,(180,320))
            self.drawtxt('Press START to begin', 30, white ,320, 560)

            mouse = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if (245+button_width) > mouse[0] > 245 and (600+button_height) > mouse[1] > 600:
                pygame.draw.rect(self.display , black ,(245,600,button_width,button_height))
                self.drawtxt('START', 35 , grey,320 , 620)
                if mouse_click[0] == 1:
                    waiting = False
            else:
                pygame.draw.rect(self.display , black ,(245,600,button_width,button_height))
                self.drawtxt('START', 35 , white,320 , 620)


            pygame.display.update()


#shows the end screen after the player dies
    def show_end_screen(self):
        waiting  = True
        while waiting:
            self.clock.tick(fps)
            self.display.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()




            kong = pygame.image.load(kong_end_screen)
            self.display.blit(kong,(200,120))
            self.drawtxt('Game Over', 40, white ,320, 560)
            mouse = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if (245+button_width) > mouse[0] > 245 and (600+button_height) > mouse[1] > 600:
                pygame.draw.rect(self.display , light_red ,(245,600,button_width,button_height))
                self.drawtxt('QUIT', 35 , black,320 , 625)
                if mouse_click[0] ==1:
                    waiting = False
                    self.running = False
            else:
                pygame.draw.rect(self.display ,red ,(245,600,button_width,button_height))
                self.drawtxt('QUIT', 35 , black,320 , 625)

            pygame.display.update()


    def win_end_screen(self):
        waiting  = True
        while waiting:
            self.clock.tick(fps)
            self.display.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()




            kong = pygame.image.load(kong_end_screen)
            self.display.blit(kong,(200,120))
            self.drawtxt('You Win', 40, white ,320, 560)
            mouse = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if (245+button_width) > mouse[0] > 245 and (600+button_height) > mouse[1] > 600:
                pygame.draw.rect(self.display , light_red ,(245,600,button_width,button_height))
                self.drawtxt('QUIT', 35 , black,320 , 625)
                if mouse_click[0] ==1:
                    waiting = False
                    self.running = False
                    self.flag = False
            else:
                pygame.draw.rect(self.display ,red ,(245,600,button_width,button_height))
                self.drawtxt('QUIT', 35 , black,320 , 625)

            pygame.display.update()





g = game()
g.show_start_screen()

#main game loop
while g.running:
    g.new()
    g.playing =True
    g.update_rand_x()
    while g.playing:
        g.clock.tick(fps)

        g.events()
        g.update()
        g.draw()
        if g.flag == True and g.playing == False :
            g.show_end_screen()

pygame.quit()
