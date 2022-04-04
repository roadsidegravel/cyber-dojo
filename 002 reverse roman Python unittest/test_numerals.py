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
        
class TestSumTheNumbers(unittest.TestCase):
    
    def test_empty_zero(self):
        value = []
        desired = 0
        result = sum_the_numbers(value)
        self.assertEqual(desired, result)
        
    def test_length_one_returns_its_value(self):
        value = [8]
        desired = 8
        result = sum_the_numbers(value)
        self.assertEqual(desired, result)
        
    def test_same_adds(self):
        value = [4, 4]
        desired = 8
        result = sum_the_numbers(value)
        self.assertEqual(desired, result)
        
    def test_big_small_adds(self):
        value = [3, 2]
        desired = 5
        result = sum_the_numbers(value)
        self.assertEqual(desired, result)
        
    def test_small_big_subtracts(self):
        value = [2, 10]
        desired = 8
        result = sum_the_numbers(value)
        self.assertEqual(desired, result)
            
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
