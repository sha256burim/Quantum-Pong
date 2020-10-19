import pygame
#from random import randint
import qsharp
from QuantumRNG import randint

#NOTE: We can take the random/randint thing and have it generate random numbers from a ranfe in our quantum simulator to add to the quantum stack

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        ##------------Quantum Computing Implementation Begin-----------##

        self.velocity = [randint(4,8),randint(-8,8)] #works fine so far

        ##------------Quantum Computing Implementation End-----------##
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)