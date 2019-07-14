
inputs = []

number_list = list(map(int, input().split()))

number = 0
elements = 0
sum = 0
square = 0

if len(number_list) > 1:
    while number < len(number_list):
        if number_list[number] < 0:
            number_list.remove(number_list[number])
            continue
        number += 1
    while elements < len(number_list):
        square = pow(number_list[elements],2)
        sum = sum + square
        elements += 1

    print(sum)

elif len(number_list) == 1:
    pass
else:
    pass
   