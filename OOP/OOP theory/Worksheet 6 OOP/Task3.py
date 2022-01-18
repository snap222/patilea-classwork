class Dog():
  def __init__(self, myName, myColour):
    self.name = myName 
    self.colour = myColour
  #end procedure
  
  def setColour(self,myColour): #Public
    if myColour == 'unknown':
      self.colour = input('Enter a colour:')
    else:
      self.colour = myColour
    #end if
  #end procedure

  def bark(barkTimes):
    for n in range(barkTimes):
      print ("Woof!")
    #next n
  #end procedure


  def getColour(self): #Public
    return self.colour
  #end function

  def getName(self):
    return self.name
  #end function
#end class

class Puppy(Dog):
  def __init__ (self,myName, myColour, myDob):
    super().__init__(myName, myColour)
    self.dob = myDob
    self.shoesChewed = 0

  def chewShoes(self,numShoes):
    self.shoesChewed = self.shoesChewed + numShoes

  def GetShoesChewed(self):
    return self.shoesChewed

  def bark(barkTimes):
    for i in range(0,barkTimes):
      print("Yap!")

  def getDob(self):
    return self.dob

myFirstPuppy = Puppy('Malla','Light brown','12/08/2016')
print(myFirstPuppy.bark(2))
print(myFirstPuppy.getName())
print(myFirstPuppy.getColour())
print(myFirstPuppy.getDob())