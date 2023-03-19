import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 640
display_height = 480
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Simple Worm Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the worm

worm_block_size = 10
worm_speed = 17
worm_body = [(display_width // 2, display_height // 2)]
worm_direction = 'DOWN'

# Set up the food
food_block_size = 10
food_x = random.randint(0, display_width - food_block_size)
food_y = random.randint(0, display_height - food_block_size)

# Set up the score
score = 0

# Define restart game
def restart_game():
    global worm_body, worm_direction, score
    worm_body = [(display_width // 2, display_height // 2)]
    worm_direction = 'DOWN'
    score = 0


# Handle user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                restart_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
            # Change worm direction when keys are pressed
            elif event.key == pygame.K_LEFT and worm_direction != 'RIGHT':
                worm_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and worm_direction != 'LEFT':
                worm_direction = 'RIGHT'
            elif event.key == pygame.K_UP and worm_direction != 'DOWN':
                worm_direction = 'UP'
            elif event.key == pygame.K_DOWN and worm_direction != 'UP':
                worm_direction = 'DOWN'

    # Move worm
    if worm_direction == 'LEFT':
        worm_body.insert(0, (worm_body[0][0] - worm_block_size, worm_body[0][1]))
    elif worm_direction == "RIGHT":
        worm_body.insert(0, (worm_body[0][0] + worm_block_size, worm_body[0][1]))
    elif worm_direction == "UP":
        worm_body.insert(0, (worm_body[0][0], worm_body[0][1] - worm_block_size))
    elif worm_direction == "DOWN":
        worm_body.insert(0, (worm_body[0][0], worm_body[0][1] + worm_block_size))

    # Check if worm hit the wall
    if worm_body[0][0] < 0 or worm_body[0][0] >= display_width or worm_body[0][1] < 0 or worm_body[0][1] >= display_height:
        pygame.quit()
        quit()

    # Check if worm hit itself
    if worm_body[0] in worm_body[1:]:
        pygame.quit()
        quit()

    # Check if worm ate food
    if worm_body[0][0] < food_x + food_block_size and worm_body[0][0] + worm_block_size > food_x and worm_body[0][1] < food_y + food_block_size and worm_body[0][1] + worm_block_size > food_y:
        food_x = random.randint(0, display_width - food_block_size)
        food_y = random.randint(0, display_height - food_block_size)
        score += 1
    else:
        worm_body.pop()


        # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the worm
    for block in worm_body:
        pygame.draw.rect(screen, (163, 33, 122), [block[0], block[1], worm_block_size, worm_block_size])
    #Draw the food
    pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, food_block_size, food_block_size])
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(15)


