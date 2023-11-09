import pygame

pygame.init()
WHITE = (255, 255, 255)
HEIGHT = 480
WIDTH = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


class Ball:
	def __init__(self, posX, posY, radius, speed, direc, color):
		self.posx = posX
		self.posy = posY
		self.radius = radius
		self.speedX = speed
		self.speedY = speed
		self.direc = direc
		self.color = color
		self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)


	def  display(self):
		self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
	
	def move(self):
		if (self.posx >= WIDTH or self.posx <= 0):
			self.posx = WIDTH/2
			self.posy = HEIGHT/2
			self.speedX *= -1
		if (self.posy >= HEIGHT or self.posy <= 0):
			self.speedY *= -1
		self.posx += self.speedX
		self.posy += self.speedY
		self.display()

	def hit(self):
		self.speedX *= -1		
	
	def getBall(self):
		return self.ball



class Stricker:
	def __init__(self, posX, posY, width, height, speed, color):
		self.posx = posX
		self.posy = posY - height/2
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		self.Rect = pygame.Rect(posX, posY, width, height)

	def display(self):
		self.Rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
		self.paddle = pygame.draw.rect(screen, self.color, self.Rect)

	def moveup(self):
		if (13 < self.posy):
			self.posy -= self.speed
			self.display()
			
	def movedown(self):
		if (self.posy < HEIGHT - 13):
			self.posy += self.speed
			self.display()

	def getRect(self):
		return self.Rect


def main():
	running = True
	paddle1 = Stricker(WIDTH - 25, HEIGHT/2, 13, 75, 20, WHITE)
	paddle2 = Stricker(25, HEIGHT/2, 13, 75, 20, WHITE)
	circle = Ball(WIDTH/2, HEIGHT/2, 10, 0.2, 1, WHITE)

	while (running):
		screen.fill((0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					paddle1.moveup()
				if event.key == pygame.K_DOWN:
					paddle1.movedown()
				if event.key == pygame.K_w:
					paddle2.moveup()
				if event.key == pygame.K_s:
					paddle2.movedown()

		if pygame.Rect.colliderect(circle.getBall(), paddle1.getRect()):
			circle.hit()
		if pygame.Rect.colliderect(circle.getBall(), paddle2.getRect()):
			circle.hit()

		paddle1.display()
		paddle2.display()
		circle.move()
		pygame.display.flip()



if __name__ == "__main__":
	main()
	pygame.quit()