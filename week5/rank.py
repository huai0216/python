students = int(input('Enter the number of studetns:'))
score = 0
topscore = 0
secondscore = 0
name = ''
topname =''
secondname = ''
for i in range (students) :
    name = input('Enter a student name:')
    score = eval(input('Enter a student score:'))
    if(score > secondscore):
        if(score > topscore):
            topscore = score
            topname = name
        else :
            secondscore = score
            secondname = name
    elif(score < secondscore):
        topscore = topscore
        topname = topname
        secondscore = secondscore
        secondname = secondname
print("Top two student:\n{}'s score is : {}\n{}'s score is: {}"\
        .format(topname,topscore,secondname,secondscore))
