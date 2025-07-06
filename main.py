import sys

import pygame

# constants
WIDTH, HEIGHT = 800, 600
FPS = 24
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
clock = pygame.time.Clock()


# Paddies
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
ball_radius = 10


player = pygame.Rect(50, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(
    WIDTH - PADDLE_WIDTH - 50,
    (HEIGHT - PADDLE_HEIGHT) // 2,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
)

# Ball
ball = pygame.Rect(
    WIDTH // 2 - ball_radius,
    HEIGHT // 2 - ball_radius,
    ball_radius * 2,
    ball_radius * 2,
)
ball_speed_x = 5
ball_speed_y = 5


def player_movement(keys):
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5


def opponent_movement():
    if opponent.top < ball.centery and opponent.bottom < HEIGHT:
        opponent.y += 5
    elif opponent.bottom > ball.centery and opponent.top > 0:
        opponent.y -= 5


def ball_movement():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision
    if ball.bottom >= HEIGHT or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right > WIDTH or ball.left < 0:
        reset_ball()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    print("--------------------------")
    print(ball_speed_x, ball_speed_y)
    print(ball.x, ball.y)
    print("--------------------------")


def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1
    ball_speed_y *= -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_movement(keys)
    opponent_movement()
    ball_movement()
    # reset_ball()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    # pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), ball_radius)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
