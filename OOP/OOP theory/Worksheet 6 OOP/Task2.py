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
    for n in range(0,barkTimes):
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


myFirstPuppy = Puppy('Bob','Red','17/06/2020')
print(myFirstPuppy.getName())
myFirstPuppy.chewShoes(3)
print(myFirstPuppy.GetShoesChewed())