# Import and initialize pygame
import pygame 
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# game loop 
running = True 
while running: 
        # Looking at the events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Clear the screen 
        # screen.fill((255,255,255))
        
        # #Circle
        # color = (25, 184, 22)
        # positon = (250,250)
        # pygame.draw.circle(screen, color, positon, 75)
        # # Update
        # pygame.display.flip()
        
        
        # Challenge 1 
        screen.fill((63,63,63))
        
        # # Circle 1 
        # color = (0,255,0)
        # postion = (100, 400)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        # #Circle 2 
        # color = (255,0,0)
        # postion = (100, 100)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        # #Circle 3
        # color = (225,225,0)
        # postion = (250, 250)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        # #Circle 4
        # color = (250,141,7)
        # postion = (400, 100)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        # #Circle 5
        # color = (0,225,225)
        # postion = (400, 400)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        
        #Challenge 2 
        
        # Circle 1 
        color = (169,169,169)
        postion = (100, 400)
        pygame.draw.circle(screen, color, postion, 55)
       
        #Circle 2 
        color = (169,169,169)
        postion = (100, 100)
        pygame.draw.circle(screen, color, postion, 55)
        
        #Circle 3
        color = (169,169,169)
        postion = (250, 250)
        pygame.draw.circle(screen, color, postion, 55)
        
        #Circle 4
        color = (169,169,169)
        postion = (400, 100)
        pygame.draw.circle(screen, color, postion, 55)
        
        #Circle 5
        color = (169,169,169)
        postion = (400, 400)
        pygame.draw.circle(screen, color, postion, 55)
       
        # Circle 6 
        color = (169,169,169)
        postion = (50, 50)
        pygame.draw.circle(screen, color, postion, 55)
       
        #Circle 7
        color = (169,169,169)
        postion = (50, 50)
        pygame.draw.circle(screen, color, postion, 55)
       
        #Circle 8
        color = (169,169,169)
        postion = (75, 75)
        pygame.draw.circle(screen, color, postion, 55)
        #Circle 9
        color = (169,169,169)
        postion = (50, 50)
        pygame.draw.circle(screen, color, postion, 55)
        pygame.display.flip()
        
        
        
        