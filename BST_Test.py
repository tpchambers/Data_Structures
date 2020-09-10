import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):
    def setUp(self):
        self.__BST = Binary_Search_Tree()

    def test_empty (self):
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual('[ ]', self.__BST.post_order())
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual(0, self.__BST.get_height())

    def test_value_error (self):
        with (self.assertRaises(ValueError)):
            self.__BST.insert_element(5)
            self.__BST.remove_element(20)
        self.assertEqual('[ 5 ]', str(self.__BST))
        self.assertEqual('[ 5 ]', self.__BST.pre_order())
        self.assertEqual('[ 5 ]', self.__BST.post_order())
        self.assertEqual(1, self.__BST.get_height())
        self.assertEqual([5], self.__BST.to_list())

    def test_remove_root(self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(20)
        self.__BST.insert_element(22)
        self.__BST.remove_element(15)
        self.assertEqual('[ 20, 22 ]', str(self.__BST))
        self.assertEqual('[ 22, 20 ]', self.__BST.post_order())
        self.assertEqual('[ 20, 22 ]', self.__BST.pre_order())
        self.assertEqual([20,22], self.__BST.to_list())
        self.assertEqual(2, self.__BST.get_height())

    def test_emoval_empty (self):
        self.__BST.insert_element(7)
        self.__BST.remove_element(7)
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual('[ ]', self.__BST.post_order())
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual(0, self.__BST.get_height())


    def test_insert_string (self):
        self.__BST.insert_element('spaces')
        self.assertEqual('[ spaces ]', str(self.__BST))

    def test_insert_two_strings(self):
        self.__BST.insert_element('tree')
        self.__BST.insert_element('dog')
        self.assertEqual('[ dog, tree ]', str(self.__BST))


    def test_one_height(self):
        self.__BST.insert_element(0)
        self.assertEqual('[ 0 ]', str(self.__BST))
        self.assertEqual([0], self.__BST.to_list())
        self.assertEqual(1, self.__BST.get_height())

    def test_remove_empty(self):
        with (self.assertRaises(ValueError)):
            self.__BST.remove_element(13)
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual('[ ]', self.__BST.post_order())
        self.assertEqual(0, self.__BST.get_height())
        self.assertEqual([], self.__BST.to_list())

    def test_insert_one(self):
        self.__BST.insert_element(10)
        self.assertEqual('[ 10 ]', str(self.__BST))
        self.assertEqual('[ 10 ]', self.__BST.post_order())
        self.assertEqual('[ 10 ]', self.__BST.pre_order())
        self.assertEqual([10], self.__BST.to_list())
        self.assertEqual(1 , self.__BST.get_height())


    def test_balance_three (self):
        self.__BST.insert_element(15)
        self.__BST.insert_element(9)
        self.__BST.insert_element(22)
        self.assertEqual('[ 9, 15, 22 ]', str(self.__BST))
        self.assertEqual('[ 9, 22, 15 ]', self.__BST.post_order())
        self.assertEqual('[ 15, 9, 22 ]', self.__BST.pre_order())
        self.assertEqual([9, 15, 22], self.__BST.to_list())
        self.assertEqual(2, self.__BST.get_height())


    def test_remove_double_left(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(10)
        self.__BST.insert_element(4)
        self.__BST.insert_element(25)
        self.__BST.insert_element(6)
        self.__BST.remove_element(10)
        self.assertEqual('[ 2, 4, 6, 25 ]', str(self.__BST))
        self.assertEqual('[ 2, 6, 25, 4 ]', self.__BST.post_order())
        self.assertEqual('[ 4, 2, 25, 6 ]', self.__BST.pre_order())
        self.assertEqual([2, 4, 6, 25], self.__BST.to_list())
        self.assertEqual(3, self.__BST.get_height())

    

    def test_left_three_rotate(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(13)
        self.__BST.insert_element(7)
        self.assertEqual('[ 7, 13, 20 ]', str(self.__BST))
        self.assertEqual('[ 7, 20, 13 ]', self.__BST.post_order())
        self.assertEqual('[ 13, 7, 20 ]', self.__BST.pre_order())
        self.assertEqual(2, self.__BST.get_height())

    def test_right_three_rotate(self):
        self.__BST.insert_element(2)
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.assertEqual('[ 2, 50, 60 ]', str(self.__BST))
        self.assertEqual('[ 2, 60, 50 ]', self.__BST.post_order())
        self.assertEqual('[ 50, 2, 60 ]', self.__BST.pre_order())
        self.assertEqual([2, 50, 60], self.__BST.to_list())
        self.assertEqual(2, self.__BST.get_height())


    def test_right_four_rotate(self):
        self.__BST.insert_element(10)
        self.__BST.insert_element(4)
        self.__BST.insert_element(7)
        self.__BST.insert_element(1)
        self.assertEqual('[ 1, 4, 7, 10 ]', str(self.__BST))
        self.assertEqual('[ 1, 4, 10, 7 ]', self.__BST.post_order())
        self.assertEqual('[ 7, 4, 1, 10 ]', self.__BST.pre_order())
        self.assertEqual([1, 4, 7, 10], self.__BST.to_list())
        self.assertEqual(2, self.__BST.get_height())


    def test_height (self):
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual(0, self.__BST.get_height())
      
    def test_remove_one(self):
        self.__BST.insert_element(5)
        self.__BST.remove_element(5)
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual('[ ]', self.__BST.post_order())
        self.assertEqual('[ ]', self.__BST.pre_order())
        self.assertEqual([], self.__BST.to_list())
        self.assertEqual(0, self.__BST.get_height())

    
if __name__ == '__main__':
    unittest.main()