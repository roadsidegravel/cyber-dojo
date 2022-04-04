from bowlingScore import *
import unittest


class TestsPrepareScoreString(unittest.TestCase):
    def test_split_one_vertical(self):
        value = '4|5'
        desired = '45'
        result = prepare_score_string(value)
        self.assertEqual(desired, result)
    
    def test_split_double_vertical(self):
        value = 'X||1'
        desired = 'X!1'
        result = prepare_score_string(value)
        self.assertEqual(desired, result)
        
    def test_split_example_score_nines(self):
        value = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
        desired = '90909090909090909090!'
        result = prepare_score_string(value)
        self.assertEqual(desired, result)
        
    def test_split_example_score_mixed(self):
        value = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
        desired = 'X7/90X088/06XXX!81'
        result = prepare_score_string(value)
        self.assertEqual(desired, result)
        
    def test_input_unchanged(self):
        value = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
        desired = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
        discard = prepare_score_string(value)
        self.assertEqual(desired, value)
        
        
class TestsConvertScoreToNumbers(unittest.TestCase):
    def test_unknown_symbol_exception(self):
        value = '@'
        desired = "symbol @ in score not understood. @"
        with self.assertRaises(Exception) as e:
            discard = convert_score_to_number_list(value)
        message = str(e.exception)
        self.assertEqual(desired, message)
        
    def test_nothing_nothing_once(self):
        value = '00'
        desired = [0, 0]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_something_nothing_once(self):
        value = '50'
        desired = [5, 0]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_nothing_something_once(self):
        value = '03'
        desired = [0, 3]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_all_nine_nothing(self):
        value = '90909090909090909090!'
        desired = [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_only_strike(self):
        value = 'X'
        desired = [10]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_strike_and_two_balls(self):
        value = 'X12'
        desired = [13, 1, 2]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_strike_and_two_bonus_balls(self):
        value = 'X!12'
        desired = [13]
        result = convert_score_to_number_list(value)
        self.assertEqual(desired, result)
        
    def test_input_unchanged(self):
        value = 'X7/90X088/06XXX!81'
        desired = 'X7/90X088/06XXX!81'
        discard = convert_score_to_number_list(value)
        self.assertEqual(desired, value)
        
class TestsCalculateTotalScore(unittest.TestCase):
    def test_all_nine_nothing(self):
        value = '9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||'
        desired = 90
        result = calculate_total_score_of_bowling_game(value)
        self.assertEqual(desired, result)
        
    def test_all_nine_nothing(self):
        value = '5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5'
        desired = 150
        result = calculate_total_score_of_bowling_game(value)
        self.assertEqual(desired, result)
        
    def test_all_strikes(self):
        value = 'X|X|X|X|X|X|X|X|X|X||XX'
        desired = 300
        result = calculate_total_score_of_bowling_game(value)
        self.assertEqual(desired, result)
    
    def test_mixed(self):
        value = 'X|7/|9-|X|-8|8/|-6|X|X|X||81'
        desired = 167
        result = calculate_total_score_of_bowling_game(value)
        self.assertEqual(desired, result)
        
      
        
    


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
