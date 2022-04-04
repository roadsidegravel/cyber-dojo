'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''

def denumeralize(value):
    numberList = create_number_list(value)
    result = sum_the_numbers(numberList)
    return result

def create_number_list(value):
    numberList = []
    for c in value:
        if c == "I":
            number = 1
        elif c == "V":
            number = 5
        elif c == "X":
            number = 10
        elif c == "L":
            number = 50
        elif c == "C":
            number = 100
        elif c == "D":
            number = 500
        elif c == "M":
            number = 1000
        else:
            raise Exception(c + " means nothing to me")
        numberList.append(number)
    return numberList

def sum_the_numbers(numberList):
    result = 0
    midsum = 0
    for index, number in enumerate(numberList):
        if index == len(numberList) - 1:
            result += midsum
            result += number
        else:
            nextNumber = numberList[index + 1]
            if number == nextNumber:
                midsum += number
            if number > nextNumber:
                result += midsum
                result += number
                midsum = 0
            if number < nextNumber:
                result -= midsum
                result -= number
                midsum = 0
    return result
