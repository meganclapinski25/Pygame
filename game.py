# Import and initialize pygame
import pygame 
from random import randint, choice
pygame.init()

lanes = [93, 218, 343]
# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Get the clock
clock = pygame.time.Clock()

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image, scale = (64,64)):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.surf = pygame.transform.scale(self.surf, scale)
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect()

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
    screen.blit(self.surf, (self.x, self.y))
    # Challenge 1
    # screen.fill((63,63,63))



class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = (randint(100,200) / 100) -1 
        self.dy = 0 
        self.reset()

    def move(self):
      self.x += self.dx  
      if self.x > 500: 
        self.reset()
      

    def reset(self):
      self.y = choice(lanes)    
      self.x = -64
      self.dx = (randint(100,200) / 100) +1 
      # self.dx = (randint(100, 200) / 100) + 1


class Strawberry(GameObject):
    def __init__(self):
      super(Strawberry, self).__init__(0, 0, 'strawberry.png')
      self.dy = (randint(100,200) / 100) +1 
      self.dx = 0  
      self.reset()
    
    def move(self):
      self.y += self.dy  
      if self.y > 500:
        self.reset()
      
    
    def reset(self):
        self.x = choice(lanes)
        self.y = -64
        self.dy = (randint(100,200) / 100) + 1
class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0,0, 'pngegg.png', scale=(58,64))
    self.dy = (randint(100,200)/100) + 1 
    self.dx = (randint(100,200)/100) + 1 
    self.reset()
  def move(self):
    self.y+=self.dy
    
    if self.y > 500 or self.x > 500 :
      self.reset()
  def reset(self):
    self.x = choice(lanes)
    self.y = -64
    self.dy = (randint(100,200)/ 100)+ 1    
    self.dx =  (randint(100,200)/ 100)+ 1       


class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1 # new attribute
    self.pos_y = 1 # new attribute
    self.reset()

  def left(self):
	  if self.pos_x > 0:
		  self.pos_x -= 1
		  self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]



#initalize
player = Player()
strawberry = Strawberry()
apple = Apple()
bomb = Bomb()
# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
# make a fruits Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)


# apple2 = GameObject(100, 100, 'apple.png') 
# apple3 = GameObject(250, 250, 'apple.png') 
# apple4 = GameObject(400, 100, 'apple.png') 
# apple5 = GameObject(400, 400, 'apple.png') 

# strawberry = GameObject(100, 250, 'strawberry.png')
# strawberry1 = GameObject(400,250, 'strawberry.png')
# strawberry2 = GameObject(250,100, 'strawberry.png')
# strawberry3 = GameObject(250,400, 'strawberry.png')

# game loop 
# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render all sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Check for collisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()  
    # Check collision player and bomb
    if pygame.sprite.collide_rect(player, bomb):
      running = False  

    # Update the display
    pygame.display.flip()

    # Tick the clock to maintain a frame rate of 60 FPS
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
        
        
        
        