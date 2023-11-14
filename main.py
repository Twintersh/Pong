import pygame
import random
from math import * 

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
HEIGHT = 480
WIDTH = 640
MAX_ANGLE = 55 # default value : 55

paddleHeight=100 # default value: 100
paddleWidth=10 # default value: 10
paddleSpeed=15 # default value: 15
paddleMinHeight=50 # default value: 50
paddleDestruction=7 # default value:7
paddleColor=WHITE # default value: WHITE

ballColor=WHITE # default value: WHITE
ballRadius=7 # default value: 7
ballSpeed=5 # default value: 5
ballAcceleration=1.2 # default value: 1.2
ballMaxSpeed=7 # default value: 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
font = pygame.font.Font('./font.ttf', 50)
clock = pygame.time.Clock()
FPS=60


class Ball:
	def __init__(self, posX, posY, radius, speed, acce, color):
		self.posx = posX
		self.posy = posY
		self.radius = radius
		self.speedX = speed
		self.speedY = speed
		self.curSpeed = speed
		self.speed = speed
		self.acce = acce
		self.color = color
		self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)


	def  display(self):
		pygame.draw.circle(screen, (0,0,0), (self.posx, self.posy), self.radius+1)
		self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
	
	def move(self, paddles, score):
		if (self.posx >= WIDTH or self.posx <= 0):
			if (self.posx >= WIDTH):
				score[0] += 1
			else:
				score[1] += 1 
			self.posx = WIDTH/2
			self.posy = random.randint(HEIGHT * 0.25, HEIGHT * 0.75)
			self.speedX = (abs(self.speedX)/self.speedX) * -self.speed # (abs(self.speedX/self.speedX)) to keep the current sign of speedX
			self.speedY = (abs(self.speedY)/self.speedY) * self.speed
			self.curSpeed = self.speed
			paddles[0].height = paddleHeight
			paddles[1].height = paddleHeight
		if (self.posy >= HEIGHT or self.posy <= 0):
			self.speedY *= -1
		self.posx += self.speedX
		self.posy += self.speedY
		self.display()	

	def hit(self, paddle):
		hitPoint = self.posy - (paddle.posy + paddle.height/2)
		angle = (2* MAX_ANGLE * hitPoint) / paddle.height
		if (angle == 0):
			angle = 0.1

		if (abs(self.curSpeed) < ballMaxSpeed):
			self.curSpeed *= self.acce
		elif (abs(self.speed) >= ballMaxSpeed):
			self.curSpeed = (abs(self.curSpeed)/self.curSpeed) * -ballMaxSpeed

		self.speedY = self.curSpeed * sin(radians(angle))
		self.speedX = self.curSpeed * cos(radians(angle))

		if (self.posx >= WIDTH/2):
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

	def display(self, move):
		self.posy += move * self.speed
		if (self.posy < 0):
			self.posy = 0
		if (self.posy + self.height > HEIGHT):
			self.posy = HEIGHT-self.height
			
		self.Rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
		self.paddle = pygame.draw.rect(screen, self.color, self.Rect)

	def hit(self):
		if (self.height > paddleMinHeight):
			self.height -= paddleDestruction
		if (self.height < paddleMinHeight):
			self.height = paddleMinHeight

	def getRect(self):
		return self.Rect


def dispScore(score):
	score1 = font.render(str(score[0]), True, WHITE)
	score2 = font.render(str(score[1]), True, WHITE)

	rectScore1 = score1.get_rect()
	rectScore1 = (WIDTH * 0.22, 0)

	rectScore2 = score2.get_rect()
	rectScore2 = (WIDTH * 0.72, 0)

	screen.blit(score1, rectScore1)
	screen.blit(score2, rectScore2)
	

def main():
	running = True
	score = [0, 0]
	paddle1 = Stricker(WIDTH - (15 + paddleWidth), HEIGHT/2, paddleWidth, paddleHeight, paddleSpeed, paddleColor)
	paddle2 = Stricker(15, HEIGHT/2, paddleWidth, paddleHeight, paddleSpeed, paddleColor)
	circle = Ball(WIDTH/2, HEIGHT/2, ballRadius, ballSpeed, ballAcceleration, ballColor)
	move1 = 0;
	move2 = 0;

	while (running):
		screen.fill((0, 0, 0))
		dispScore(score)
		pygame.draw.line(screen, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					move1 = -1;
				if event.key == pygame.K_DOWN:
					move1 = 1;
				if event.key == pygame.K_w:
					move2 = -1;
				if event.key == pygame.K_s:
					move2 = 1;
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					move1 = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					move2 = 0

		if pygame.Rect.colliderect(circle.getBall(), paddle1.getRect()):
			circle.hit(paddle1)
			paddle1.hit()
		if pygame.Rect.colliderect(circle.getBall(), paddle2.getRect()):
			circle.hit(paddle2)
			paddle2.hit()

		paddle1.display(move1)
		paddle2.display(move2)
		circle.move([paddle1, paddle2], score)
		pygame.display.flip()
		clock.tick(FPS)



if __name__ == "__main__":
	main()
	pygame.quit()
