dollar = eval(input('Input an amount as integer:'))
dollarOffifty = dollar//50 
remainbyfifty = dollar %50
dollarOften = remainbyfifty //10
remainbyten = remainbyfifty % 10
dollarOffive = remainbyten // 5
remainbyfive = remainbyten % 5


print("Your amount "+str(dollar)+" consists of\n"+str(dollarOffifty)+ " fifty dollars\n"\
    +str(dollarOften)+" ten dollars\n"+str(dollarOffive)+" five dollars\n"\
        +str(remainbyfive)+ " one dollars")