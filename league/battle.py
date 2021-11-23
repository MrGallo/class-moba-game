from typing import List

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d


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
        # Centering player
        self.pos_x = 1280 // 2 # width // 2
        self.pos_y = 720 // 2 # height // 2

        # Player data (should be given from Unit)
        self.speed = 30
        self.PLAYER_RADIUS = 50

        # starting position for player (based on map position)
        self.map_pos_x = -100
        self.map_pos_y = 100

        self.map = pygame.image.load('league\\images\\map.png')

        # taken from png properties
        self.MAP_WIDTH = 2403
        self.MAP_HEIGHT = 5120
        self.MAP_SIZE = (self.MAP_WIDTH, self.MAP_HEIGHT)

        # Grid variables
        pygame.font.init()

        self.font = pygame.font.SysFont('Calibri', 50)

        self.ROWS = 20
        self.COLUMNS = 5

        self.cell_width = self.MAP_WIDTH // self.COLUMNS
        self.cell_height = self.MAP_HEIGHT // self.ROWS


    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == KEYDOWN:
                print(event)


    def update(self, screen) -> None:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_d]:
            color = screen.get_at((self.pos_x + self.PLAYER_RADIUS + 1, self.pos_y))
            if self.pos_x < self.MAP_WIDTH and color != (0,0,0,255): # should check for blue and red team?
                self.map_pos_x -= self.speed
        
        if keys_pressed[K_a]:
            color = screen.get_at((self.pos_x - self.PLAYER_RADIUS - 1, self.pos_y))
            if self.pos_x > 0 and color != (0,0,0,255):
                self.map_pos_x += self.speed

        if keys_pressed[K_s]:
            color = screen.get_at((self.pos_x, self.pos_y + self.PLAYER_RADIUS + 1))
            if self.pos_y < self.MAP_HEIGHT and color != (0,0,0,255):
                self.map_pos_y -= self.speed

        if keys_pressed[K_w]:
            color = screen.get_at((self.pos_x, self.pos_y - self.PLAYER_RADIUS - 1))
            if self.pos_y > 0 and color != (0,0,0,255):
                self.map_pos_y += self.speed
        
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0,0,0))

        # draw grid
        for x in range(0, self.MAP_WIDTH, self.cell_width):
            pygame.draw.line(self.map, (128,128,128), (x,0), (x, self.MAP_HEIGHT), 1)

        for y in range(0, self.MAP_HEIGHT, self.cell_height):
            pygame.draw.line(self.map, (128,128,128), (0,y), (self.MAP_WIDTH, y), 1)

        # add labels to each cell
        row_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i, x in enumerate(range(0, self.MAP_WIDTH, self.cell_width)):
            for j, y in enumerate(range(0, self.MAP_HEIGHT, self.cell_height)):
                text = row_letters[j] + str(i)

                grid_text = self.font.render(text, True, (0, 0, 255))
                self.map.blit(grid_text, (x, y))

        # draw map and player
        screen.blit(self.map, (self.map_pos_x,self.map_pos_y))
        pygame.draw.circle(screen, (255,0,0), (self.pos_x, self.pos_y), self.PLAYER_RADIUS) # "Player" circle (centered)
