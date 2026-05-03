import pygame
import sys

pygame.init()
pygame.mixer.init()

bgmusic='music\music.mp3'

pygame.mixer.music.load(bgmusic)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


screen=pygame.display.set_mode((1000,500))
pygame.display.set_caption("Witch in the Jungle")
testfont=pygame.font.Font('font/yoster.ttf',50)
testfont1=pygame.font.Font('font/yoster.ttf',20)


clock=pygame.time.Clock()

mousepos=pygame.mouse.get_pos()
mx,my=mousepos

cursor1=pygame.image.load('character/cursor.png').convert_alpha()
cursor2=pygame.transform.scale(cursor1, (15,20))

goblin1=pygame.image.load('character/goblin.png').convert_alpha()
goblin=pygame.transform.scale(goblin1, (50,50))

goblin2=pygame.image.load('character/goblin.png').convert_alpha()
goblin3=pygame.transform.scale(goblin2, (50,50))

score=testfont.render('Score: ', False, 'darkgreen')
screen2=pygame.image.load('graphics/background.jpg').convert()
background=pygame.transform.scale(screen2, (1000,500))
name=testfont1.render("Witch in the Jungle", False, 'darkolivegreen')

character1 = pygame.image.load('character/witch1.png').convert_alpha()
character= pygame.transform.scale(character1, (100,80))

x=-200

witch= character.get_rect(topleft= (x, 320))

goblinn= goblin.get_rect(topleft=(1000,380))
goblinn1= goblin3.get_rect(topleft=(1000,280))
goblinn2= goblin3.get_rect(topleft=(500,330))
goblinn4= goblin3.get_rect(topleft=(700,230))
goblinn5= goblin3.get_rect(topleft=(400,180))

score1=0


while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background, (0,0))
    screen.blit(score, (410, 50))
    screen.blit(name, (390, 15))
    

    witch.left +=2.5
    if witch.left>=1000:
        witch.left=x       
    screen.blit(character, witch) 

    goblinn.right -= 1.6
    if goblinn.right<=-120:
        goblinn.right=1100
    screen.blit(goblin, goblinn)

    goblinn1.right-=1
    if goblinn1.right<=-150:
        goblinn1.right=1150
    screen.blit(goblin3, goblinn1)

    goblinn2.right-=1.2
    if goblinn2.right<=-150:
        goblinn2.right=1150
    screen.blit(goblin3, goblinn2)

    goblinn4.right-=1.9
    if goblinn4.right<=-150:
        goblinn4.right=1150
    screen.blit(goblin3, goblinn4)

    goblinn5.right-=1.5
    if goblinn5.right<=-150:
        goblinn5.right=1150
    screen.blit(goblin3, goblinn5)


    mousepos=pygame.mouse.get_pos()
    mx,my=mousepos

    pygame.mouse.set_visible(False)
    cursor=cursor2.get_rect(topleft=(mx,my))
    screen.blit(cursor2, cursor)


    # if witch.collidepoint(mousepos):
    #             print(f"Mouse touching witch! Current top = {witch.top}")
    
    if witch.collidepoint(mousepos):
                    mx,my=mousepos
                    witch.centery=my
                    #witch.centerx=mx
                    if witch.top<100:
                        witch.top=100   
                    if witch.bottom>480:
                        witch.bottom=480                                          
                    
    gob= [goblinn, goblinn1, goblinn2, goblinn4, goblinn5]
    if any (witch.colliderect(g) for g in gob):
            score1-=1
            
    elif any (witch.right-g.left<80 and witch.right-g.left>=0 and not witch.colliderect(g) for g in gob):
            # print("Score added ")
            score1+=2

    # elif witch.right-goblinn1.left<80 and witch.right-goblinn1.left>=0 and not witch.colliderect(goblinn1):
    #         # print("Score added ")
    #         score1+=2
  
    score2=testfont.render(f"{score1}", False, 'gold')
    screen.blit(score2, (615,50))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
