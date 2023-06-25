#create an input for rock, paper, scissor 
#put it into a variable for player
#(i can also make a player name input and assign it to the input for rock paper scissors)
#i would need to create a start button in a function maybe 
#probably put that function assigned to player name input
# then i create a computer player that displays a random option after player name input
# so that will fire after input selection
# if player chooses , then computer chooses
# then use an if then statemnt to compare the two 
# apply rounds where the score gets incremented by 2 global variables 
#compare results after lets say 5 rounds


import random #must import before we use it
player_score = 0
comp_score = 0

options = ['rock', 'paper', 'scissors']

while True:
    player_input = input('ro sham bo or q to quit: ')
    if player_input == 'q':
       break

    if player_input not in options: # or ['rock', 'paper', 'scissors']: #checking if the player typed in rock, paper, scissors
        #a trick to check multiple things in 1 line
        continue #python - goes back to the top of the while loop aka re asks them the input since we put the variable in the line

    random_number = random.randint(0,2)
    #rock: 0, paper:1, scissor:2
    computer_pick = options[random_number]
    print('computer picked', computer_pick + ".")

    if player_input == "rock" and computer_pick == "scissors":
        print('you won')
        player_score += 1
        # we check the elifs if this is false, if the elifs are false then we check the else 
        

    elif player_input == "paper" and computer_pick == "rock":
        print('you won')
        player_score += 1
        

    elif player_input == "scissors" and computer_pick == "paper":
        print('you won')
        player_score += 1
    

    else:
        print('you lost') #no point in checking if the computer beat us becausethe above are our only options of winning
        comp_score += 1

#this occurs outside of the while loop
#meaning that when we break we access these prints
# and we break out by hitting q
# so this while loop will go and loop up and down until it breaks
if player_score > comp_score:
    print('you won', player_score, 'times')
else: 
    print('the computer won', comp_score, 'times')
print('goodbye')

