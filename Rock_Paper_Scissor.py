import random
options = ["rock", "paper", "scissors"]

while True:
 plr_choice = input("Rock Paper Scissors? (rock/ paper/ scissors): ").lower()
 comp_choice = random.choice(options)
 if plr_choice not in options:
       print("Invalid Input. Please enter 'rock', 'paper', or 'scissors'.")
       continue
 print(f"You Chose {plr_choice} ")
 print(f"Computer Chose {comp_choice} ")

 if plr_choice == comp_choice:
    print("Its a Tie")
 else:
      if(
          (plr_choice == "paper" and comp_choice == "rock") or
          (plr_choice == "scissors" and comp_choice == "paper") or
          (plr_choice == "rock" and comp_choice == "scissors")
      ):
          print("Player Wins")
      else:
          print("Computer Wins")

      continue_game = input("Want To Continue? (y/n): ")
      if continue_game == "y":
          continue
      elif continue_game == "n":
          print("Thanks For Playing")
          break
      else:
          break
      

