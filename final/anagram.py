word1 = input('Enter the first string: ')
word2 = input('Enter the second string: ')

def isAnagram(word1, word2):
    return sorted(word1) == sorted(word2)

if isAnagram(word1, word2) == True:
    print('{} and {} are anagram.'.format(word1,word2))
else :
    print('{} and {} are not anagram.'.format(word1, word2))

