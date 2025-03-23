import pygame
import sys
from map import draw_background  # นำเข้าเฉพาะ draw_background
from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("เกมทดสอบแผนที่และผู้เล่น")

    start_x, start_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2  
    player = Player(start_x, start_y)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        draw_background(screen)
        player.draw(screen, 0, 0)  # ไม่ใช้กล้อง ให้แสดงผู้เล่นตรงตำแหน่งจริง

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
