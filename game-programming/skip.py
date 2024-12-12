
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_width, player_height = 50, 50
player_x, player_y = 100, HEIGHT - player_height - 10
player_velocity_y = 0
gravity = 0.5
jump_strength = -10
is_jumping = False

# Obstacle properties
obstacle_width, obstacle_height = 50, 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 10
obstacle_speed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not is_jumping:
            if event.key == pygame.K_SPACE:
                is_jumping = True
                player_velocity_y = jump_strength

    # Update player position
    player_velocity_y += gravity
    player_y += player_velocity_y
    if player_y >= HEIGHT - player_height - 10:
        player_y = HEIGHT - player_height - 10
        is_jumping = False

    # Update obstacle position
    obstacle_x -= obstacle_speed
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH
        score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if player_rect.colliderect(obstacle_rect):
        running = False  # End the game on collision

    # Draw player and obstacle
    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, RED, obstacle_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
