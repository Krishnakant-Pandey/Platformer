import pygame as pg
from game_variables import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((player_width, player_height))
        self.image.fill(green)
        self.rect = self.image.get_rect(center=(screen_width/2, screen_height/2))
        self.pos = vec(screen_width/2, screen_height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.y += 3
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 3

        if hits :
            self.vel.y = -player_jump

    def update(self):
        self.acc = vec(0, 0.5)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -player_acc
        if keys[pg.K_RIGHT]:
            self.acc.x = +player_acc

        # forcing a terminal velocity
        self.acc.x += self.vel.x*friction
        self.acc.y += self.vel.y*air_resistance

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        # limiting the motion to the visible screen (Note : don't use ' >= ' or ' <= ')
        # including equality creates a problem because first if statement teleport block to x = screen_width
        # But instantly the next if statement acts and second statement keeps it at screen_width
        if self.pos.x < 0:
            self.pos.x = screen_width
        if self.pos.x > screen_width:
            self.pos.x = 0

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(red)
        self.rect = self.image.get_rect(topleft=(x, y))
