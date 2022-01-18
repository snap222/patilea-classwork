from typing_extensions import Self


class Shape():
	def __init__(self,myColourFill, myColourOutline):
		self.colourFill = myColourFill
		self.colourOutline = myColourOutline

	def calculateArea(self,mySide):
		self.area = mySide * mySide

class Rectangle(Shape):
	def __init__ (self, myColourFill, myColourOutline, myHeight, myWidth):
		super().__init__ (myColourFill, myColourOutline)
		self.height = myHeight
		self.width = myWidth

  def calculateArea(self):
    self.area = self.height * self.width

class Circle(Shape):
  def __init__ (self, myColourFill, myColourOutline, myRadius):
    super().__init__ (myColourFill, myColourOutline)
    self.radius = myRadius

  def calculateArea(self):
    self.area = 3.1415 * (self.radius)^2
  

myRectangle = Rectangle("red","yellow", 4, 5)
myCircle = Circle("purple", "black", 3, 6)
print(myCircle.calculateArea())
print(myRectangle.calculateArea())