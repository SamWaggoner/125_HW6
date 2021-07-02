# This is the updated version that I made on 7/2/21
# This program will ask input for a list then determine the mode.
def determinemode():
    numlist = []
    freqlist = []
    print("Hello! I will calculate the longest sequence of numbers in a list.")
    print("Type your list of numbers and then type \"end\".")
    num = (input("Please enter a number: "))
    
    def CheckNum(num):
        try:
            num = int(num)
            return True
        except ValueError:
            return False
            
    while CheckNum(num) != False:
        numlist.append(int(num))
        num = ((input("Please enter a number: ")))
    print(numlist)
    
    currFreq = 1
    modeNum = -1
    maxNumOccurrences = 1
    for i in range(len(numlist)-2):
        if numlist[i] == numlist[i+1]:
            currFreq += 1
            if currFreq > maxNumOccurrences:
                maxNumOccurrences = currFreq
                modeNum = numlist[i]
        else:
            currFreq = 1
            
    if len(numlist) == 0:
        print("There is no mode, the list provided is empty.")
        
    elif modeNum == -1:
        print("There is no mode, all of the numbers occur an equal number of times.")
            
    else:
        print("The mode is " + str(modeNum) + " which occurred " + str(maxNumOccurrences) + " times.")
        
determinemode()
while input("Would you like to find another mode from a new list? (Type \"yes\"): ") == "yes":
    determinemode()
    
print("Okay, glad I could help!")

# This is the original program that I made while in school as homework.
# File: hw6a.py
# Author: Sam Waggoner
# Date: 10/25/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Create a count for the largest number of subsequent numbers entered by the user.
# Collaboration:
# I did not discuss this assignment with anyone other than the course staff. (I
# got help from Matt.)

def main():

    numlist = []
    freqlist = []
    print("Hello! I will calculate the longest sequence of numbers in a list.")
    print("Type your list of numbers and then type end.")
    num = (input("Please enter a number: "))
    while num!= "end":
        numlist.append(int(num))
        num = ((input("Please enter a number: ")))
    print(numlist)
    freq = 1
    currfreq = 1
    numfreq = 0
    for i in range(len(numlist)-1):
        if numlist[i] == numlist[i+1]:
            currfreq += 1
        if currfreq > freq:
            freq = currfreq
            currfreq = 1
            numfreq = numlist[i]
    print("The most frequent number was "+str(numfreq)+" which was printed "+str(freq)+" times.")

main()
