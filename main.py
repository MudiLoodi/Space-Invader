import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("./img/ufo.png")
pygame.display.set_icon(icon)
BG = pygame.image.load("./img/bg.png")

playerImg = pygame.image.load("./img/player.png")
playerX = 600
playerY = 700
player_xMove = 0

enemyImg = []
enemyX = []
enemyY = []
enemy_XMove = []
enemy_YMove = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./img/enemy.png"))
    enemyX.append(random.randint(0, 1200))
    enemyY.append(random.randint(-60, 150))
    enemy_XMove.append(6)
    enemy_YMove.append(30)

bulletImg = pygame.image.load("./img/bullet.png")
bulletX = 0
bulletY = 700
bullet_xMove = 0
bullet_YMove = 18
bulletState = "ready"

scoreValue = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 25, y))


def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) +
                         (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(BG, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xMove = -8
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_xMove = 8
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_xMove = 0

    playerX += player_xMove

    if playerX < 0:
        playerX = 0
    elif playerX > 1136:
        playerX = 1136

    for i in range(num_of_enemies):
        enemyX[i] += enemy_XMove[i]
        if enemyX[i] < 0:
            enemy_XMove[i] = 6
            enemyY[i] += enemy_YMove[i]
        elif enemyX[i] > 1136:
            enemy_XMove[i] = -6
            enemyY[i] += enemy_YMove[i]
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 700
            bulletState = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 1200)
            enemyY[i] = random.randint(-60, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletState == "fire":
        fire(bulletX, bulletY)
        bulletY -= bullet_YMove

    if bulletY < 0:
        bulletY = 700
        bulletState = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
