import pygame
import random
import math

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космический Симулятор")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Класс для звезд
class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.1, 1)
        self.size = random.randint(1, 3)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Класс для космического корабля
class Spaceship:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.polygon(screen, WHITE, [(self.x, self.y), (self.x - 20, self.y + 40), (self.x + 20, self.y + 40)])

# Создание объектов
stars = [Star() for _ in range(100)]
ship = Spaceship()

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.move("left")
    if keys[pygame.K_RIGHT]:
        ship.move("right")

    screen.fill(BLACK)

    for star in stars:
        star.move()
        star.draw()

    ship.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
