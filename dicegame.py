import random

min = 1
max = 6
PlayerScore = 0
ComputerScore = 0
InPlay = True

def gameplay():
     while InPlay:
      PlayerScore=random.randint(min,max)
      ComputerScore=random.randint(min,max)
      print(f"You got {PlayerScore} vs CPU got {ComputerScore}")
      break
    
    
gameplay()