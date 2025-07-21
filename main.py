import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import Asteroid
import sys

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for thing in asteroids:
            if thing.check_collision(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        dt = pygame.time.Clock().tick(60) / 1000
        


if __name__ == "__main__":
    main()
