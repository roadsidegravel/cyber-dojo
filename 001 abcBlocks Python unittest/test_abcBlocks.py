from abcBlocks import *
import unittest
      
        
class TestCheckBlockForLetter(unittest.TestCase):
    def test_is_not_on_block(self):
        desired = False
        block = ['A', 'B']
        letter = 'Z'
        result = check_block_for_letter(block, letter)
        self.assertEqual(desired, result)
        
    def test_is_on_block_top(self):
        desired = True
        block = ['A', 'B']
        letter = 'A'
        result = check_block_for_letter(block, letter)
        self.assertEqual(desired, result)
        
    def test_is_on_block_bottom(self):
        desired = True
        block = ['A', 'B']
        letter = 'B'
        result = check_block_for_letter(block, letter)
        self.assertEqual(desired, result)
        
        
class TestReturnListOfBlocksWithThisChar(unittest.TestCase):
    def test_result_length_A(self):
        desired = 2
        char = 'A'
        listBlocksWithChar = return_list_of_blocks_with_this_char(char)
        result = len(listBlocksWithChar)
        self.assertEqual(desired, result)
        
    def test_result_list_A(self):
        desired = [['N', 'A'], ['A', 'N']]
        char = 'A'
        result = return_list_of_blocks_with_this_char(char)
        self.assertEqual(desired, result)
   
    def test_result_length_exclaimation_mark(self):
        desired = 0
        char = '!'
        listBlocksWithChar = return_list_of_blocks_with_this_char(char)
        result = len(listBlocksWithChar)
        self.assertEqual(desired, result)
        
    def test_result_list_exlaimation_mark(self):
        desired = []
        char = '!'
        result = return_list_of_blocks_with_this_char(char)
        self.assertEqual(desired, result)
        

class TestCheckCanMakeWord(unittest.TestCase):
    def test_can_make_a(self):
        word = 'A'
        desired = True
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_can_make_bark(self):
        word = 'BARK'
        desired = True
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_cannot_make_book(self):
        word = 'BOOK'
        desired = False
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_can_make_treat(self):
        word = 'TREAT'
        desired = True
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_cannot_make_common(self):
        word = 'COMMON'
        desired = False
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_can_make_squad(self):
        word = 'SQUAD'
        desired = True
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_can_make_confuse(self):
        word = 'CONFUSE'
        desired = True
        result = check_can_make_word(word)
        self.assertEqual(desired, result)
        
    def test_allBlocks_unchanged(self):
        allBlocksCopy = allBlocks.copy()
        discard = check_can_make_word('A')
        discard = check_can_make_word('COMMON')
        discard = check_can_make_word('CONFUSE')
        self.assertEqual(allBlocksCopy, allBlocks)
        


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
