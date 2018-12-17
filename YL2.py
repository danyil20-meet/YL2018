
# EX 1

##b = []
##def func(list):
##    b.append(list[0])
##    b.append(list[-1])
##    print(b)
##func([1 , 3, 4])

# EX 2

##num = (int)(input("Enter the num: "))
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##b = []
##
##for i in range(len(a) - 1):
##    if a[i] < num:
##        b.append(a[i])
##print(b)

#EX 3

##import random
##
##a = []
##b = []
##answer = []
##
##ind = 1
##
##x = random.randint(1, 11)
##y = random.randint(1, 11)
##
##for i in range(x):
##    num = random.randint(1, 11)
##    a.append(num)
##print('The first list is ' + str(a))
##
##    
##for i in range(x):
##    num = random.randint(1, 11)
##    b.append(num)
##print('The second list is ' + str(b))
##
##if(len(a) > len(b) or len(a) == len(b)):
##    length = len(b)
##else:
##    length = len(a)
##
##    
##for i in range(length):
##    if a[i] in b:
##        answer.append(a[i])
##for i in range(len(answer)):
##               if (answer[0] == answer[ind]):
##                   del(answer[0])
##                   ind += 1
##print(answer)

#EX 4

import tkinter as tk
from tkinter import simpledialog

answer = (int)(simpledialog.askstring("Input", "Enter the number: ", parent=tk.Tk()))
boolean = 0

for i in range(2, answer-1):
    if(answer%(i) == 0):
        print('Nope')
        boolean = 0
        break
    else:
        print('Maybe')
        boolean = 1

if (boolean == 1):
    print('YES')
     

