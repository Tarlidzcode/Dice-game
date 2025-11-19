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
      if PlayerScore > ComputerScore :
            print("Congratulations you win!!!")
      
      elif ComputerScore > PlayerScore:
            print("Computer wins")
            
      else:
            print("Its a draw")
      
      play_again = input("Play again? (yes/no):    ")
      if play_again.lower() != 'yes':
            break
    
    

gameplay()
