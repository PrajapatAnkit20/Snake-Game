import pygame
import time
import random

# Initialize the game
pygame.init()

# Set the width and height of the display
width, height = 640, 480
display = pygame.display.set_mode((width, height))

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set the font for the score
font = pygame.font.Font(None, 36)

# Set the initial positions
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (width//10)) * 10,
                 random.randrange(1, (height//10)) * 10]
food_spawn = True

# Set the initial direction
direction = "RIGHT"
change_to = direction

# Set the initial score
score = 0


# Function to display the score on the screen
def display_score(score):
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, [0, 0])


# Function to display "Game Over" message on the screen
def game_over():
    message = font.render("Game Over!", True, red)
    display.blit(message, [width//2 - 100, height//2 - 50])
    pygame.display.flip()
    time.sleep(2)
    main()


# Main game logic
def main():
    global direction, change_to, snake_position, food_position, food_spawn, score

    # Game loop
    game_over_status = False
    while not game_over_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        # Validate the direction change
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        elif change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        elif change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        elif change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        # Update the snake position
        if direction == "UP":
            snake_position[1] -= 10
        elif direction == "DOWN":
            snake_position[1] += 10
        elif direction == "LEFT":
            snake_position[0] -= 10
        elif direction == "RIGHT":
            snake_position[0] += 10

        # Snake body mechanism
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (width//10)) * 10,
                             random.randrange(1, (height//10)) * 10]
        food_spawn = True

        # Draw the display
        display.fill(black)
        for pos in snake_body:
            pygame.draw.rect(display, green, pygame.Rect(
                pos[0], pos[1], 10, 10))

        pygame.draw.rect(display, white, pygame.Rect(
            food_position[0], food_position[1], 10, 10))

        # Game over conditions
        if snake_position[0] < 0 or snake_position[0] > width - 10:
            game_over_status = True
        if snake_position[1] < 0 or snake_position[1] > height - 10:
            game_over_status = True
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over_status = True

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.update()

        # Set the frames per second (FPS)
        pygame.time.Clock().tick(20)

    # Call the game over function
    game_over()


# Start the game
main()
