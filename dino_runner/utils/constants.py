import pygame
import os

# Global Constants
TITLE = "Chrome Demon Slayer Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/TanjiroStart.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/TanjiroDead.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/TanjiroRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/TanjiroRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRun2.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunShield2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/TanjiroDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/TanjiroDuck2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuck2.png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckShield2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump/TanjiroJump.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpShield.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)

# Obstacles
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
TREE = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallTree1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallTree2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallTree3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTree1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTree2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeTree3.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

DEMON = [    
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Demon1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Demon2.png")),
    ]

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))

LOGO = pygame.image.load(os.path.join(IMG_DIR, "Other/Logo.png"))
BG = pygame.image.load(os.path.join(IMG_DIR, "Other/TanjiroTrack.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
