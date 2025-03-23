import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE_PATH

background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)

def draw_background(surface):
    background_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    surface.blit(background_scaled, (0, 0))
