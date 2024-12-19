import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 750, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Urban Escape")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)  # Road color
YELLOW = (255, 255, 0)  # Lane divider color
DARK_GRAY = (30, 30, 30)  # Road edge color

# Car dimensions
car_width, car_height = 85, 170

# Load car images
player_image = pygame.image.load('player.png')  # Player car image
player_image = pygame.transform.scale(player_image, (car_width, car_height))

enemy_images = [
    pygame.transform.scale(pygame.image.load('enemy.png'), (car_width, car_height)),
    pygame.transform.scale(pygame.image.load('car1.png'), (car_width, car_height)),
    pygame.transform.scale(pygame.image.load('car2.png'), (car_width, car_height)),
    pygame.transform.scale(pygame.image.load('car3.png'), (car_width, car_height))
]

# Lane details
num_lanes = 6
lane_width = WIDTH // num_lanes
lane_centers = [lane_width * i + lane_width // 2 for i in range(num_lanes)]  # Center of each lane

# Player properties
player_x = lane_centers[num_lanes // 2] - car_width // 2  # Start in the middle lane
player_y = HEIGHT - car_height - 20
player_speed = 1  # Movement by lanes, not pixels

# Enemy car properties
enemy_cars = []
enemy_min_speed = 3
enemy_max_speed = 8
spawn_interval = 2000
last_spawn_time = pygame.time.get_ticks()

# Score and difficulty
score = 0
font = pygame.font.SysFont("Arial", 24)
difficulty_increase = 10

# Sound effects
pygame.mixer.init()
crash_sound = pygame.mixer.Sound('bang.wav')  # Replace with a realistic crash sound

# Game state
running = True
paused = False

def draw_road():
    # Draw the road
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, HEIGHT))
    
    # Draw the road edges
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, lane_width // 2, HEIGHT))
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH - lane_width // 2, 0, lane_width // 2, HEIGHT))
    
    # Draw lane dividers
    for i in range(1, num_lanes):
        x = i * lane_width
        for y in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, YELLOW, (x - 2, y, 5, 20))

# Game loop
while running:
    # Draw the road
    draw_road()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Toggle pause
                paused = not paused
            if not paused:
                # Player moves between lanes
                if event.key == pygame.K_LEFT:
                    current_lane_index = lane_centers.index(player_x + car_width // 2)
                    if current_lane_index > 0:  # Ensure not out of bounds
                        player_x = lane_centers[current_lane_index - 1] - car_width // 2
                if event.key == pygame.K_RIGHT:
                    current_lane_index = lane_centers.index(player_x + car_width // 2)
                    if current_lane_index < num_lanes - 1:  # Ensure not out of bounds
                        player_x = lane_centers[current_lane_index + 1] - car_width // 2

    if paused:
        pause_text = font.render("Game Paused - Press P to Resume", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        continue

    # Spawn enemy cars based on timer
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_interval:
        lane_center = random.choice(lane_centers)
        enemy_x = lane_center - car_width // 2
        enemy_speed = random.randint(enemy_min_speed, enemy_max_speed)
        enemy_image = random.choice(enemy_images)
        enemy_cars.append({"rect": pygame.Rect(enemy_x, -car_height, car_width, car_height), "speed": enemy_speed, "image": enemy_image})
        last_spawn_time = current_time

    # Move enemy cars
    for car in enemy_cars[:]:
        car["rect"].y += car["speed"]
        if car["rect"].y > HEIGHT:
            enemy_cars.remove(car)
            score += 1
        # Collision detection
        if car["rect"].colliderect(pygame.Rect(player_x, player_y, car_width, car_height)):
            pygame.mixer.Sound.play(crash_sound)
            running = False

    # Draw player car
    screen.blit(player_image, (player_x, player_y))

    # Draw enemy cars
    for car in enemy_cars:
        screen.blit(car["image"], (car["rect"].x, car["rect"].y))

    # Gradually increase difficulty
    if score % difficulty_increase == 0 and score != 0:
        enemy_min_speed += 1
        enemy_max_speed += 1
        spawn_interval = max(500, spawn_interval - 100)  # Decrease spawn interval, minimum 500ms

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
