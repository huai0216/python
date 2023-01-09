import re

id_number = input('Please Enter your ID No.: ')



def validate_id_number(id_number):
    # 使用正則表達式驗證身份證號碼是否符合格式要求
    pattern = r'^[A-Z][0-9]{9}$'
    if not re.match(pattern, id_number):
        return False
    
    # 將字母轉換成相對應的數字
    letter_map = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17",
                  "I": "34", "J": "18", "K": "19", "L": "20", "M": "21", "N": "22", "O": "35", "P": "23",
                  "Q": "24", "R": "25", "S": "26", "T": "27", "U": "28", "V": "29", "W": "32", "X": "30",
                  "Y": "31", "Z": "33"}
    id_number = letter_map[id_number[0]] + id_number[1:]
    
    # 將身份證號碼中的每一位數字與其相對應的權重相乘後加總
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    total = sum([int(id_number[i]) * weights[i] for i in range(11)])
    
    # 判斷結果是否為 10 的倍數
    return total % 10 == 0

if validate_id_number(id_number) == True :
    print('Id. number {} is valid'.format(id_number))
else :
    print('Id. number {} is invalid'.format(id_number))