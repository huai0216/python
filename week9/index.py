bubble = list(map(int,input("Enter list element separated by spaces from one line:").split()))
def  indexOfSmallestElement(lst):
    current_index = 1
    min_index = 0
    while current_index < len(lst):
        if lst[current_index]<lst[min_index]:
            min_index = current_index
        current_index = current_index +1
    return min_index

def indexOfGreatestelement(lst):
    current_index = 1
    max_index = 0
    while current_index < len(lst):
        if lst[current_index]>lst[max_index]:
            max_index = current_index
        current_index = current_index + 1
    return max_index
print("The index of the smallest element is {}".format(indexOfSmallestElement(bubble)))
print("The index of the greatest element is {}".format(indexOfGreatestelement(bubble)))