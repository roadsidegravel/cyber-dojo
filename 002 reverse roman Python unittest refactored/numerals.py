'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''

def denumeralize(value):
    if not isinstance(value, str):
        raise Exception(f'denumeralize expects a string, not {type(value)} {value}')
    if len(value) == 0:
        raise Exception(f'denumeralize expects a string with length > 0')
    numberList = create_number_list(value)
    compactedNumberList = add_up_identical_neighbours(numberList)
    subtractedNumberList = subtract_when_smaller_than_next(numberList)
    result = sum(subtractedNumberList)
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

def add_up_identical_neighbours(numberList):
    result = []
    neighbourSum = 0
    for index, number in enumerate(numberList):
        if index == len(numberList) -1:
            nextNumber = 0
        else:
            nextNumber = numberList[index + 1]
        neighbourSum += number
        if number != nextNumber:
            result.append(neighbourSum)
            neighbourSum = 0
    return result

def subtract_when_smaller_than_next(numberList):
    result = [numberList[0]]
    previousNumber = 0
    for number in numberList[1:]:           
        if result[-1] < number:
            result[-1] = number - result[-1]
        else:
            result.append(number)
    return result
