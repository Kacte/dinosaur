import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import TREE, DEMON


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def random_obstacle(self):
        obstacle_type = random.choice([TREE, DEMON])

        if obstacle_type == TREE:
            self.obstacles.append(Cactus(TREE))
        elif obstacle_type == DEMON:
            self.obstacles.append(Bird(DEMON))

    def update(self, game):
        if len(self.obstacles) == 0:
            self.random_obstacle()

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset_obstacles(self):
        self.obstacles = []