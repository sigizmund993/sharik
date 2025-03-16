import pygame
import time
import math
height = 255
width = 255
screen = pygame.display.set_mode((width,height))
screen.fill((0,255,0))
dT = 0.01
r = 10
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
gapAngle = 0.5
vecX = 1
vecY = 1
circleRotateSpeed = 0.1
gapSize = 0.3
def calcSpeedCollide(velX:float,velY:float,a:float,b:float)->tuple[float,float]:
    alpha = math.acos((a*velX+b*velY)/math.sqrt((a**2+b**2)*(velX**2+velY**2)))
    beta = math.acos(velY/math.sqrt((velX**2+velY**2)))    
    ang = math.pi/2*3-2*alpha+beta
    vel = math.sqrt(velX**2+velY**2)
    resX = math.cos(ang)*vel
    resY = math.sin(ang)*vel
    return resX,resY
def calcABC(x1:float,y1:float,x2:float,y2:float)->tuple[float,float]:
    try:
        k = (y1-y2)/(x1-x2)
        a = 1
        b = a/(-k)
        return a,b
    except:
        return 0,0
def calcAngleBetweenVectors(x1:float,y1:float,x2:float,y2:float)->float:
    return math.acos((x1*x2+y1*y2)/math.sqrt((x1**2+y1**2)*(x2**2+y2**2)))
def drawCircle(xBall,yBall,r,w):
    for x in range(2*r):
        x-=r
        for y in range(2*r):
            y -=r
            if((x)**2+(y)**2<=r**2):
                if(w>0):
                    if((x)**2+(y)**2>=(r-w)**2):
                        z = 255/r*math.sqrt((x)**2+(y)**2)
                        screen.set_at((int(x+xBall),int(y+yBall)),(0,z,z))
                else:
                    z = 255/r*math.sqrt((x)**2+(y)**2)
                    screen.set_at((int(x+xBall),int(y+yBall)),(0,z,z))

    
while(True):
    gapAngle+=circleRotateSpeed
    vecX = math.cos(gapAngle)
    vecY = math.sin(gapAngle)
    screen.fill((0,0,0))
    ballVelY+=g
    xBall+=ballVelX
    yBall+=ballVelY
    
    # alpha = math.acos((yBall-height/2)/math.sqrt(((width/2-xBall)**2+(height/2-yBall)**2)))    
    if((height/2-yBall)**2+(width/2-xBall)**2>=(R-r)**2 and math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)<R):
        collisionPointX = (xBall-width/2)/math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)*R+width/2
        collisionPointY = (yBall-height/2)/math.sqrt((xBall-width/2)**2+(yBall-height/2)**2)*R+height/2
        collisionPointAngle = calcAngleBetweenVectors(collisionPointX,collisionPointY,vecX,vecY)
        if(collisionPointAngle>gapSize):
            acol,bcol = calcABC(width/2,height/2,collisionPointX,collisionPointY)
            tmp = acol
            acol = -bcol
            bcol = tmp
            ballVelX,ballVelY = calcSpeedCollide(ballVelX,ballVelY,acol,bcol)
            xBall-=0.03*(collisionPointX-width/2)
            yBall-=0.03*(collisionPointY-height/2)
    


    # for x in range(255):
    #     for y in range(255):
    #         angle = calcAngleBetweenVectors(vecX,vecY,(x-width/2),(y-height/2))
    #         if((xBall-x)**2+(yBall-y)**2<=r**2):
    #             z = 255/r*math.sqrt((x-xBall)**2+(y-yBall)**2)
    #             screen.set_at((x,y),(0,z,z))
    #         if((height/2-y)**2+(width/2-x)**2>=R**2 and (height/2-y)**2+(width/2-x)**2<=(R+2)**2 and angle>gapSize):
    #             screen.set_at((x,y),(255,0,255))
    
    drawCircle(xBall,yBall,r,-1)
    # drawCircle(width/2,height/2,R,3)

    pygame.draw.circle(screen,(0,255,0),(width/2,height/2),R,1)
    # pygame.draw.circle(screen,(0,0,255),(xBall,yBall),r)
    pygame.display.flip()
    time.sleep(dT)