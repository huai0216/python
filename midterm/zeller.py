year = eval(input("Enter year(e.g.,2020):"))
month = eval(input("Enter month(1-12):"))
q =  eval(input("Enter the day of the month(1-31):"))
#day = ""
j = year // 100
k = year % 100
m = month % 13
if month == 1 or month == 2:
    year = year-1
    m = month + 12
else :
    m = month 
m_h = (26 * (m+1)) // 10
k_h = k // 4
j_h = j // 4 
h = (q + (m_h) + k + k_h + j_h + 5*j)%7
def day(i):
    if i == 0:
        return "Saturday"
    elif i == 1:
        return "Sunday"
    elif i == 2:
        return "Monday"
    elif i == 3:
        return "Tuesday"
    elif i == 4:
        return "Wednesday"
    elif i == 5:
        return "Thursday"
    elif i == 6:
        return "Friday"
    else:
        return

def main():
    print("Day of the week is {}".format(day(h)))
main()
