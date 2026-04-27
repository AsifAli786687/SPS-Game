
from userguess import usrguess
from compguess import comguess


def SPS():

  user = usrguess()
  comp = comguess()
    
  print("User chose:", user)
  print("Computer chose:", comp)

  if user == comp:
    print("Match draw")

  elif (
        (user == "Stone" and comp == "Scissor") or
        (user == "Paper" and comp == "Stone") or
        (user == "Scissor" and comp == "Paper")
    ):
      print("You win")

  else:
      print("You lose")

while True:
   SPS()

