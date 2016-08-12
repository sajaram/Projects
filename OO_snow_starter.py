"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
darkblue = (14, 81, 117)
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
	
	def __init__(self, size, position, wind = False):
		self.size = size
		self.position = position
		self.wind = wind
	def fall(self, speed):
		self.position[1] = self.position[1] + speed
		if self.wind :
			self.position[0] = self.position[0] + random.randint(-speed, speed)
	def draw(self):
		pygame.draw.circle(screen, WHITE, self.position, self.size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List
snow_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(darkblue)
	x_pos = random.randrange(0, 700)
	y_pos = 0
    # --- Drawing code should go here 
	snow_list.append(SnowFlake(5,[x_pos, y_pos], True))
    # Begin Snow
	for flake in snow_list:
		flake.draw()
		flake.fall(speed)

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
