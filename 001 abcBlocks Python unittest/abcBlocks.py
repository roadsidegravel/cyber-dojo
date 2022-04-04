from collections import Counter

allBlocks = [['B', 'O'],
             ['X', 'K'],
             ['D', 'Q'],
             ['C', 'P'],
             ['N', 'A'],
             ['G', 'T'],
             ['R', 'E'],
             ['T', 'G'],
             ['Q', 'D'],
             ['F', 'S'],
             ['J', 'W'],
             ['H', 'U'],
             ['V', 'I'],
             ['A', 'N'],
             ['O', 'B'],
             ['E', 'R'],
             ['F', 'S'],
             ['L', 'Y'],
             ['P', 'C'],
             ['Z', 'M']]


def check_block_for_letter(block, letter):
    result = False
    if letter in block:
        result = True
    return result
    
def return_list_of_blocks_with_this_char(char):
    blocksWithChar = []
    for block in allBlocks:
        if check_block_for_letter(block, char):
            if block not in blocksWithChar:
                blocksWithChar.append(block)
    return blocksWithChar

def check_have_enough_blocks(blocksList, limit):
    if len(blocksList) >= limit:
        return True
    else:
        return False

def check_can_make_word(word):
    characterCounter = Counter(word)
    characterResultList = []
    blocksUsed = []
    for char in characterCounter:
        blocksWithChar = return_list_of_blocks_with_this_char(char)
        for block in blocksWithChar:
            if block not in blocksUsed:
                blocksUsed.append(block)
        charCount = characterCounter[char]
        charResult = check_have_enough_blocks(blocksWithChar, charCount)
        characterResultList.append(charResult)
    allCharacterCheck = False not in characterResultList
    if allCharacterCheck is False:
        wordResult = False
    else:
        wordResult = check_have_enough_blocks(blocksUsed, len(word))
    return wordResult
