# Import and initialize pygame
import pygame 
from random import randint
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Get the clock
clock = pygame.time.Clock()

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

class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the apple
   if self.y > 500: 
     self.reset()

 # add a new method
 def reset(self):
   self.x = randint(50, 400)
   self.y = -64

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0,0, 'strawberry.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here!
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500: 
            self.reset()
    def reset(self):
        self.x = randint(50, 400)
        self.y = -64


apple = Apple() 
strawberry = Strawberry()
# apple2 = GameObject(100, 100, 'apple.png') 
# apple3 = GameObject(250, 250, 'apple.png') 
# apple4 = GameObject(400, 100, 'apple.png') 
# apple5 = GameObject(400, 400, 'apple.png') 

# strawberry = GameObject(100, 250, 'strawberry.png')
# strawberry1 = GameObject(400,250, 'strawberry.png')
# strawberry2 = GameObject(250,100, 'strawberry.png')
# strawberry3 = GameObject(250,400, 'strawberry.png')

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
        apple.x += 1.5
        apple.move()
        apple.render(screen)
        strawberry.x +=1.5
        strawberry.move()
        strawberry.render(screen)
        # apple2.render(screen)
        # apple3.render(screen)
        # apple4.render(screen)
        # apple5.render(screen)
        # strawberry.render(screen)
        # strawberry1.render(screen)
        # strawberry2.render(screen)
        # strawberry3.render(screen)
        pygame.display.flip()
        clock.tick(60)
        

        
        
       
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
        
        
        
        