'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''

def calculate_total_score_of_bowling_game(scoreString):
    preparedScore = prepare_score_string(scoreString)
    numbers = convert_score_to_number_list(preparedScore)
    result = sum(numbers)
    return result

def prepare_score_string(scoreString):
    scoreString = scoreString.replace('||','!')
    scoreString = scoreString.replace('|','')
    result = scoreString.replace('-','0')
    return result

def convert_score_to_number_list(score):
    result = []
    game = score+'!'
    splitGame = game.split('!')
    balls = splitGame[0]
    bonusBalls = splitGame[1]
    allBalls = balls + bonusBalls + '00'
    for index,char in enumerate(balls):
        number = 0
        if char.isdigit():
            number += int(char)
        elif char == '/':
            previousScore = int(game[index-1])
            number += 10 - previousScore
            nextBall = allBalls[index+1]
            nextBall = nextBall.replace('X', '10')
            bonusScore = int(nextBall)
            number += bonusScore
        elif char == 'X':
            number += 10
            nextBall = allBalls[index+1]
            nexterBall = allBalls[index+2]
            if nexterBall == '/':
                bonusScore = 10
            else:
                nextBall = nextBall.replace('X', '10')
                nexterBall = nexterBall.replace('X', '10')
                bonusScore = int(nextBall) + int(nexterBall)
            number +=bonusScore
        else:
            raise Exception(f'symbol {char} in score not understood. {score}')
        result.append(number)             
    return result