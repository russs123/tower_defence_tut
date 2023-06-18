import pygame as pg
import json
from enemy import Enemy
from world import World
import constants as c

#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#load images
#map
map_image = pg.image.load('levels/level.png').convert_alpha()
#enemies
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

#load json data for level
with open('levels/level.tmj') as file:
  world_data = json.load(file)

#create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

#game loop
run = True
while run:

  clock.tick(c.FPS)

  screen.fill("grey100")

  #draw level
  world.draw(screen)

  #update groups
  enemy_group.update()

  #draw groups
  enemy_group.draw(screen)

  #event handler
  for event in pg.event.get():
    #quit program
    if event.type == pg.QUIT:
      run = False

  #update display
  pg.display.flip()

pg.quit()