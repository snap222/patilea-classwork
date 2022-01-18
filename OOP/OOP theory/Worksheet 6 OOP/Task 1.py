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

myDog3 = Dog('Mutton','unknown')
myDog4 = Dog('Jeff','unknown')
myDog3.setColour('unknown')
print(myDog3.getName())
print(myDog3.getColour())