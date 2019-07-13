#Input of number of test cases
testCases = int(input())
#Input must be between 1 and 100.
if testCases >= 1 and testCases <= 100: #If condition is true then
    repeat = 0 #Iterate each testCase without for loop.
    results = []
    while repeat < testCases:
        #Ask for quantity of numbers contained in each testCase.
        testCaseLen = int(input()) #Must be between 1 and 100.
        if testCaseLen >= 1and testCaseLen <=100:#If condition is true then
            numberList = list(map(int, input().split())) #Ask for the numbers as a list. Separated by spaces.
             
            while len(numberList) == testCaseLen: #Quantity must be the same as input.
                square = 0
                sum = 0
                elements = 0
                number = 0 #Iterate all elements of list
                while number < len(numberList): #With the purpose of
                    if numberList[number] < 0:#If number contained in list is negative
                        numberList.remove(numberList[number])#Then remove it from list. 
                        continue #Jump loop
                    number += 1#add number
                while elements < len(numberList): #Iterate all elements of list
                    square = pow(numberList[elements],2) #Power each element ^2
                    sum = sum + square #The sum of squares of all elements.
                    elements += 1 #add number
                print(sum)
    


        

 
    