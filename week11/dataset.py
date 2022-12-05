import random
import os


f = open('Salary.txt','a+')
with open('Salary.txt','r+') as test:
    read_data = test.read()
    test.seek(0)
    test.truncate()

for i in range(1001):
    full_sal = str(random.randint(75000,130000))
    assoc_sal = str(random.randint(60000,110000))
    assis_sal = str(random.randint(50000,80000))
    prof = random.randint(0,2)
    if prof == 0:
        jobtitle = "Full\t"
        salary = full_sal
    elif prof == 1:
        jobtitle = "Associate"
        salary = assoc_sal
    else :
        jobtitle = "Assistant"
        salary = assis_sal
    f.write(str("Firstname{}\tLastName{}\t{}\t\t{}\n".format(i,i,jobtitle,salary)))
f.seek(0,0)
print(f.read())
f.close()