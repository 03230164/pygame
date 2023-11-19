import unittest
from  match_three import swap, find_matches, Candy

class TestGameFunctions(unittest.TestCase):
   def setUp(self):
       self.candy1 = Candy(0, 0)
       self.candy2 = Candy(1, 1)

   def test_swap(self):
       self.assertEqual(self.candy1.row_num, 0)
       self.assertEqual(self.candy1.col_num, 0)
       self.assertEqual(self.candy2.row_num, 1)
       self.assertEqual(self.candy2.col_num, 1)
       
       swap(self.candy1, self.candy2)
       
       self.assertEqual(self.candy1.row_num, 1)
       self.assertEqual(self.candy1.col_num, 1)
       self.assertEqual(self.candy2.row_num, 0)
       self.assertEqual(self.candy2.col_num, 0)

   def test_find_matches(self):
       matches = find_matches(self.candy1, set())
       self.assertNotIn(self.candy2, matches)

       self.candy1.color = 'blue'
       self.candy2.color = 'blue'
       matches = find_matches(self.candy1, set())
       self.assertIn(self.candy2, matches)

if __name__ == '__main__':
   unittest.main()
