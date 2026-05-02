import pygame

pygame.init

screen=pygame.display.set_mode((500,600))


x=0
hii=pygame.Vector2(x,250)



run=True
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False
     
    #screen.fill("pink")
    
    pygame.draw.circle(screen, 'green' ,hii, 40)
    x+=0.1
    pygame.display.update()

pygame.quit()
