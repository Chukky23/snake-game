import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake & Food Setup
def create_snake(length):
    return [(100 - i * BLOCK_SIZE, 100) for i in range(length)]

def generate_food(snake):
    grid_x = WIDTH // BLOCK_SIZE
    grid_y = HEIGHT // BLOCK_SIZE
    while True:
        x = random.randint(0, grid_x - 1) * BLOCK_SIZE
        y = random.randint(0, grid_y - 1) * BLOCK_SIZE
        if (x, y) not in snake:
            return (x, y)

snake = create_snake(5)
direction = (BLOCK_SIZE, 0)
food = generate_food(snake)
score = 0

running = True
while running:
    clock.tick(10)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)
            elif event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)

    # Move
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Eat
    if new_head == food:
        score += 1
        food = generate_food(snake)
    else:
        snake.pop()

    # Collisions
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        running = False

    # Draw
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()