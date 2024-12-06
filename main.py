class ioword:
   #contructor
   def __init__(self):
      self.word = " "
      #method -1
   def getword(self):
         self.word=input("Enter a word:")
         #method-2
   def display(self):
            print("uppercase val is:",self.word.upper())

word=ioword()
word.getword()
word.display()
