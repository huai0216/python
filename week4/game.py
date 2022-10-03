import math
import random
yoursint = eval(input("scissor(0), rock(1), paper(2):"))
if yoursint == 0:
    yours = "scissor"
elif yoursint == 1:
    yours = "rock"
else : 
    yours = "paper"
computerint = random.randint(0,2)
if computerint == 0:
    computer = "scissor"
    if yoursint == 0:
        yours = "scissor too"
        result = "It is a draw"
    elif yoursint == 1:
        result = "You won!"
    else :
        result = "You lost!"
elif computerint  == 1 :
    computer = "rock"
    if yoursint == 0:
        result = "You lost!"
    elif yoursint == 1:
        yours = "rock too"
        result = "It is a draw"
    else :
        result = "You won!"
else :
    computer = "paper"
    if yoursint == 0:
        result = "You won!"
    elif yoursint == 1:
        result = "You lost!"
    else :
        yours = "paper too"
        result = "It is a draw"

print("The computer is "+str(computer)+". You are "+str(yours)+". "+str(result))