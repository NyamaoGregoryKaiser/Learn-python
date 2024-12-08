import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player properties
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Falling object properties
block_width, block_height = 50, 50
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move the falling block
    block_y += block_speed
    if block_y > HEIGHT:
        block_y = -block_height
        block_x = random.randint(0, WIDTH - block_width)
        score += 1  # Increase score when a block is successfully dodged

    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
    if player_rect.colliderect(block_rect):
        print(f"Game Over! Final Score: {score}")
        running = False

    # Draw everything
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))  # Player
    pygame.draw.rect(screen, RED, (block_x, block_y, block_width, block_height))  # Falling block

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Cap the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
