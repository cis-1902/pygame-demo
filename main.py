import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CELL_WIDTH = 20

RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
BLACK_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game Demo")


def display_snake(snake: list[tuple[int, int]]):
    for x, y in snake:
        pygame.draw.rect(screen, GREEN_COLOR, pygame.Rect(x, y, CELL_WIDTH, CELL_WIDTH))


def display_apple(apple: tuple[int, int]):
    pygame.draw.circle(screen, RED_COLOR, apple, CELL_WIDTH // 2)


def get_random_coordinate():
    x = random.randint(0, SCREEN_WIDTH // CELL_WIDTH) * CELL_WIDTH
    y = random.randint(0, SCREEN_HEIGHT // CELL_WIDTH) * CELL_WIDTH
    return x, y


snake = [get_random_coordinate()]  # [head, ..., tail]

running = True

clock = pygame.time.Clock()

dir = "RIGHT"

apple = get_random_coordinate()

while True:
    while running:
        # event queue, process whatever has been clicked
        for event in pygame.event.get():
            # process each event
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # process snake direction changes
                if event.key == pygame.K_UP and dir != "DOWN":
                    dir = "UP"
                if event.key == pygame.K_DOWN and dir != "UP":
                    dir = "DOWN"
                if event.key == pygame.K_LEFT and dir != "RIGHT":
                    dir = "LEFT"
                if event.key == pygame.K_RIGHT and dir != "LEFT":
                    dir = "RIGHT"

        # depending on the direction, we update the snake
        curr_x, curr_y = snake[0]
        if dir == "UP":
            curr_y -= CELL_WIDTH
        elif dir == "DOWN":
            curr_y += CELL_WIDTH
        elif dir == "LEFT":
            curr_x -= CELL_WIDTH
        elif dir == "RIGHT":
            curr_x += CELL_WIDTH

        snake.insert(0, (curr_x, curr_y))

        # first thing to check, did we run into the wall or ourselves
        if (
            curr_x < 0
            or curr_x >= SCREEN_WIDTH
            or curr_y < 0
            or curr_y >= SCREEN_HEIGHT
        ):
            running = False

        # did we eat the apple
        if snake[0] == apple:
            apple = get_random_coordinate()
        else:
            snake.pop()

        # clear screen
        screen.fill(BLACK_COLOR)

        # draw snake
        display_snake(snake)
        display_apple(apple)

        clock.tick(10)

        pygame.display.flip()

    for event in pygame.event.get():
        # process each event
        if event.type == pygame.QUIT:
            break
