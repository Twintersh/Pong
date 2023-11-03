from graphics import *

def main() :

	win = GraphWin("Program", 300, 300)	
	aR = Rectangle(Point(50, 50), Point(250, 250))
	aR.draw(win)

	win.getMouse()
	win.close()

main()