import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player properties
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Load image
image = pygame.image.load("player.jpg")  # Ensure this file exists
image_rect = image.get_rect()
image_rect.topleft = (200, 200)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Drawing everything
    screen.fill(WHITE)  # Clear screen
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))  # Draw player
    screen.blit(image, image_rect)  # Draw image

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Cap the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
