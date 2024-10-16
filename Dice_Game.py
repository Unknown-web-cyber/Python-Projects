import random
choice = None

print("Welcome to the Dice Rolling Game! 🎲")
while choice != "n":
 choice = input("Roll the Dice? (y/n): ").lower()
 
 if (choice == "y"):
     dice_1 =random.randint(1,6)
     dice_2 =random.randint(1,6)
     print(f"You rolled: {dice_1} and {dice_2}")
 
 elif(choice =="n"):
     print("Thanks for Playing the game")

 else:
    print("Invalid Choice")
