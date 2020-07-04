
import random
import time
Wins = 0
Loss = 0
def main():
    print("There are two games to play. A coin flip where you guess Heads or Tails and Cho-Han where you roll two dice and guess if the result is even or odd")
    
    while True:
        try:
            pick = int(input("Pick a game: 1 for coin flip or 2 for Cho-Han.\n"))
            
            if pick == 1:
                coinFlip()
                
            elif pick == 2:
                choHan()
        except ValueError:
            print("Enter a number: 1 or 2")
            
def coinFlip():
    global Wins
    global Loss
    
    guess = input("Heads or Tails\n")
    result = random.randint(1,2)
    
    if (guess == 'Heads' or guess == 'heads'):
        guess = 1
    elif (guess == 'Tails' or guess == 'tails'):
        guess = 2
    else:
        print("Guess must be Heads or Tails")
        coinFlip()
        
    print("Flipping a coin....")
    time.sleep(.8)
    
    if result == 1:
        print("The coin is heads")
    else:
        print("The coin is tails")
    
    time.sleep(.5)
    
    if result == guess:
        print("Your guess was correct")
        Wins += 1
    else:
        print("Your guess was wrong")
        Loss += 1
        
    print("Wins: ",Wins)
    print("Loss: ",Loss)
    
    repeat = input("Play again? Y/N\n")
    
    if repeat[0] == ("y" or "Y"):
        coinFlip()
    else:
        main()
        
def choHan():
    global Wins
    global Loss
    
    guess = input("Even or Odd\n")
    result = random.randint(1,6)
    result2 = random.randint(1,6)
    total = result + result2
    
    if (guess == 'Even' or guess == 'even'):
        guess = 0
    elif (guess == 'Odd' or guess == 'odd'):
        guess = 1
    else:
        print("Guess must be Even or odd")
        choHan()
        
    print("Rolling a couple of dice....")
    time.sleep(.8)
    
    print(total)
    if (total % 2 == 0):
        print("The result is even")
    elif (total % 2 == 1):
        print("The result is odd")
    
    time.sleep(.5)
    
    if (total % 2) == guess:
        print("Your guess was correct")
        Wins += 1
    else:
        print("Your guess was wrong")
        Loss += 1
        
    print("Wins: ",Wins)
    print("Loss: ",Loss)
    
    repeat = input("Play again? Y/N\n")
    
    if repeat[0] == ("y" or "Y"):
        choHan()
    else:
        main()
    
    