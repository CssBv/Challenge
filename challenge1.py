#Input of numberIndex of test cases
testCases = int(input())
#Input must be between 1 and 100.
if testCases >= 1 and testCases <= 100: #If condition is true then
    repeat = 0 #Iterate each testCase without for loop.
    results = []
    
    while repeat < testCases:
        #Ask for quantity of numbers contained in each testCase.
        testCaseLen = int(input()) #Must be between 1 and 100.
        if testCaseLen >= 1 and testCaseLen <= 100:#If condition is true then
            numberList = list(map(int, input().split())) #Ask for the numbers as a list. Separated by spaces.
             
            if len(numberList) == testCaseLen: #Quantity must be the same as input.
                
                numberIndex = 0 #Iterate all elementIndex of list
                
                while numberIndex < len(numberList): #With the purpose of
                    if numberList[numberIndex] < 0:#If numberIndex contained in list is negative
                        numberList.remove(numberList[numberIndex])#Then remove it from list. 
                        continue #Jump loop
                    numberIndex += 1#add numberIndex
                elementIndex = 0
                
                sum = 0
                while elementIndex < len(numberList): #Iterate all elementIndex of list
                    square = pow(numberList[elementIndex],2) #Power each element ^2
                    sum = sum + square #The sum of squares of all elementIndex.
                    elementIndex += 1 #add numberIndex
                results.append(sum)
            
        repeat += 1
    i = 0 
      
    while i < len(results):
        print(results[i])
        i += 1
               
               

               

        

 
    