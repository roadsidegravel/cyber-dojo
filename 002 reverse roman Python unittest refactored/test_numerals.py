from numerals import *
import unittest

class TestDenumeralize(unittest.TestCase):

    def test_i(self):
        value = "I"
        desired = 1
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_ii(self):
        value = "II"
        desired = 2
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_iii(self):
        value = "III"
        desired = 3
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_iv(self):
        value = "IV"
        desired = 4
        result = denumeralize(value)
        self.assertEqual(desired, result)

    def test_v(self):
        value = "V"
        desired = 5
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_vi(self):
        value = "VI"
        desired = 6
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_cd(self):
        value = "CD"
        desired = 400
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_dc(self):
        value = "DC"
        desired = 600
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_mcmxc(self):
        value = "MCMXC"
        desired = 1990
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_mmviii(self):
        value = "MMVIII"
        desired = 2008
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_xcix(self):
        value = "XCIX"
        desired = 99
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_xlvii(self):
        value = "XLVII"
        desired = 47
        result = denumeralize(value)
        self.assertEqual(desired, result)
        
    def test_input_unchanged(self):
        value = "XLVII"
        desired = "XLVII"
        irrelevant = denumeralize(value)
        self.assertEqual(desired, value)
        
    def test_only_accepts_str(self):
        value = 5
        message = "denumeralize expects a string, not <class 'int'> 5"
        with self.assertRaises(Exception) as e:
            irrelevant = denumeralize(value)
        self.assertEqual(message, str(e.exception))
            
    def test_input_empty_exception(self):
        value = ''
        message = "denumeralize expects a string with length > 0"
        with self.assertRaises(Exception) as e:
            discard = denumeralize(value)
        self.assertEqual(message, str(e.exception))
        

class TestCreateNumberList(unittest.TestCase):
    
    def test_r_exception(self):
        value = "r"
        with self.assertRaises(Exception):
            create_number_list(value)
            
    def test_iii(self):
        value = "III"
        desired = [1, 1, 1]
        result = create_number_list(value)
        self.assertEqual(desired, result)
        
class TestAddUpIdenticalNeighbours(unittest.TestCase):
    
    def test_length_one(self):
        value = [2]
        desired = [2]
        result = add_up_identical_neighbours(value)
        self.assertEqual(desired, result)
        
    def test_two_different(self):
        value = [4, 3]
        desired = [4, 3]
        result = add_up_identical_neighbours(value)
        self.assertEqual(desired, result)
    
    def test_two_same(self):
        value = [3, 3]
        desired = [6]
        result = add_up_identical_neighbours(value)
        self.assertEqual(desired, result)
        
    def test_four_same_two_different_same(self):
        value = [2, 2, 2, 2, 5, 5]
        desired = [8, 10]
        result = add_up_identical_neighbours(value)
        self.assertEqual(desired, result)
        
    def test_input_unchanged(self):
        value = [2, 2, 2, 2, 5, 5]
        desired = [2, 2, 2, 2, 5, 5]
        irrelevant = add_up_identical_neighbours(value)
        self.assertEqual(desired, value)
        
class TestSubtractWhenSmallerThanNext(unittest.TestCase):
    
    def test_two_same(self):
        value = [3, 3]
        desired = [3, 3]
        result = subtract_when_smaller_than_next(value)
        self.assertEqual(desired, result)
        
    def test_large_small(self):
        value = [5, 2]
        desired = [5, 2]
        result = subtract_when_smaller_than_next(value)
        self.assertEqual(desired, result)
    
    def test_small_large(self):
        value = [2, 6]
        desired = [4]
        result = subtract_when_smaller_than_next(value)
        self.assertEqual(desired, result)
   
    def test_input_unchanged(self):
        value = [9, 3, 6, 1, 5]
        desired = [9, 3, 6, 1, 5]
        irrelevant = subtract_when_smaller_than_next(value)
        self.assertEqual(desired, value)
        
class TestSum(unittest.TestCase):
    
    def test_input_unchanged(self):
        value = [9, 3, 6, 1, 5]
        desired = [9, 3, 6, 1, 5]
        irrelevant = sum(value)
        self.assertEqual(desired, value)

            
"""
"VII" -> 7
"VIII" -> 8
"IX" -> 9

"X" -> 10
"XX" -> 20
"XXX" -> 30
"XL" -> 40
"L" -> 50
"LX" -> 60
"LXX" -> 70
"LXXX" -> 80
"XC" -> 90

"C" -> 100
"CC" -> 200
"CCC" -> 300
"D" -> 500
"DCC" -> 700
"DCCC" -> 800
"CM" -> 900

"M" -> 1000
"MM" -> 2000
"MMM" -> 3000
"MMMM" -> 4000
"""

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
