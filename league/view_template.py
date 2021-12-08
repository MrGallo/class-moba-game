from typing import List

import pygame

from league.base_view import BaseView

# CHANGE THE CLASS NAME MyView to something more specific
class MyView(BaseView):
    def event_loop(self, events: List[pygame.event.Event]) -> None:
        pass    

    def update(self) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((0, 0, 200))
