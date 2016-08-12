import pygame

black = (0, 0, 0)
white = (255, 255, 255) 
green = (0, 255, 0)
red = (255, 0, 0) 
blue = (0, 0, 255)
purple = (113, 33, 148)

pygame.init()

colors = ["blue", "red", "green", "purple", "white", "black"]
ball_color = random.choice(colors)

size = (700, 500) 
screen = pygame.display.set_mode(size)
screen.fill(green)


screen.fill(green)

colors = ["blue", "red", "green", "purple", "white", "black"]
ball_color = random.choice(colors)