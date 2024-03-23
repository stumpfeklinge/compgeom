import pygame
import random

class Snowflake:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y > height:  # Если снежинка достигла дна экрана
            self.y = random.randint(-height, 0)  # Перезапускаем её в верхней части экрана


    def draw(self):
        pygame.draw.circle(screen, (58, 31, 0), (int(self.x), int(self.y)), 40)


pygame.init()
width, height = 2400, 1800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Снежинка-печенье)")
clock = pygame.time.Clock()

snowflakes = []
for _ in range(150):
    x = random.randint(0, width)
    y = random.randint(0, height)
    speed = random.randint(1, 5)
    snowflakes.append(Snowflake(x, y, speed))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for snowflake in snowflakes:
                if snowflake.x - 40 <= event.pos[0] <= snowflake.x + 40 and snowflake.y - 40 <= event.pos[
                    1] <= snowflake.y + 40:
                    snowflake.x, snowflake.y = pygame.mouse.get_pos()

    screen.fill((235,208,150))

    for snowflake in snowflakes:
        snowflake.update()
        snowflake.draw()

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
