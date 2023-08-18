import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, LOGO, DEFAULT_TYPE, BG2, SHIELD_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import text_utils



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
    
    def execute(self):
        self.running = True
        while self.running:
            self.music()
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.game_speed = 20
        self.score = 0
        self.player.type = DEFAULT_TYPE
        self.player.power_up_time = 0
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def music(self):
        if self.running:
            pygame.mixer.init() 
            pygame.mixer.music.load("dinosaur/dino_runner/assets/Music/fundo.mp3")
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 3
        self.update_high_score()

    def update_high_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        text_utils(f"Score: {self.score}",
                   self.screen,
                   text_color=(0, 0, 0),
                   pos_x_center=970,
                   pos_y_center=50
                   )
        text_utils(f"High score: {self.high_score}",
                   self.screen,
                   text_color=(0, 0, 0),
                   pos_x_center=945,
                   pos_y_center=80
                   )

    def draw_power_up_time(self):
        if self.player.type == SHIELD_TYPE:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show >= 0:
                text_utils(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_menu(self):
        self.screen.blit(BG2, (0, 0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.blit(LOGO, (half_screen_width - 100, half_screen_height - 50))
            text_utils("Press any key to start",
                   self.screen,
                   pos_x_center=half_screen_width,
                   pos_y_center=half_screen_height + 200
                   )

        else:
            self.screen.blit(LOGO, (half_screen_width - 100, half_screen_height - 50))
            text_utils("Press any key to restart",
                   self.screen,
                   pos_x_center=half_screen_width,
                   pos_y_center=half_screen_height + 240
                   )
            text_utils(f"Score: {self.score}",
                   self.screen,
                   pos_x_center=675,
                   pos_y_center=225
                   )
            text_utils(f"Death Count: {self.death_count}",
                   self.screen,
                   pos_x_center=425,
                   pos_y_center=225
                   )
            text_utils(f"High score: {self.high_score}",
                   self.screen,
                   pos_x_center=half_screen_width,
                   pos_y_center=half_screen_height + 190
                   )
            text_utils("Develoment by: Kacterine Martínez",
                   self.screen,
                   font_size=14,
                   pos_x_center=170,
                   pos_y_center=half_screen_height + 280
                   )
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
