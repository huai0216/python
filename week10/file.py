import os
import collections
from collections import defaultdict
filename = str(input("Enter a Python source filename: "))
file = open(filename,mode="r").read()
 


newnum= {}
newnum["import"] = file.count("import ")
newnum["while"] = file.count("while ")
newnum["if"] = file.count(' if ')
newnum["elif"] = file.count(' elif')
newnum["is"] = file.count(' is')
newnum["else"] = file.count(' else')

print(newnum)