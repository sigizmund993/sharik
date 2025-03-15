import pygame
import time
import math
height = 255
width = 255
screen = pygame.display.set_mode((width,height))
screen.fill((0,255,0))
dT = 0.01
r = 8
R = 60
xBall = width/2
yBall = height/2
ballVelX = 3
ballVelY = 3
g = 0.2
a = 3
b = -1
c = -100
acol = 1
bcol = 1
ccol = 1
collisionPointX = 0
collisionPointY = 0
gapAngle = 0.6
vecX = 1
vecY = 1
circleRotateSpeed = 0.1
def calcSpeedCollide(velX,velY,a,b,c)->tuple[float,float]:
    alpha = math.acos((a*velX+b*velY)/math.sqrt((a**2+b**2)*(velX**2+velY**2)))
    beta = math.acos(velY/math.sqrt((velX**2+velY**2)))    
    ang = math.pi/2*3-2*alpha+beta
    vel = math.sqrt(velX**2+velY**2)
    resX = math.cos(ang)*vel
    resY = math.sin(ang)*vel
    return resX,resY
def calcABC(x1,y1,x2,y2)->tuple[float,float,float]:
    try:
        k = (y1-y2)/(x1-x2)
        d = y1-k*x1
        a = 1
        b = a/(-k)
        c = -d*b
        return a,b,c
    except:
        return 0,0,0
    
while(True):
    gapAngle+=circleRotateSpeed
    vecX = math.cos(gapAngle)
    vecY = math.sin(gapAngle)
    screen.fill((0,0,0))
    ballVelY+=g
    xBall+=ballVelX
    yBall+=ballVelY
    
    # alpha = math.acos((yBall-height/2)/math.sqrt(((width/2-xBall)**2+(height/2-yBall)**2)))    
    
    collisionPointX = (xBall-width/2)/math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)*R+width/2
    collisionPointY = (yBall-height/2)/math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)*R+height/2
    collisionPointAngle = math.acos((vecX*(collisionPointX-width/2)+vecY*(collisionPointY-height/2))/math.sqrt((vecX**2+vecY**2)*((collisionPointX-width/2)**2+(collisionPointY-height/2)**2)))
    acol,bcol,ccol = calcABC(width/2,height/2,collisionPointX,collisionPointY)
    tmp = acol
    acol = -bcol
    bcol = tmp
    ccol = -acol*collisionPointX-bcol*collisionPointY
    if((height/2-yBall)**2+(width/2-xBall)**2>=(R-r)**2 and collisionPointAngle>math.pi/6 and math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)<R):
        ballVelX,ballVelY = calcSpeedCollide(ballVelX,ballVelY,acol,bcol,ccol)
        xBall-=0.03*(collisionPointX-width/2)
        yBall-=0.03*(collisionPointY-height/2)
        # ballVelX,ballVelY = calcSpeedCollide(ballVelX,ballVelY,a,b,c)
    


    for x in range(255):
        for y in range(255):
            angle = math.acos((vecX*(x-width/2)+vecY*(y-height/2))/math.sqrt((vecX**2+vecY**2)*((x-width/2)**2+(y-height/2)**2)))
            if((xBall-x)**2+(yBall-y)**2<=r**2):
                pygame.draw.rect(screen,(255,255,255),(x,y,1,1),1)
            if((height/2-y)**2+(width/2-x)**2>=R**2 and (height/2-y)**2+(width/2-x)**2<=(R+2)**2 and angle>math.pi/6):
                pygame.draw.rect(screen,(255,0,255),(x,y,1,1),1)
            # if(acol*x+bcol*y+ccol >= 0 and acol*x+bcol*y+ccol<=1):
            #     pygame.draw.rect(screen,(255,0,0),(x,y,1,1),1)
    # pygame.draw.circle(screen,(0,0,255),(collisionPointX,collisionPointY),5)
    pygame.display.flip()
    time.sleep(dT)