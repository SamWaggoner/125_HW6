# File: hw6b.py
# Author: Sam Waggoner
# Date: 10/27/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Create a list from inputs then insert numbers sequentially.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff. Matt
# helped me by instructing me to define and use more functions.

def makeList():
    numlist = []
    num = (input("Please enter an integer: "))
    while num!= "end":
        numlist.append(int(num))
        num = ((input("Please enter an integer: ")))
    print(numlist)
    return numlist
def sortcheck(numlist):
    if (len(numlist)) == 1:
            t_or_f = True
            return t_or_f
    else:
        for i in range(len(numlist)-1):
            if numlist[i] < numlist[i+1]:
                t_or_f = True
            if numlist[i] > numlist[i+1]:
                t_or_f = False
        return t_or_f

def insert(numlist):
    newnum = (input("Integer to insert: "))
    while newnum != "end":
        if int(newnum) in numlist:
            print("This number is already in the list.")
            newnum = "end"
        else:
            index = 0
            for i in range(len(numlist)):
               if int(newnum) >= int(numlist[i]):
                   index += 1
            numlist.insert(index,newnum)
            newnum = (input("Integer to insert: "))
    return numlist

def main():
    numlist = makeList()
    if sortcheck(numlist) == True:
        list_without_quotes = insert(numlist)
        for i in range(len(list_without_quotes)):
            list_without_quotes[i] = int(list_without_quotes[i])
        print(list_without_quotes)
main()





# Version that will continue asking for numbers even if a repeat number is typed in:
"""
def makeList():
    numlist = []
    num = (input("Please enter an integer: "))
    while num!= "end":
        numlist.append(int(num))
        num = ((input("Please enter an integer: ")))
    print(numlist)
    return numlist
def sortcheck(numlist):
    if (len(numlist)) == 1:
            t_or_f = True
            return t_or_f
    else:
        for i in range(len(numlist)-1):
            if numlist[i] < numlist[i+1]:
                t_or_f = True
            if numlist[i] > numlist[i+1]:
                t_or_f = False
        return t_or_f

def insert(numlist):
    newnum = (input("Integer to insert: "))
    while newnum != "end":
        if int(newnum) in numlist:
            print("This number is already in the list.")
        else:
            index = 0
            for i in range(len(numlist)):
               if int(newnum) >= int(numlist[i]):
                   index += 1
            numlist.insert(index,newnum)
        newnum = (input("Integer to insert: "))
    return numlist

def main():
    numlist = makeList()
    if sortcheck(numlist) == True:
        list_without_quotes = insert(numlist)
        for i in range(len(list_without_quotes)):
            list_without_quotes[i] = int(list_without_quotes[i])
        print(list_without_quotes)
    else:
        print("")
main()
"""

