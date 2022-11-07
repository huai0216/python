import random
import math

diceint1 = random.randint(1,6)
diceint2 = random.randint(1,6)
sum = diceint1 + diceint2
print("You rolled {} + {} = {}".format(diceint1, diceint2, sum))
print("point is {}".format(sum))
if sum == 7 or sum == 11:
    print('You win')
else:
    while(1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)   
        sum2 = dice1 + dice2
        if(sum2 == sum):
            print("You rolled {} + {} = {}".format(dice1, dice2, sum2))
            print('You win')
            break
        elif(sum2 == 7):
            print("You rolled {} + {} = {}".format(dice1, dice2, sum2))
            print("You lose")
            break
        else:
            print("You rolled {} + {} = {}".format(dice1, dice2, sum2))


            


   

# def game(dicein1, diceint2):
#     sum = diceint1 + diceint2
#     while(sum != 7):
#         return "You win"
#     else :
#         return
# while(sum = 7):
#     sum()

# def sum():
#     print("You rolled {} + {} = {}".format(diceint1, diceint2, result))

# main()