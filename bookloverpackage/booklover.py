import pandas as pd

class BookLover:

    def __init__(self, name, email, fav_genre, 
                 num_books=0, book_list =pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        '''
        adds the book to booklist, if doesn't already exist
        '''

        if book_name  in self.book_list['book_name'].values:
            print(f"{book_name} is already in the book list.")
        
        else:

            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
                
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        '''
        deterimes if the person has read a book
        '''
        if book_name in self.book_list['book_name'].values:
            return True
        return False
    
    def num_books_read(self):
        '''
        returns number of books booklover has read
        '''
        return self.num_books
    
    def fav_books(self):
        '''
        returns list of books with book_rating > 3
        '''
        return self.book_list[self.book_list['book_rating'] > 3]
    

if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("Throne of Glass", 5)
    test_object.add_book("City of Bones", 5)  # Should notify that the book is already in the list
    test_object.add_book("City of Bones", 5)     
    test_object.add_book("Love and Other Words", 1)     
    print(test_object.has_read("City of Bones"))  # Should return True
    print(test_object.has_read("City of Hehhehhe"))  # Should return False
    print(test_object.num_books_read())  # Should return 3
    print(test_object.fav_books())