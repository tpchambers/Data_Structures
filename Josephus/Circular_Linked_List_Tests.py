import unittest
from Circular_Linked_List import CircularLinkedList

class Cltester(unittest.TestCase):
    def setUp(self):
        self.__CLL = CircularLinkedList()
    
    def test_insert(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_end(7)
        self.__CLL.insert_beginning(3)
        self.__CLL.insert_beginning(27)
        self.assertEqual([27,3,5,6,7],self.__CLL.traverse())


    def test_mid(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.assertEqual([5,27,6],self.__CLL.traverse())

    def test_size(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.assertEqual(5,self.__CLL.getsize())

    def test_length(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.assertEqual(5,len(self.__CLL))

    def test_remove_beginning(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.remove_beginning()
        self.assertEqual([15, 5, 27, 15, 6, 16],self.__CLL.traverse())

    def test_remove_end(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.remove_beginning()
        self.__CLL.remove_end()
        self.__CLL.remove_end()
        self.__CLL.remove_beginning()
        self.assertEqual([5,27,15],self.__CLL.traverse())
        self.assertEqual(3,self.__CLL.getsize())


    def test_reverse(self):
        self.__CLL.insert_end(5)
        self.__CLL.insert_end(6)
        self.__CLL.insert_mid(27)
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.remove_beginning()
        self.__CLL.remove_end()
        self.__CLL.remove_end()
        self.__CLL.remove_beginning()
        self.__CLL.insert_end(16)
        self.__CLL.insert_mid(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.insert_beginning(15)
        self.__CLL.reverse()
        self.assertEqual([16, 15, 15, 27, 5, 15, 15],self.__CLL.traverse())
if __name__ == '__main__':
    unittest.main()

