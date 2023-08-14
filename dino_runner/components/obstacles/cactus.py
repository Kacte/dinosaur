import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)

        if self.type in (0, 1, 2):
          self.rect.y = 375
        else:
          self.rect.y = 330