bubble = []
bubble = list(map(int,input("Enter numbers:").split()))
n = len(bubble)
for i in range(n):
    for j in range(n-i-1):
        if bubble[j]>bubble[j+1]:
            bubble[j],bubble[j+1] = bubble[j+1],bubble[j]

print(bubble)