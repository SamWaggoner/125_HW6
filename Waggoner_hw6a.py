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