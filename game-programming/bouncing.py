import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example: Moving Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_radius = 20
ball_speed = [2, 2]

# Clock
clock = pygame.time.Clock()

# Music
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/cosym/Downloads/kids/background_music.mp3")
 # Ensure the music file is in the same directory or provide a path
pygame.mixer.music.play(-1)  # Play the music in a loop (-1 for infinite loops)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # Stop music before quitting
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce off walls
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
