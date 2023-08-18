import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.freeze import Freeze
from dino_runner.utils.constants import SHIELD, FREEZE, FREEZE_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def random_power(self):
        power_type = random.choice([SHIELD, FREEZE])
        if power_type == SHIELD:
            self.power_ups.append(Shield())
        elif power_type == FREEZE:
            self.power_ups.append(Freeze())

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(300, 400)
            self.random_power()

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                self.sound = pygame.mixer.Sound("dinosaur/dino_runner/assets/Music/smw_power-up.wav")
                self.sound.play()
                if power_up == SHIELD:
                    game.player.shield = True
                elif power_up == FREEZE:
                    game.player.freeze = True
                game.player.type = power_up.type
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
        if game.player.type == FREEZE_TYPE:
            game.game_speed = 25

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(300, 400)
