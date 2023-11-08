import pygame

pygame.init()
ballcolor = (255, 0, 0)
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Pong")


class Ball:
	def __init__(self, posX, posY, radius, speed, direc, color):
		print("caca")
		self.posx = posX
		self.posy = posY
		self.radius = radius
		self.speed = speed
		self.direc = direc
		self.color = color

	def  display(self):
		self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
	
	def move(self):
		if (self.posx >= 200 or self.posx <= 0):
			self.speed *= -1
		self.posx += self.speed
		self.display()




class Stricker:
	def __init__(self, posX, posY, width, height, speed, color):
		self.posx = posX
		self.posy = posY
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		self.Rect = pygame.Rect(posX, posY, width, height)
		# self.paddle = pygame.draw.rect(screen, self.color, self.Rect)

	def display(self):
		self.paddle = pygame.draw.rect(screen, self.color, self.Rect)



def main():
	running = True
	direc = 0.1
	ballXY = [100, 100]
	paddle1 = Stricker(100, 100, 10, 50, 0.1, ballcolor)
	circle = Ball(100, 10, 10, 0.1, 1, (0, 255, 255))
	paddle1.display()

	while (running):
		screen.fill((255, 0, 255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		circle.move()

		pygame.display.flip()



if __name__ == "__main__":
	main()
	pygame.quit()