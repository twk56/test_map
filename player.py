# player.py
import pygame
from config import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT  # ปรับใช้ SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)

    def handle_movement(self, keys):
        # เคลื่อนที่ตามการกดปุ่มและจำกัดการเคลื่อนไหวในขอบเขตของหน้าจอ
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PLAYER_SPEED
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

    def draw(self, surface, camera_x, camera_y):
        # วาดผู้เล่นในตำแหน่งจริง โดยไม่มีการเลื่อนกล้อง
        pygame.draw.rect(surface, PLAYER_COLOR, (self.rect.x, self.rect.y, PLAYER_SIZE, PLAYER_SIZE))
