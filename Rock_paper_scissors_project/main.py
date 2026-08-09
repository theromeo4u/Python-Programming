# import random
# '''
# -1 for Rock
# 1 for scissors
# 0 for paper
# '''
# user_score = 0
# computer_score = 0


# computer = random.choice([-1,1,0])
# youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ").lower()
# yourDict = {'r': -1, 's': 1, 'p': 0}
# reverseDict = {-1: "Rock", 1: "Scissors", 0: "Paper"}

# if youstr not in yourDict:
#     print("Invalid Input choose (r = Rock, p = Paper, s = Scissors): ") 
#     exit()
    
# you = yourDict[youstr]

# print(f"You choose '{reverseDict[you]}' and Computer choose '{reverseDict[computer]}'")


# if computer == you:
#     print("It's a Draw!")

# elif computer == -1 and you == 0:
#     print("You Win!")      # Paper beats Rock

# elif computer == 0 and you == 1:
#     print("You Win!")      # Scissors beats Paper

# elif computer == 1 and you == -1:
#     print("You Win!")      # Rock beats Scissors

# else:
#     print("You Lose!")


import random

userScore = 0
computerScore = 0

while True:
    '''
    -1 for Rock
    1 for scissors
    0 for paper
    '''
    computer = random.choice([-1,1,0])
    youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ").lower()
    yourDict = {'r': -1, 's': 1, 'p': 0}
    reverseDict = {-1: "Rock", 1: "Scissors", 0: "Paper"}

    if youstr not in yourDict:
        print("Invalid Input choose (r = Rock, p = Paper, s = Scissors): ")
        continue

    you = yourDict[youstr]

    print(f"You choose '{reverseDict[you]}' and Computer choose '{reverseDict[computer]}'")

    if computer == you:
        print("It's a Draw!")

    elif computer == -1 and you == 0:
        print("You Win!")
        userScore += 1

    elif computer == 0 and you == 1:
        print("You Win!")
        userScore += 1

    elif computer == 1 and you == -1:
        print("You Win!")
        userScore += 1

    else:
        print("You Lose!")
        computerScore += 1

    print(f"\nScore")
    print(f"You : {userScore}")
    print(f"Computer : {computerScore}")

    playAgain = input("\nDo you want to play again? (y/n): ").lower()

    if playAgain != 'y':
        break

print("\nGame Over!")
print(f"Final Score")
print(f"You : {userScore}")
print(f"Computer : {computerScore}")