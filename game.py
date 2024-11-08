# Import and initialize pygame
import pygame 
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))
        # Challenge 1 
        # screen.fill((63,63,63))

apple = GameObject(100, 400, 'apple.png') 
apple2 = GameObject(100, 100, 'apple.png') 
apple3 = GameObject(250, 250, 'apple.png') 
apple4 = GameObject(400, 100, 'apple.png') 
apple5 = GameObject(400, 400, 'apple.png') 

strawberry = GameObject(100, 250, 'strawberry.png')
strawberry1 = GameObject(400,250, 'strawberry.png')
strawberry2 = GameObject(250,100, 'strawberry.png')
strawberry3 = GameObject(250,400, 'strawberry.png')

# game loop 
running = True 
while running: 
        # Looking at the events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Clear the screen 
        screen.fill((255,255,255))
        # ADD!
        apple.render(screen)
        apple2.render(screen)
        apple3.render(screen)
        apple4.render(screen)
        apple5.render(screen)
        strawberry.render(screen)
        strawberry1.render(screen)
        strawberry2.render(screen)
        strawberry3.render(screen)
        pygame.display.flip()
        

        
        
       
    # Make an instance of GameObject
        
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
        # color = (169,169,169)
        # postion = (100, 400)
        # pygame.draw.circle(screen, color, postion, 55)
       
        # #Circle 2 
        # color = (169,169,169)
        # postion = (100, 100)
        # pygame.draw.circle(screen, color, postion, 55)
        
        # #Circle 3
        # color = (169,169,169)
        # postion = (250, 250)
        # pygame.draw.circle(screen, color, postion, 55)
        
        # #Circle 4
        # color = (169,169,169)
        # postion = (400, 100)
        # pygame.draw.circle(screen, color, postion, 55)
        
        # #Circle 5
        # color = (169,169,169)
        # postion = (400, 400)
        # pygame.draw.circle(screen, color, postion, 55)
       
        # # Circle 6 
        # color = (169,169,169)
        # postion = (100, 250)
        # pygame.draw.circle(screen, color, postion, 55)
       
        # #Circle 7
        # color = (169,169,169)
        # postion = (400, 250)
        # pygame.draw.circle(screen, color, postion, 55)
       
        # #Circle 8
        # color = (169,169,169)
        # postion = (250, 100)
        # pygame.draw.circle(screen, color, postion, 55)
        # #Circle 9
        # color = (169,169,169)
        # postion = (250, 400)
        # pygame.draw.circle(screen, color, postion, 55)
        # pygame.display.flip()
        
        
        
        