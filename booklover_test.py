import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        lover1 = BookLover("Bobby Jones", "bobbyjones@gmail.com", "fantasy")
        lover1.add_book("Jane Eyre", 4)
        self.assertTrue("Jane Eyre" in lover1.book_list['book_name'].values)


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        lover2 = BookLover("Bobbette Jones", "bobbettejones@gmail.com", "history")
        lover2.add_book("Fight Club", 3)
        lover2.add_book("Fight Club", 3)

        self.assertEqual("Fight Club" in lover2.book_list['book_name'].value_counts(), 1)   


    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        lover3 = BookLover("Bobber Jones", "bobberjones@gmail.com", "fiction")
        lover3.add_book("The Divine Comedy", 5)
        self.assertTrue(lover3.has_read("The Divine Comedy"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        lover4 = BookLover("Bob Jones", "bobjones@example.com", "fiction")
        self.assertFalse(lover4.has_read("The Popol Vuh"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        lover5 = BookLover("Bobberette Jones", "boberettejones@example.com", "mystery")
        lover5.add_book("Jane Eyre", 4)
        lover5.add_book("Fight Club", 3)
        lover5.add_book("The Divine Comedy", 5)
        lover5.add_book("The Popol Vuh", 5)
        self.assertEqual(lover5.num_books_read(), 4)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        lover6 = BookLover("Bobberette Jones", "boberettejones@example.com", "mystery")
        lover6.add_book("Jane Eyre", 4)
        lover6.add_book("Fight Club", 3)
        lover6.add_book("The Divine Comedy", 5)

        fav_books = lover6.fav_books()

        self.assertTrue(all(fav_books['book_rating'] > 3))
        self.assertEqual(len(fav_books), 2)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)