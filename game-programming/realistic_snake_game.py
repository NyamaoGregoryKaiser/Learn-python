import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Snake Game")

# Clock to control the game loop speed
clock = pygame.time.Clock()

# Snake settings
snake_block = 20
snake = [[100, 50]]  # Initial position of the snake's body (head + segments)
direction = "RIGHT"
change_to = direction

# Food settings
food = [random.randint(0, (WIDTH // snake_block) - 1) * snake_block,
        random.randint(0, (HEIGHT // snake_block) - 1) * snake_block]

# Score
score = 0
font = pygame.font.Font(None, 35)

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))

def spawn_food():
    while True:
        new_food = [random.randint(0, (WIDTH // snake_block) - 1) * snake_block,
                    random.randint(0, (HEIGHT // snake_block) - 1) * snake_block]
        if new_food not in snake:  # Ensure food doesn't spawn inside the snake
            return new_food

def game_over():
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    screen.blit(game_over_text, [WIDTH // 4, HEIGHT // 2])
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle snake movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        change_to = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        change_to = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        change_to = "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        change_to = "RIGHT"

    # Update the direction
    direction = change_to

    # Move the snake
    head = snake[0]
    if direction == "UP":
        new_head = [head[0], head[1] - snake_block]
    elif direction == "DOWN":
        new_head = [head[0], head[1] + snake_block]
    elif direction == "LEFT":
        new_head = [head[0] - snake_block, head[1]]
    elif direction == "RIGHT":
        new_head = [head[0] + snake_block, head[1]]

    # Check for collisions
    if (new_head in snake or  # Snake collides with itself
        new_head[0] < 0 or new_head[0] >= WIDTH or  # Snake hits left/right wall
        new_head[1] < 0 or new_head[1] >= HEIGHT):  # Snake hits top/bottom wall
        game_over()

    # Add the new head to the snake
    snake.insert(0, new_head)

    # Check if snake eats the food
    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()  # Remove the tail if no food is eaten

    # Draw the screen
    screen.fill(BLACK)
    draw_snake(snake)
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], snake_block, snake_block))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

    # Control the speed of the snake
    clock.tick(10)

