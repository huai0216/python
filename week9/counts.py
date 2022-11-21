st = str(input("Enter a string:"))
c_array = [int(a) for a in str(st) if a.isdigit()]

def counter(s):
    counts = []
    for i in range(len(s)):
        counts.append(s.count(i)) 
        # if counts[i] != 0:
    
    return counts
        
for i in range(len(counter(c_array))):
    if counter(c_array)[i] != 0:
        print("{} occurs {} time".format(i,counter(c_array)[i]))