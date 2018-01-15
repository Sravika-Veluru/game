import pygame
import random
W = 1200
H =650



WHITE= (255, 255, 128)
YELLOW=(255, 224, 102)
BLACK=(0,0,0)

B_PLAYCOLOR1=(115,115,115)
PLAYCOLOR1=(18,18,84)


PLAYCOLOR2=(18,18,84)
B_PLAYCOLOR2=(115,115,115)


B_PLAYCOLOR3=(115,115,115)
PLAYCOLOR3=(18,18,84)



TITLECOLOR=(204, 230, 255)
BLUE = (0, 255, 0)
GREEN = (26, 26, 255)
pygame.init()


bgmcoin=pygame.mixer.Sound("IMG_0842 (1).wav")



gameDisplay = pygame.display.set_mode([W,H])



pygame.display.set_caption('Fun & Frolic')
imggameover=pygame.image.load('gameover.png')

imgbluecar=pygame.image.load('bluecar1.png')
imgbluecar1=pygame.image.load('bluecar1.png')

imgbg=pygame.image.load('bg.png')


imglevel1intro=pygame.image.load('level1intro.png')
imglevel2intro=pygame.image.load('level2intro.png')
imglevel3intro=pygame.image.load('level3intro.png')



def level1intro():
    level1=True
    while level1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imglevel1intro,(0,0))
        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 100>mouse[0]>0 and 50>mouse[1]>0:
            pygame.draw.rect(gameDisplay,(67,112,112),(0,0,100,50))
            if click[0]==1:
                game_intro()
        else:
            pygame.draw.rect(gameDisplay,(96,159,159),(0,0,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf12,TextRect12=text_objects("BACK",smallText)
        TextRect12.center=((45,30))
        gameDisplay.blit(TextSurf12,TextRect12)
        
        pygame.display.update()
        clock.tick(150)
    
    
    
def level2intro():
    level2=True
    while level2:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imglevel2intro,(0,0))

        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 0+100>mouse[0]>0 and 0+50>mouse[1]>0:
            pygame.draw.rect(gameDisplay,(67,112,112),(0,0,100,50))
            if click[0]==1:
                game_intro()
        else:
            pygame.draw.rect(gameDisplay,(96,159,159),(0,0,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf11,TextRect11=text_objects("BACK",smallText)
        TextRect11.center=((45,30))
        gameDisplay.blit(TextSurf11,TextRect11)
        
        pygame.display.update()
        clock.tick(150)
   
    



def level3intro():
    
    level3=True
    while level3:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(WHITE)
        gameDisplay.blit(imglevel3intro,(0,0))
        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 0+100>mouse[0]>0 and 0+50>mouse[1]>0:
            pygame.draw.rect(gameDisplay,(67,112,112),(0,0,100,50))
            if click[0]==1:
                game_intro()
        else:
            pygame.draw.rect(gameDisplay,(96,159,159),(0,0,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf10,TextRect10=text_objects("BACK",smallText)
        TextRect10.center=((45,30))
        gameDisplay.blit(TextSurf10,TextRect10)
        
        
        pygame.display.update()
        clock.tick(150)
        

    
def gameover(count):
    
   
    gmov=True
    while gmov:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        
        
        gameDisplay.blit(imggameover,(0,0))
        largeText=pygame.font.Font('freesansbold.ttf',70)
        TextSurf1,TextRect1=text_objectsb("Score:",largeText)
        TextRect1.center=((W/2),(H/2-50))
        
        smallText=pygame.font.Font('freesansbold.ttf',50)
        TextSurf3,TextRect3=text_objectsb(str(count),smallText)
        TextRect3.center=((W/2+200),(H/2-50))
        
        
        gameDisplay.blit(TextSurf1,TextRect1)
        
        
        gameDisplay.blit(TextSurf3,TextRect3)
        
        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 0+100>mouse[0]>0 and 0+50>mouse[1]>0:
            pygame.draw.rect(gameDisplay,(67,112,112),(0,0,100,50))
            if click[0]==1:
                game_intro()
        else:
            pygame.draw.rect(gameDisplay,(96,159,159),(0,0,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects("BACK",smallText)
        TextRect.center=((45,30))
        gameDisplay.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(15)






def thingsl2(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])



def scorel2(count):
    font = pygame.font.SysFont(None,25)
    text=font.render("SCORE :"+str(count),True,(255,255,255))
    gameDisplay.blit(text,(05,10))
    


def circlel2(cx1,cy1):
    pygame.draw.circle(gameDisplay,(117,160,240),(cx1,cy1),15)
    



clock = pygame.time.Clock()




 

    

    
def min1l2(x1,y1):
    gameDisplay.blit(imgbluecar,(x1,y1))
def min2l2(x2,y2):
    gameDisplay.blit(imgbluecar1,(x2,y2))
def text_objects(text,font):
    textSurface=font.render(text,True,(255,255,255))
    return textSurface,textSurface.get_rect()
def text_objectsb(text,font):
    textSurface=font.render(text,True,(0,0,0))
    return textSurface,textSurface.get_rect()




def game_intro():
    
    intro=True
    while intro:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(imgbg,(0,0))
        largeText=pygame.font.Font('freesansbold.ttf',110)
        TextSurf,TextRect=text_objectsb("FnF",largeText)
        TextRect.center=((W/2),(H/2-200))
        gameDisplay.blit(TextSurf,TextRect)


      

        mouse = pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 130+100>mouse[0]>130 and 450+50>mouse[1]>450:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR1,(130,450,100,50))
            if click[0]==1:
                gameloop1()
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR1,(130,450,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects("LEVEL 1 ",smallText)
        TextRect.center=((180,480))
        gameDisplay.blit(TextSurf,TextRect)







        if 550+100>mouse[0]>550 and 450+50>mouse[1]>450:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR2,(550,450,100,50))
            if click[0]==1:
                gameloop2()
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR2,(550,450,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects("LEVEL 2 ",smallText)
        TextRect.center=((600,480))
        gameDisplay.blit(TextSurf,TextRect)
        






        

        if 900+100>mouse[0]>900 and 450+50>mouse[1]>450:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR3,(900,450,100,50))
            if click[0]==1:
                gameloop3()
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR3,(900,450,100,50))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf,TextRect=text_objects("LEVEL 3 ",smallText)
        TextRect.center=((900+50,480))
        gameDisplay.blit(TextSurf,TextRect)




        if 150+30>mouse[0]>150 and 400+30>mouse[1]>400:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR1,(150,400,30,30))
            if click[0]==1:
                level1intro()
            
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR1,(150,400,30,30))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf4,TextRect4=text_objects("?",smallText)
        TextRect4.center=((150+15,400+20))
        gameDisplay.blit(TextSurf4,TextRect4)



        
        

        if 570+30>mouse[0]>570 and 400+30>mouse[1]>400:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR2,(570,400,30,30))
            if click[0]==1:
                level2intro()
            
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR2,(570,400,30,30))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf5,TextRect5=text_objects("?",smallText)
        TextRect5.center=((570+15,400+20))
        gameDisplay.blit(TextSurf5,TextRect5)






        if 920+30>mouse[0]>920 and 400+30>mouse[1]>400:
            pygame.draw.rect(gameDisplay,B_PLAYCOLOR3,(920,400,30,30))
            if click[0]==1:
                level3intro()
            
        else:
            pygame.draw.rect(gameDisplay,PLAYCOLOR3,(920,400,30,30))
        smallText=pygame.font.Font('freesansbold.ttf',20)
        TextSurf6,TextRect6=text_objects("?",smallText)
        TextRect6.center=((920+15,400+20))
        gameDisplay.blit(TextSurf6,TextRect6)
        


        

            





        pygame.display.update()
        clock.tick(15)



def gameloop1():
    
    gameDisplay = pygame.display.set_mode([W,H])
    x1=W/8-10
    x2=5*W/8-10
    y2=350
    y1=350


    thing_x1=W/4-10
    
    thing_y1=0
    
    thing_w=20
    thing_h=125

    thing_x2=3*W/4-10
    thing_y2=0



    speed=3
    COUNT=0
    
    

    
    x_change1=0
    x_change2=0
    y_change2=0
    y_change1=0


   
    c_y1=-1500
    c_y2=H+1500

    
    
    
    
    randomno1 = random.randrange(1,3)
    if randomno1==1:
        c_x1=Wl1/8
       
        
        
        
    elif randomno1==2:
        c_x1=3*Wl1/8
        

    randomno2 = random.randrange(1,3)
    if randomno2==1:
        c_x2=5*Wl1/8
        
        
        
        
    elif randomno2==2:
        c_x2=7*Wl1/8
        



    
        
    

    crash=False

    while not crash:
        
        

        
       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crash=True
                
                gameover(COUNT)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if x1<300:
                        while(x1!=440):
                        
                            x_change1=5
                            x1+=x_change1
                            
                    else:
                        while(x1!=140):
                            
                            x_change1=-5
                            x1+=x_change1
                elif event.key==pygame.K_RIGHT:
                    if x2<900:
                        while(x2!=1040):
                            x_change2=5
                            x2+=x_change2
                    else:
                        while(x2!=740):
                            x_change2=-5
                            x2+=x_change2
                
            if event.type==pygame.KEYUP:
                x_change1=0
                y_change1=0
                x_change2=0

        
        
        gameDisplay.fill((38,38,38))
        thingsl2(thing_x1,thing_y1,thing_w,thing_h,(255,255,255))
        thing_y1+=speed

        thingsl2(thing_x2,thing_y2,thing_w,thing_h,(255,255,255))
        thing_y2+=speed

        if thing_y1>H:
            
            thing_y1=-200
        if thing_y2>H:
            
            thing_y2=-200
        



        circlel2(c_x1,c_y1)
        
        c_y1+=speed

        circlel2(c_x2,c_y2)
        c_y2-=speed
        if c_y1>H or c_y2<0:
            
            c_y1=0
            c_y2=H
            COUNT+=1
            randomno1 = random.randrange(1,3)
            if randomno1==1:
                c_x1=Wl1/8
            
            
            
            
            elif randomno1==2:
                c_x1=3*Wl1/8
                

            randomno2 = random.randrange(1,3)
            if randomno2==1:
                c_x2=5*Wl1/8
                
            
            
            
            elif randomno2==2:
                c_x2=7*Wl1/8
                

            
        if ((c_x1>x1 and c_x1<x1+30) and (c_y1>=y1 and c_y1<y1+60)) or ((c_x2>=x2 and c_x2<x2+30) and (c_y2>=y2 and c_y2<y2+60)):
            crash=True
            
            gameover(COUNT)
        
        
        
        min1l2(x1,y1)
        min2l2(x2,y2)
        scorel2(COUNT)
        


        
        for i in range(0,7):
            point1 = i,0
            point2 = i,H
            point3 = W-i,0
            point4 = W-i,648
            point5 = 0,i
            point6 = W,i
            point7 = 0,H-i
            point8 = W,H-i
            point9=W/2-i,0
            point10=W/2-i,H
            pygame.draw.line(gameDisplay,(0,0,255),point1,point2)
            pygame.draw.line(gameDisplay,(0,0,255),point3,point4)
            pygame.draw.line(gameDisplay,(0,0,255),point5,point6)
            pygame.draw.line(gameDisplay,(0,0,255),point7,point8)
            pygame.draw.line(gameDisplay,(0,0,255),point9,point10)

        
        

        pygame.display.update()

        clock.tick(150)

Wl1 = 1200
Hl1 =650


WHITEl1 = (255,255,255)
BLACKl1 = (0,0,0)


BLUEl1 = (255, 255, 26)
GREENl1 = (26, 26, 255)



gameDisplay = pygame.display.set_mode([Wl1,Hl1])


pygame.display.set_caption('Fun & Frolic')


def thingsl1(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])


def scorel1(count):
    font = pygame.font.SysFont(None,25)
    text=font.render("SCORE :"+str(count),True,(0,250,250))
    gameDisplay.blit(text,(W-200,30))
    
    





def circlel1(cx1,cy1):
    pygame.draw.circle(gameDisplay,GREEN,(cx1,cy1),10,10)
    



clock = pygame.time.Clock()



img = pygame.image.load('car.png')

 

    

    
def min1l1(x1,y1):
    gameDisplay.blit(img,(x1,y1))
def min2l1(x2,y2):
    gameDisplay.blit(img,(x2,y2))

imgl2=pygame.image.load('divider.png')

def divider(divx,divy):
    gameDisplay.blit(imgl2,(divx,divy))

def LIFE(count1):
    font = pygame.font.SysFont(None,25)
    text=font.render("LIFE:"+str(count1),True,(227,150,99))
    gameDisplay.blit(text,(W-200,10))






def gameloop2():
    
    

    x1=W/8-10
    x2=5*W/8-10
    y2=450
    y1=450
    life=3

    thing_x1=W/4-10
    
    thing_y1=0
    speed=5
    thing_w=20
    thing_h=125

    thing_x2=3*W/4-10
    thing_y2=0


    
    x_change1=0
    x_change2=0
    y_change2=0
    y_change1=0


    
    c_y1=-800
    c_y2=-800
    c_y3=-1000
    c_y4=-1000



    divx=W/2-10
    divy1=0
    divy2=162
    divy3=2*162
    divy4=3*162
    divy5=4*162


    COUNT=0
    
    
    
    

    randomno1 = random.randrange(1,3)
    if randomno1==1:
        c_x1=Wl1/8
        c_x3=3*Wl1/8
        
        
        
    elif randomno1==2:
        c_x1=3*Wl1/8
        c_x3=Wl1/8

    randomno2 = random.randrange(1,3)
    if randomno2==1:
        c_x2=5*Wl1/8
        c_x4=7*Wl1/8
        
        
        
    elif randomno2==2:
        c_x2=7*Wl1/8
        c_x4=5*Wl1/8



    
        
    

    crash=False

    while not crash:
        
        

        
       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crash=True
                gameover(COUNT)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if x1<300:
                        while(x1!=440):
                        
                            x_change1=5
                            x1+=x_change1
                            
                    else:
                        while(x1!=140):
                            
                            x_change1=-5
                            x1+=x_change1
                elif event.key==pygame.K_RIGHT:
                    if x2<900:
                        while(x2!=1040):
                            x_change2=5
                            x2+=x_change2
                    else:
                        while(x2!=740):
                            x_change2=-5
                            x2+=x_change2
                
            if event.type==pygame.KEYUP:
                x_change1=0
                y_change1=0
                x_change2=0

        
        
        gameDisplay.fill(BLACKl1)
        thingsl1(thing_x1,thing_y1,thing_w,thing_h,WHITEl1)
        thing_y1+=speed

        thingsl1(thing_x2,thing_y2,thing_w,thing_h,WHITEl1)
        thing_y2+=speed

        if thing_y1>Hl1 or thing_y2>Hl1:
            
            thing_y1=-200
            thing_y2=-200
            
    





        divider(divx,divy1)
        divy1+=speed

        if divy1>H:
            divy1=-160
        divider(divx,divy2)
        divy2+=speed
        if divy2>H:
            divy2=-160
        divider(divx,divy3)
        divy3+=speed
        if divy3>H:
            divy3=-160
        divider(divx,divy4)
        divy4+=speed
        if divy4>H:
            divy4=-160


        divider(divx,divy5)
        divy5+=speed
        if divy5>H:
            divy5=-160





        

        circlel1(c_x1,c_y1)
        
        c_y1+=speed
        circlel1(c_x3,c_y3)
        c_y3+=speed

        circlel1(c_x2,c_y2)
        c_y2+=speed
        circlel1(c_x4,c_y4)
        c_y4+=speed
        if c_y1>Hl1 or c_y2>Hl1:
            
            c_y1=0
            c_y2=0
            COUNT+=1
            randomno1 = random.randrange(1,3)
            if randomno1==1:
                c_x1=Wl1/8
                
        
        
        
            elif randomno1==2:
                c_x1=3*Wl1/8
                


            randomno2 = random.randrange(1,3)
            if randomno2==1:
                c_x2=5*Wl1/8
                
        
        
        
            elif randomno2==2:
                c_x2=7*Wl1/8
                
            
        if c_y3>Hl1 or c_y4>Hl1:
            c_y3=0
            c_y4=0
            COUNT+=1
            randomno1 = random.randrange(1,3)
            if randomno1==1:
                
                c_x3=3*Wl1/8
        
        
        
            elif randomno1==2:
                
                c_x3=Wl1/8


            randomno2 = random.randrange(1,3)
            if randomno2==1:
                
                c_x4=7*Wl1/8
        
        
        
            elif randomno2==2:
                
                c_x4=5*Wl1/8
            
        if ((c_x1>=x1 and c_x1<x1+30) and (c_y1>=y1 and c_y1<y1+60)) or ((c_x3>=x1 and c_x3<x1+30)and (c_y3>=y1 and c_y3<y1+60)) or ((c_x4>=x2 and c_x4<x2+30) and (c_y4>=y2 and c_y4<y2+60)) or ((c_x2>=x2 and c_x2<x2+30) and (c_y2>=y2 and c_y2<y2+60)):
            if(c_y1==y1)or(c_y2==y2)or(c_y3==y1)or(c_y4==y2):
                life=life-1
            
            if(life==-1):
                crash=True              
                gameover(COUNT)
        
        
        min1l1(x1,y1)
        min2l1(x2,y2)
        scorel1(COUNT)
        LIFE(life)
        

       
        
        for i in range(0,7):
            point1 = i,0
            point2 = i,Hl1
            point3 = Wl1-i,0
            point4 = Wl1-i,648
            point5 = 0,i
            point6 = Wl1,i
            point7 = 0,Hl1-i
            point8 = W,Hl1-i
            point9=Wl1/2,0
            point10=Wl1/2,Hl1
            pygame.draw.line(gameDisplay,BLUE,point1,point2)
            pygame.draw.line(gameDisplay,BLUE,point3,point4)
            pygame.draw.line(gameDisplay,BLUE,point5,point6)
            pygame.draw.line(gameDisplay,BLUE,point7,point8)
            
            
        
        
        pygame.display.update()

        clock.tick(150)







W = 1200
H =650


WHITE = (255,255,255)
BLACK = (0,0,0)


BLUE = (255, 255, 26)
GREEN = (26, 26, 255)
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])



img3=pygame.image.load('divider.png')
def divider(divx,divy):
    gameDisplay.blit(img3,(divx,divy))

def score(count):
    font = pygame.font.SysFont(None,25)
    text=font.render("SCORE :"+str(count),True,(227,150,99))
    gameDisplay.blit(text,(W-200,30))
def LIFE(count1):
    font = pygame.font.SysFont(None,25)
    text=font.render("LIFE:"+str(count1),True,(227,150,99))
    gameDisplay.blit(text,(W-200,10))
    
    

img = pygame.image.load('car.png')



def circle(cx1,cy1):
    pygame.draw.circle(gameDisplay,GREEN,(cx1,cy1),10,10)

def rect(rx1,ry1):
    pygame.draw.rect(gameDisplay,BLUE,[rx1,ry1,20,20])


clock = pygame.time.Clock()



img = pygame.image.load('car.png')

 

    

    
def min1(x1,y1):
    gameDisplay.blit(img,(x1,y1))
def min2(x2,y2):
    gameDisplay.blit(img,(x2,y2))


def gameloop3():
    
    x1=W/8-10
    x2=5*W/8-10
    y2=450
    y1=450


    thing_x1=W/4-10
    
    thing_y1=0
    speed=5
    thing_w=20
    thing_h=125

    thing_x2=3*W/4-10
    thing_y2=0


    
    x_change1=0
    x_change2=0
    y_change2=0
    y_change1=0


    
    divx=W/2-10
    divy1=0
    divy2=162
    divy3=2*162
    divy4=3*162
    divy5=4*162

   
    c_y1=-200
    c_y2=-200

    ry1=-500
    ry2=-500


    

    


    COUNT=0

    life=2
    
    
    

    randomno1 = random.randrange(1,3)
    if randomno1==1:
        c_x1=W/8
        rx1=3*W/8
        
        
        
    elif randomno1==2:
        c_x1=3*W/8
        rx1=W/8

    randomno2 = random.randrange(1,3)
    if randomno2==1:
        c_x2=5*W/8
        rx2=7*W/8
        
        
        
    elif randomno2==2:
        c_x2=7*W/8
        rx2=5*W/8

    


    
        
    

    crash=False

    while not crash:
        
        
        

        
       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crash=True
                gameover(COUNT)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if x1<300:
                        while(x1!=440):
                        
                            x_change1=5
                            x1+=x_change1
                            
                    else:
                        while(x1!=140):
                            
                            x_change1=-5
                            x1+=x_change1
                elif event.key==pygame.K_RIGHT:
                    if x2<900:
                        while(x2!=1040):
                            x_change2=5
                            x2+=x_change2
                    else:
                        while(x2!=740):
                            x_change2=-5
                            x2+=x_change2
                
            if event.type==pygame.KEYUP:
                x_change1=0
                y_change1=0
                x_change2=0

        
        
        gameDisplay.fill(BLACK)
        
        things(thing_x1,thing_y1,thing_w,thing_h,WHITE)
        thing_y1+=speed

        things(thing_x2,thing_y2,thing_w,thing_h,WHITE)
        thing_y2+=speed

        if thing_y1>H or thing_y2>H:
            
            thing_y1=-200
            thing_y2=-200
            
    









        divider(divx,divy1)
        divy1+=1

        if divy1>H:
            divy1=-160
        divider(divx,divy2)
        divy2+=1
        if divy2>H:
            divy2=-160
        divider(divx,divy3)
        divy3+=1
        if divy3>H:
            divy3=-160
        divider(divx,divy4)
        divy4+=1
        if divy4>H:
            divy4=-160


        divider(divx,divy5)
        divy5+=1
        if divy5>H:
            divy5=-160



       








        

        circle(c_x1,c_y1)
        
        c_y1+=speed
        rect(rx1,ry1)
        ry1+=speed

        circle(c_x2,c_y2)
        c_y2+=speed
        rect(rx2,ry2)
        ry2+=speed
        if c_y1>H or c_y2>H:
            
            
            c_y1=0
            c_y2=0
            COUNT+=1
            
                
            randomno1 = random.randrange(1,3)
            if randomno1==1:
                c_x1=W/8
                
        
        
        
            elif randomno1==2:
                c_x1=3*W/8
                


            randomno2 = random.randrange(1,3)
            if randomno2==1:
                c_x2=5*W/8
                
        
        
        
            elif randomno2==2:
                c_x2=7*W/8
                
            
        if ry1>H or ry2>H:
            ry1=0
            ry2=0
            
            randomno1 = random.randrange(1,3)
            if randomno1==1:
                
                rx1=3*W/8
        
        
        
            elif randomno1==2:
                
                rx1=W/8


            randomno2 = random.randrange(1,3)
            if randomno2==1:
                
                rx2=7*W/8
        
        
        
            elif randomno2==2:
                
                rx2=5*W/8
            
        if (c_x1==x1+10 and (c_y1>=y1 and c_y1<y1+60) ) or (c_x2==x2+10 and (c_y2>=y2 and c_y2<y2+60)):
            if c_y1==y1 or  c_y2==y2 :
                life=life-1
            if (life==-1):
                crash=True
                life=2
                gameover(COUNT)
        if (rx1==x1+10 and (ry1>=y1 and ry1<y1+60) ) or (rx2==x2+10 and (ry2>=y2 and ry2<y2+60)):

            COUNT=COUNT+0.25
            pygame.mixer.Sound.play(bgmcoin)
            
            
        
        
        min1(x1,y1)
        min2(x2,y2)
        score(COUNT)
        
        LIFE(life)
       
        


        
        for i in range(0,7):
            point1 = i,0
            point2 = i,H
            point3 = W-i,0
            point4 = W-i,648
            point5 = 0,i
            point6 = W,i
            point7 = 0,H-i
            point8 = W,H-i
            point9=W/2,0
            point10=W/2,H
            pygame.draw.line(gameDisplay,BLUE,point1,point2)
            pygame.draw.line(gameDisplay,BLUE,point3,point4)
            pygame.draw.line(gameDisplay,BLUE,point5,point6)
            pygame.draw.line(gameDisplay,BLUE,point7,point8)
            

        
        

        pygame.display.update()

        clock.tick(150)
    
     









     
game_intro()



pygame.quit()
quit()
