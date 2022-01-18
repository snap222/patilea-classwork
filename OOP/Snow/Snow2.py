import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class House:
  def __init__(self):
    self.x = 440
    self.y = 400
    self.height = 55
    self.width = 112
    self.colour - RED

class Snow:
  def __init__(self,height,width):
    self.y = random.randint(0,490)
    self.x = random.randint(10,680)
    self.colour = WHITE
    self.height = height
    self.width = width
  #end procedure
  def update(self):
    if self.y > 500:
      self.x = random.randint(10,690)
      self.y = random.randint(0,490)
    else:
      self.y = self.y + 1
    #endif
  #end procedure
  def draw(self):
      pygame.draw.rect(screen, self.colour, [self.x,self.y,10,10])
  #end procdure
#end class
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
snow_drops = []
for n in range(0,200):
    snow_drops.append(Snow(10,10))
#next

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for snow_drop in snow_drops:
        snow_drop.update()
    #next
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for snow_drop in snow_drops:
        snow_drop.draw()
    #next
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
