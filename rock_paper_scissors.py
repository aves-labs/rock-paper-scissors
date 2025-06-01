import random, time, sys

# Custom print function to simulate a typewriter effect (makes it feel dramatic)
def printx(text):
    for char in text:
        print(char, flush=True, end='')
        time.sleep(0.03)
    print()

# Game intro
printx("Rock, Paper, Scissors Game")
printx("Enter (r)ock, (p)aper, (s)cissor or (q)uit.")

# Scoreboard counters
wins = 0
losses = 0
ties = 0

# Main game loop — keeps running until the user quits
while True:
    printx('%s wins, %s losses, %s ties' % (wins, losses, ties))
    playerMove = input("Type Here: ").lower()

    # Exit the game
    if playerMove == 'q' or playerMove == 'quit':
        printx("Bye")
        sys.exit()

    # Process player input and show move
    if playerMove == 'r' or playerMove == 'rock':
        playerMove = 'r'
        printx("Rock vs ............")
    elif playerMove == 'p' or playerMove == 'paper':
        playerMove = 'p'
        printx('Paper vs...........')
    elif playerMove == 's' or playerMove == 'scissor':
        playerMove = 's'
        printx('Scissor vs..........')
    else:
        printx("Invalid input! Only type r, p, s, or q.")
        continue  # Go back to the top and try again

    # Computer randomly picks a move
    xNumber = random.randint(1, 3)
    if xNumber == 1:
        computerMove = 'r'
        printx('Rock')
    elif xNumber == 2:
        computerMove = 'p'
        printx('Paper')
    else:
        computerMove = 's'
        printx('Scissor')

    # Compare player vs computer and update score
    if playerMove == computerMove:
        printx('Oh ties!')
        ties += 1
    elif playerMove == 'r' and computerMove == 'p':
        printx("You lose :(")
        losses += 1
    elif playerMove == 'r' and computerMove == 's':
        printx("You win :)")
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        printx('You win :)')
        wins += 1
    elif playerMove == 'p' and computerMove == 's':
        printx('You lose :(')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        printx('You lose :(')
        losses += 1
    elif playerMove == 's' and computerMove == 'p':
        printx('You Win :)')
        wins += 1
