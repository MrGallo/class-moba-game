from typing import List
from .unit import Hero
from .team import Team

import pygame
from pygame.locals import KEYDOWN, K_w, K_a, K_s, K_d


class View:
    """A pseudo-interface for views that can be used in the game class."""

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        """View-specific event loop for key-bindings"""
        raise NotImplementedError("You need to override the 'event_loop' method in every class inheriting from the View class.")

    def update(self) -> None:
        """Update the view's state"""
        raise NotImplementedError("You need to override the 'update' method in every class inheriting from the View class.")
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the view's contents."""
        raise NotImplementedError("You need to override the 'draw' method in every class inheriting from the View class.")



class Battle(View):
    def __init__(self):

        self.player_controlled_hero = Hero(200, 10, 20, 400, 10, Team(), Team(), (pygame.Rect(590,310,100,100)))

        self.background = pygame.image.load('league\\images\\background.png')
        self.player_surface = pygame.Surface((2400, 5120), pygame.SRCALPHA)
        self.player_surface_movement = (0,0)

        # taken from png properties
        self.BACKGROUND_WIDTH = 2400
        self.BACKGROUND_HEIGHT = 5120
        self.BACKGROUND_SIZE = (self.BACKGROUND_WIDTH, self.BACKGROUND_HEIGHT)

        # Grid variables
        pygame.font.init()

        self.font = pygame.font.SysFont('Calibri', 50)

        self.ROWS = 20
        self.COLUMNS = 5

        self.cell_width = self.BACKGROUND_WIDTH // self.COLUMNS
        self.cell_height = self.BACKGROUND_HEIGHT // self.ROWS


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == KEYDOWN:
                print(event)


    def update(self, screen) -> None:
        # need background mask not screen

        keys_pressed = pygame.key.get_pressed()
        self.player_surface_movement = self.player_controlled_hero.update(screen, self.player_surface_movement, keys_pressed)

    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0,0,0))
        self.player_surface.fill((255,255,255,0))

        self._draw_grid()

        window = self._cropped_background_surface(screen, self.background)

        # draw background and player
        pygame.draw.rect(self.player_surface, (255,0,0), self.player_controlled_hero.get_rect())
        screen.blit(window, (0,0))
        screen.blit(self.player_surface, self.player_surface_movement)


    def _cropped_background_surface(self, screen: pygame.Surface, background: pygame.Surface):
        """Creates a crop of the background to use on screen.
        
        Args:
            screen: Surface that is used for the game screen size.
            background: Full surface containing the entire background.
        
        Returns:
            A cropped background surface to draw as the screen window.
        """

        # DOES NOT WORK PROPERLY YET
        # MOVES FASTER WHEN SCREEN MOVES
        # POSSIBLY DUE TO BLITTING SURFACES ON SCREEN WHICH CHANGES POSITIONS

        player_x = self.player_controlled_hero.get_rect().x
        player_y = self.player_controlled_hero.get_rect().y
        # player_center = self.player_controlled_hero.get_rect().center
        player_size = self.player_controlled_hero.get_rect().size
        player_center_x = player_x + (player_size[0] // 2)
        player_center_y = player_y + (player_size[1] // 2)

        screen_rect = screen.get_rect().copy()

        if player_center_x < screen_rect.center[0]:
            new_val_x = screen_rect.center[0]
        elif player_center_x > self.BACKGROUND_WIDTH - (screen_rect.center[0]):
            new_val_x = self.BACKGROUND_WIDTH - (screen_rect.center[0])
        else:
            new_val_x = player_center_x
        
        if player_center_y < screen_rect.center[1]:
            new_val_y = screen_rect.center[1]
        elif player_center_y > self.BACKGROUND_HEIGHT - (screen_rect.center[1]):
            new_val_y = self.BACKGROUND_HEIGHT - (screen_rect.center[1])
        else:
            new_val_y = player_center_y

        screen_rect.center = (player_center_x, player_center_y)
        screen_rect.__setattr__('center', (new_val_x, new_val_y))

        background_subsurface = background.subsurface(screen_rect)

        return background_subsurface


    def _draw_grid(self):
        """Draws a grid on the background."""

        for x in range(0, self.BACKGROUND_WIDTH, self.cell_width):
            pygame.draw.line(self.background, (128,128,128), (x,0), (x, self.BACKGROUND_HEIGHT), 1)

        for y in range(0, self.BACKGROUND_HEIGHT, self.cell_height):
            pygame.draw.line(self.background, (128,128,128), (0,y), (self.BACKGROUND_WIDTH, y), 1)

        # add labels to each cell
        row_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i, x in enumerate(range(0, self.BACKGROUND_WIDTH, self.cell_width)):
            for j, y in enumerate(range(0, self.BACKGROUND_HEIGHT, self.cell_height)):
                text = row_letters[j] + str(i)

                grid_text = self.font.render(text, True, (0, 0, 255))
                self.background.blit(grid_text, (x, y))