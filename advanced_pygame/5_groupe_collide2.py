import pygame
from pygame.sprite import Sprite
import random


class Game:
    """The game class"""

    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        self.check_collisions()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)


class Monster(Sprite):
    """A simple class to represent a spooky monster"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('blue_monster.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """Update and move the monster"""
        self.rect.y += self.velocity


class Knight(Sprite):
    """A simple class to represent a spooky monster"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """Update and move the monster"""
        self.rect.y -= self.velocity


class KnightFight:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set display surface
        self.WIDTH = 800
        self.HEIGHT = 600
        self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Group Collide!')
        self.running = True

        # Set FPS and clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Create monster group
        self.my_monster_group = pygame.sprite.Group()
        for i in range(12):
            monster = Monster(i * 64, 10)
            self.my_monster_group.add(monster)

        # Create knight group
        self.my_knight_group = pygame.sprite.Group()
        for i in range(12):
            knight = Knight(i * 64, self.HEIGHT - 64)
            self.my_knight_group.add(knight)

        # Instantiate the game object
        self.game = Game(self.my_monster_group, self.my_knight_group)


    def run_game(self):
        # The main game loop
        while self.running:
            for event in pygame.event.get():
                self._check_events(event)

            # check for collision
            self.game.update()

            # Update the display and draw assets
            self._update_display()


    def _check_events(self, event):
        if event.type == pygame.QUIT:
            self.running = False


    def _update_display(self):
        # Fill the display
        self.display_surface.fill((0, 0, 0))

        # Update and draw sprite groups
        self.my_monster_group.update()
        self.my_monster_group.draw(self.display_surface)

        self.my_knight_group.update()
        self.my_knight_group.draw(self.display_surface)

        # Update the display and tick the clock
        pygame.display.flip()
        self.clock.tick(self.FPS)


if __name__ == '__main__':
    kf = KnightFight()
    kf.run_game()
