import random


def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return '- debug test - name_to_number - ' + name


def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return '- debug test - number_to_name - ' + number


def rpsls(player_choice): 

    
    player_number = name_to_number(player_choice)

    
    comp_number = random.randrange(0, 4)

    
    comp_choice = number_to_name(comp_number)
    
    
    winner = (comp_number - player_number) % 5

    
    print ('Player chooses ' + player_choice)

   
    print ('Computer chooses ' + comp_choice)

    
    if winner == 0:
        print ('Player and computer tie!')
    elif winner >= 3:
        print ('Player wins!')
    elif winner > 0 and winner <= 2:
        print ('Computer wins!')
    else:
        print ('- debug test - Printing the winner - ' + winner)
    
    
    print


rpsls('rock')
rpsls('spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')