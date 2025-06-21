# Rock Paper Scissors Game
import time
import sys
import random

def write(text):
    """Print text with typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Initialize game statistics
wins = 0
losses = 0
ties = 0

def show_score():
    """Display current game statistics"""
    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
    print("-" * 30)

# Game options
agreement_list = ['yes', 'ya', 'sure', 'continue']
disagreement_list = ['no', 'na', 'nah', '', 'quit', 'exit', 'q', 'e']
signs = [
    ['rock', 'rocks', 'r'],
    ['paper', 'papers', 'p'],
    ['scissor', 'scissors', 's']
]

def handle_quit():
    """Handle quit game request"""
    write('Are you sure you want to quit?')
    response = input('Type yes or no: ').lower()
    
    if response in agreement_list:
        write('Bye. See You Later.')
        show_score()
        sys.exit()
    elif response in disagreement_list[:2]:
        write('Great! Let\'s continue playing!')
    else:
        write('Please type in between (yes or no): ')

# Main game loop
write('Welcome to Rock Paper Scissors!')
print('=' * 35)

while True:
    write('\nDo you want to play Rock, Paper, Scissors?')
    response = input('Type yes or no: ').lower()
    
    # Handle player response
    if response in agreement_list:
        write("Great! Let's play the game!")
        break
    elif response in disagreement_list:
        if response == '':
            handle_quit()
        else:
            write('Bye, see you!')
            show_score()
            sys.exit()
    else:
        write("Please type in between (yes or no)!")

# Game session
while True:
    write('\nStarting the game.........')
    player_move = input('Rock, paper or scissors?: ').lower()
    computer_move = random.choice(signs)
    
    # Handle quit during game
    if player_move in disagreement_list:
        handle_quit()
        continue
    
    # Check game results
    player_won = False
    tie = False
    
    if player_move in signs[0]:  # Rock
        if computer_move == signs[0]:
            tie = True
        elif computer_move == signs[1]:
            player_won = False
        else:  # Scissors
            player_won = True
            
    elif player_move in signs[1]:  # Paper
        if computer_move == signs[1]:
            tie = True
        elif computer_move == signs[0]:
            player_won = True
        else:  # Scissors
            player_won = False
            
    elif player_move in signs[2]:  # Scissors
        if computer_move == signs[2]:
            tie = True
        elif computer_move == signs[0]:
            player_won = False
        else:  # Paper
            player_won = True
            
    else:
        write('Please type rock, paper or scissors.')
        continue
    
    # Display results
    if tie:
        write('Oh ties! Try again!')
        ties += 1
    elif player_won:
        write('Hurrah! You won this time!')
        wins += 1
    else:
        write('You Lose! Please try again.')
        losses += 1
    
    show_score()
    
    # Ask to play again
    write('\nPlay another round?')
    again = input('Type yes or no: ').lower()
    
    if again in disagreement_list:
        handle_quit()
        break
    elif again not in agreement_list:
        write("I'll take that as a yes!")