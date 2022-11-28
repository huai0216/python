occ = list(map(int,input("Enter the numbers:").split()))
maxlabel = []
cur = max(occ,key=occ.count)
maxlabel.append(max(occ,key=occ.count))
num1 = occ.count(max(occ,key=occ.count))
for i in range(len(occ)):
    k = 0
    for j in range(len(maxlabel)):
        if occ.count(occ[i]) == num1:
            if maxlabel.count(occ[i])<1:
                maxlabel.append(occ[i])
            else : 
                pass
    else:
        pass      
  

print("The numbers with the most occurrence are: ",end = "")
for i in range(len(maxlabel)):
    print(maxlabel[i],end=" ")