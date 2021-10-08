import pygame
import random
import math
from pygame import mixer

#intialize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((1000,600))

#Opening image
background1=pygame.image.load("open.jpg")
#Background image
background=pygame.image.load("background.jpg")

#Game over image
gameoverimg=pygame.image.load("gameover.jpg")
overX=0
overY=0

#Background sound
mixer.music.load("waltz-music-loop.mp3")
mixer.music.play(-1)


#title and icon
pygame.display.set_caption("Shooting Zombies")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#player
playerimg=pygame.image.load("player.png")
playerX=50
playerY=270
playerY_change=5

#Enemies
enemy1img=[]
enemy1X=[]
enemy1Y=[]
enemy1X_change=[]
enemy1Y_change=[]
enemy2img=[]
enemy2X=[]
enemy2Y=[]
enemy2X_change=[]
enemy2Y_change=[]
enemy3img=[]
enemy3X=[]
enemy3Y=[]
enemy3X_change=[]
enemy3Y_change=[]
enemy4img=[]
enemy4X=[]
enemy4Y=[]
enemy4X_change=[]
enemy4Y_change=[]
enemy5img=[]
enemy5X=[]
enemy5Y=[]
enemy5X_change=[]
enemy5Y_change=[]
num_of_enemies=2
for i in range(num_of_enemies):
    enemy1img.append(pygame.image.load("enemy1.png"))
    enemy1X.append(random.randint(600,900))
    enemy1Y.append(random.randint(40,120))
    enemy1Y_change.append(0)
    enemy1X_change.append(0.5)
    enemy2img.append(pygame.image.load("enemy2.png"))
    enemy2X.append(random.randint(600, 900))
    enemy2Y.append(random.randint(120, 240))
    enemy2Y_change.append(0)
    enemy2X_change.append(0.5)
    enemy3img.append(pygame.image.load("enemy3.png"))
    enemy3X.append(random.randint(600, 900))
    enemy3Y.append(random.randint(240, 360))
    enemy3Y_change.append(0)
    enemy3X_change.append(0.5)
    enemy4img.append(pygame.image.load("enemy4.png"))
    enemy4X.append(random.randint(600, 900))
    enemy4Y.append(random.randint(360, 480))
    enemy4Y_change.append(0)
    enemy4X_change.append(0.5)
    enemy5img.append(pygame.image.load("enemy5.png"))
    enemy5X.append(random.randint(600, 900))
    enemy5Y.append(random.randint(480, 500))
    enemy5Y_change.append(0)
    enemy5X_change.append(0.5)






#Bullets
#Ready-you can't see the bullet
#Fire-it means bullets moving on
bulletimg=pygame.image.load("bullet.png")
bulletX=50
bulletY=0
bulletX_change=10
bulletY_change=0
bullet_state="ready"

score_value=0
#score
font=pygame.font.Font('freesansbold.ttf',32)
textX=850
textY=10
font1=pygame.font.Font('freesansbold.ttf',64)
text1X=600
text1Y=400
def show_score(x,y):
    score=font.render("score:"+ str(score_value),True,(255,0,0))
    screen.blit(score,(x,y))

def show_score1(x,y):
    score=font1.render("score:"+ str(score_value),True,(255,0,0))
    screen.blit(score,(x,y))

#Game over
over_font=pygame.font.Font('freesansbold.ttf',70)
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,0,0))
    screen.blit(over_text,(300,50))


def player(x,y):
    screen.blit(playerimg,(x,y))

def over_game(x,y):
    screen.blit(gameoverimg,(x,y))

def enemy1(x,y,i):
    screen.blit(enemy1img[i],(x,y))
def enemy2(x,y,i):
    screen.blit(enemy2img[i],(x,y))
def enemy3(x,y,i):
    screen.blit(enemy3img[i],(x,y))
def enemy4(x,y,i):
    screen.blit(enemy4img[i],(x,y))
def enemy5(x,y,i):
    screen.blit(enemy5img[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+14,y+2))

def iscollision1(enemy1X,enemy1Y,bulletX,bulletY):
    distance=math.sqrt(((enemy1X-bulletX)**2)+((enemy1Y-bulletY)**2))
    if distance<30:
        return True
    else:
        return False
def iscollision2(enemy2X,enemy2Y,bulletX,bulletY):
    distance=math.sqrt(((enemy2X-bulletX)**2)+((enemy2Y-bulletY)**2))
    if distance<30:
        return True
    else:
        return False
def iscollision3(enemy3X,enemy3Y,bulletX,bulletY):
    distance=math.sqrt(((enemy3X-bulletX)**2)+((enemy3Y-bulletY)**2))
    if distance<30:
        return True
    else:
        return False
def iscollision4(enemy4X,enemy4Y,bulletX,bulletY):
    distance=math.sqrt(((enemy4X-bulletX)**2)+((enemy4Y-bulletY)**2))
    if distance<30:
        return True
    else:
        return False
def iscollision5(enemy5X,enemy5Y,bulletX,bulletY):
    distance=math.sqrt(((enemy5X-bulletX)**2)+((enemy5Y-bulletY)**2))
    if distance<30:
        return True
    else:
        return False

#game loop
running=True
while running:
    # screen color
    screen.fill((0, 255, 0))
    #Background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #keyboard controls
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
               playerY_change=-5
            if event.key==pygame.K_DOWN:
               playerY_change=5
            if event.key== pygame.K_SPACE:
                bullet_sound=mixer.Sound("gun.wav")
                bullet_sound.play()
                #Get a bullet for player Y coordinates
                if bullet_state=="ready":
                    bulletY=playerY
                    fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change=0
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 510:
        playerY = 510

    # Enemy1 movement
    for i in range(num_of_enemies):
        # Game over
        if enemy1X[i]<100:
            game_over_sound=mixer.Sound("game1.wav")
            game_over_sound.play()
            over_game(overX,overY)
            game_over_text()
            show_score1(text1X,text1Y)
            playerY=2000
            break
            for j in range(2):
                enemy1X[j]=2000
                enemy2X[j]=2000
                enemy3X[j]=2000
                enemy4X[j]=2000
                enemy5X[j]=2000
        elif enemy2X[i]<100:
            game_over_sound = mixer.Sound("game1.wav")
            game_over_sound.play()
            over_game(overX, overY)
            game_over_text()
            show_score1(text1X, text1Y)
            playerY = 2000
            break
            for j in range(2):
                enemy1X[j]=2000
                enemy2X[j]=2000
                enemy3X[j]=2000
                enemy4X[j]=2000
                enemy5X[j]=2000
        elif enemy3X[i]<100:
            game_over_sound = mixer.Sound("game1.wav")
            game_over_sound.play()
            over_game(overX, overY)
            game_over_text()
            show_score1(text1X, text1Y)
            playerY = 2000
            break
            for j in range(2):
                enemy1X[j]=2000
                enemy2X[j]=2000
                enemy3X[j]=2000
                enemy4X[j]=2000
                enemy5X[j]=2000
        elif enemy4X[i]<100:
            game_over_sound = mixer.Sound("game1.wav")
            game_over_sound.play()
            over_game(overX, overY)
            game_over_text()
            show_score1(text1X, text1Y)
            playerY = 2000
            break
            for j in range(2):
                enemy1X[j]=2000
                enemy2X[j]=2000
                enemy3X[j]=2000
                enemy4X[j]=2000
                enemy5X[j]=2000
        elif enemy5X[i]<100:
            game_over_sound = mixer.Sound("game1.wav")
            game_over_sound.play()
            over_game(overX, overY)
            game_over_text()
            show_score1(text1X, text1Y)
            playerY = 2000
            break
            for j in range(2):
                enemy1X[j]=2000
                enemy2X[j]=2000
                enemy3X[j]=2000
                enemy4X[j]=2000
                enemy5X[j]=2000



        enemy1X[i]+= enemy1X_change[i]
        if enemy1X[i] <=50:
            enemy1X_change[i]=0.5
        elif enemy1X [i]>=900:
            enemy1X_change[i]=-0.5
        # collision1
        collision1 = iscollision1(enemy1X[i], enemy1Y[i], bulletX, bulletY)
        if collision1:
            death_sound = mixer.Sound("explosion1.wav")
            death_sound.play()
            bulletX = 50
            bullet_state = "ready"
            score_value += 1
            enemy1X[i] = random.randint(600, 900)
            enemy1Y[i]= random.randint(40, 120)

        enemy1(enemy1X[i], enemy1Y[i],i)

        #Enemy2 movement
        enemy2X[i] +=enemy2X_change[i]
        if enemy2X[i] <=50:
            enemy2X_change[i]=0.5
        elif enemy2X[i] >=900:
            enemy2X_change[i]=-0.5
        # collision2
        collision2 = iscollision2(enemy2X[i], enemy2Y[i], bulletX, bulletY)
        if collision2:
            death_sound = mixer.Sound("explosion1.wav")
            death_sound.play()
            bulletX = 50
            bullet_state = "ready"
            score_value +=1
            enemy2X[i] = random.randint(600, 900)
            enemy2Y[i] = random.randint(120, 240)

        enemy2(enemy2X[i], enemy2Y[i],i)


        # Enemy3 movement
        enemy3X[i]+= enemy3X_change[i]
        if enemy3X[i] <= 50:
            enemy3X_change[i] = 0.5
        elif enemy3X[i] >= 900:
            enemy3X_change[i] = -0.5
        # collision3
        collision3 = iscollision3(enemy3X[i], enemy3Y[i], bulletX, bulletY)
        if collision3:
            death_sound = mixer.Sound("explosion1.wav")
            death_sound.play()
            bulletX = 50
            bullet_state = "ready"
            score_value +=1
            enemy3X[i] = random.randint(600, 900)
            enemy3Y[i] = random.randint(240, 360)

        enemy3(enemy3X[i], enemy3Y[i],i)
        # Enemy4 movement
        enemy4X[i] += enemy4X_change[i]
        if enemy4X[i] <= 50:
            enemy4X_change[i] = 0.5
        elif enemy4X[i] >= 900:
            enemy4X_change[i] = -0.5
        # collision4
        collision4 = iscollision4(enemy4X[i], enemy4Y[i], bulletX, bulletY)
        if collision4:
            death_sound = mixer.Sound("explosion1.wav")
            death_sound.play()
            bulletX = 50
            bullet_state = "ready"
            score_value +=1
            enemy4X[i] = random.randint(600, 900)
            enemy4Y[i] = random.randint(360, 480)

        enemy4(enemy4X[i], enemy4Y[i],i)
        # Enemy5 movement
        enemy5X[i] += enemy5X_change[i]
        if enemy5X[i] <= 50:
            enemy5X_change[i] = 0.5
        elif enemy5X[i] >= 900:
            enemy5X_change[i] = -0.5
        # collision5
        collision5 = iscollision5(enemy5X[i], enemy5Y[i], bulletX, bulletY)
        if collision5:
            death_sound=mixer.Sound("explosion1.wav")
            death_sound.play()
            bulletX = 50
            bullet_state = "ready"
            score_value +=1
            enemy5X[i] = random.randint(600, 900)
            enemy5Y[i] = random.randint(480, 500)

        enemy5(enemy5X[i], enemy5Y[i],i)

    #Bullet Movement
    if bulletX>=1000:
        bulletX=50
        bullet_state="ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletX +=bulletX_change

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()






