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
        screen.fill((255,255,255))
        
        #Circle
        color = (255, 0, 255)
        positon = (250,250)
        pygame.draw.circle(screen, color, positon, 75)
        # Update
        pygame.display.flip()