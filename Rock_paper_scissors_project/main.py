import random
'''
-1 for Rock
1 for scissors
0 for paper
'''
computer = random.choice([-1,1,0])
youstr = input("Enter your choice (r = Rock, p = Paper, s = Scissors): ").lower()
yourDict = {'r': -1, 's': 1, 'p': 0}
reverseDict = {-1: "Rock", 1: "Scissors", 0: "Paper"}

you = yourDict[youstr]

print(f"You choose '{reverseDict[you]}' and Computer choose '{reverseDict[computer]}'")

if computer == you:
    print("It's a Draw!")

elif computer == -1 and you == 0:
    print("You Win!")      # Paper beats Rock

elif computer == 0 and you == 1:
    print("You Win!")      # Scissors beats Paper

elif computer == 1 and you == -1:
    print("You Win!")      # Rock beats Scissors

else:
    print("You Lose!")