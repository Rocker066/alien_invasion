import pygame


class Rocket:
    def __init__(self, bs_game):
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.image = pygame.image.load('ship_edit.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
            print(self.rect.x, self.screen_rect.right)

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
            print(self.rect.x, self.screen_rect.left)

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 1
            print(self.rect.y, self.screen_rect.top)

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
            print(self.rect.y, self.screen_rect.bottom)

    def blitme(self):
        self.screen.blit(self.image, self.rect)