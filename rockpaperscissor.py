
import random

player1 = input("Enter 'Rock','Paper','Scissor':  ")
player2 = random.choice(['Rock','Paper','Scissor']).lower()
print("player2 selected :  ", player2)

if player1 =='paper' and player2 =='scissor' :
    print("player1 lost the game and player2 win the game ")

elif player1 == 'rock' and player2 == 'scissor':
    print("player1 win the game and player2 lost the game ")

elif player1 == 'paper' and player2 == 'rock':
    print("player1 win the game and player2 lost the game ")

elif player1 == 'scissor' and player2 == 'paper':
    print("player1 win the game and player2 lost the game ")

elif player1 == 'rock' and player2 == 'paper':
    print("player1 lost the game and player2 win the game ")

elif player1 == 'scissor' and player2 == 'rock':
    print("player1 lost the game and player2 win the game ")
    
else:
    player1 and player2 =='rock'
    player1 and player2 =='paper'
    player1 and player2 =='scissor'
    print("its a tie")
    




