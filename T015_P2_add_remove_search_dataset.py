#Fiona Cheng (101234672) (Compiler)
#Adam Saunders (101217748) (Reviewer)
#Owen Petersen (101233850) (Reviewer)
#Isaac Walberg (101234320) (Reviewer)

from T015_P5_load_data import book_category_dictionary
from T015_check_equal import check_equal

def add_book(library: dict, new_book: tuple) -> dict:
    """
    Returns the contents of library with new_book added under the correct category.
    Displays whether or not the addition was a success on the console.
    Precondition: library is sorted by category
    Developed by Fiona Cheng (101234672)
    
    >>>add_book(main_dict, ('Nexus', 'Westerfield', 'English', 'Simon & Schuster', 'Fiction', 5.0, 9999))
    The book has been added correctly
    #Returns main_dict with {'title': 'Nexus', 'author': 'Westerfield', 'rating': 5.0, 'publisher': 'Simon & Schuster', 'pages': 9999, 'language': 'English'} 
    added to the list of Fiction books
    
    >>>add_book(main_dict, ('Not a real book', 'Fiona', 'English', 'Cheng', 'Imaginary', 'N/A', 1))
    The book has been added correctly
    #Returns main_dict with with an additional key called 'Imaginary' linked to the following list:
    [{'title:': 'Not a real book', 'author': 'Fiona', 'rating': 'N/A', 'publisher': 'Cheng', 'pages': 1, 'language': 'English'}]
    
    >>>add_book(main_dict, ('Not a real book', 'Fiona', 41, 'Cheng', 'Imaginary', 'N/A', 1))
    There was an error adding the book
    #Returns main_dict unchanged
    
    >>>add_book(main_dict, ('Not a real book', 'Fiona', 'English', 'Cheng', 'Imaginary', 'N/A'))
    There was an error adding the book
    #Returns main_dict unchanged
    """
    #ensures the book being added has the correct amount of information
    if len(new_book) != 7: 
        print("There was an error adding the book")
        return library
    
    title, author, language, publisher, category, rating, pages = new_book #separating the new_book into associated variables
    
    #ensures the information in new_book are acceptable types
    if (type(category) != type('str') or type(title) != type('str') or type(author) != type('str') or type(language) != type('str') or type(publisher) != type('str') or type(pages) != type(1)):
        print("There was an error adding the book")
        return library
    
    #ensures the rating is either a string, a float, or an integer
    if (type(rating) != type('str') and type(rating) != type(1) and type(rating) != type(1.0)):
        print("There was an error adding the book")
        return library
    
    current_book = {'title': title, 'author': author, 'rating': rating, 'publisher': publisher, 'pages': pages, 'language': language} #creates a dictionary with all details except the category
    
    if category in library: #if the category of book exists, add current_book to the category (allows for duplicates)
        library[category] += [current_book]
    else: #if the category of book does not exist, create a new category and add current_book to the new category
        library.update({category: [current_book]})
    
    print("The book has been added correctly")
    return library #returns the updated library

def remove_book(dictionary: dict, book: str, category: str) -> dict:
    """
    Removes the given book from the given dictionary. Give the book's category for ease of removal. If the book is successfully removed,
    prints "The book has been removed correctly". If the book is not found, prints "There was an error removing the book. Book not found".
    Developed by Adam Saunders (101217748)
    
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'), "Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction")
    The book has been removed correctly
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'), 'Not a Real Book', 'Fiction')
    There was an error removing the book. Book not found
    >>>remove_book(book_category_dictionary('google_books_dataset.csv'), 'Antiques Roadkill: A Trash 'n' Treasures Mystery', 'Not a Real Category')
    There was an error removing the book. Book not found
    """
    
    status = 0                  # Used to check if a book was removed
    if category in dictionary:      # If the category is not real, it will bypass everything else, which is optimal
        for cat in dictionary:          # Checks through each category in the entire dictionary
            if cat == category:             # Until it finds the correct category
                for inner_list in dictionary[cat]:          # Goes through the list of individual book dictionaries in the category
                    if inner_list['title'] == book:           # Finds the correct book
                        dictionary[cat].pop(dictionary[cat].index(inner_list))       # Clears the correct book and all of its info
                        status = 1                                  # Now status != 0
                        print("The book has been removed correctly")
    
    if status == 0:     # Staus will only be 0 if no book was removed
        print("There was an error removing the book. Book not found")
                
    return dictionary

def get_books_by_category(dic: dict, cat: str)-> int:
    """
    Developed by Isaac Walberg (101234320)
    Returns the total amount of books in a given catagory, along with printing the title of each book along with the author under the set category
    >>>get_books_by_category(book_category_dictionary('google_books_dataset.csv'),'Legal')
    The category Legal has 1 books. This is the list of books
    Book 1: The Guardians: The explosive new thriller from international bestseller John Grisham by John Grisham
    1
    >>>get_books_by_category(book_category_dictionary('google_books_dataset.csv'),'Social Science')
    The category Social Science has 3 books. This is the list of books
    Book 1: We Should All Be Feminists by Chimamanda Ngozi Adichie
    Book 2: Happy: Why More or Less Everything is Absolutely Fine by Derren Brown
    Book 3: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    3
    """
    if cat not in dic.keys():
        return 0
    lis = dic[cat]
    total = 0
    num = 1
    for book in lis:
        total +=1
    print('The category', cat ,'has', total ,'books. This is the list of books:')
    for i in lis:
        print('Book', str(num)+':',i['title'], 'by', i['author'])
        num +=1
    return total

def get_books_by_rate(master_list:dict, rating:int) -> int:
    """Returns the number of books in a given dictionary of books which fall within the specified rating.
    Developed By: Owen Petersen (101233850)
    
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"), 3)
    There are 8 books whose rate is between 3 and 4. This is the list of books:
    Book 1: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 2: Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    Book 3: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 4: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 5: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 6: The Infinite Game by Simon Sinek
    Book 7: Bring Me Back by B A Paris
    Book 8: Mrs. Pollifax Unveiled by Dorothy Gilman
    
    8
    """
    book_list = set() #creates an empty set to keep track of all book which fall whithin the rating range
    book_list_print = '' #the string used to make the print funciton easier later on
    book_count = 0 #the counter for the number of books in the rating range
    for category in master_list: #iterates through each category in the main dictionary
        for book in master_list[category]: #iteratees through each entry (or book) in the list for each category
            if book['rating'] != 'N/A' and rating <= book['rating'] < (rating + 1): #checks if there is no rating and then checks if the rating is within the specific range
                book_list.add((book['title'], book['author'])) #adds the book's title and author to the set as a tuple
    for entry in book_list: #iterates over all the (title, author) entries in the set containing the information
        book_count += 1 #counts the number of books which fall in the ratings range
        book_list_print += 'Book ' + str(book_count) + ': ' + str(entry[0]) + ' by ' + str(entry[1]) + '\n'#neatly formats the title and author information to be printed later
    print('There are ', len(book_list), ' books whose rate is between ', rating, ' and ', rating +1, '. This is the list of books:\n', book_list_print, sep='')#neatly prints all relevant information
    return len(book_list)
        
def get_book_by_title(library: dict, title: str)-> bool:
    """
    Returns True if the title exists in the dictionary.
    Prints whether or not the book has been found to the console.
    Precondition: library is sorted by category
    Developed by Fiona Cheng (101234672)
    
    >>>get_book_by_title(main_dict, 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader')
    The book has been found
    True
    
    >>>get_book_by_title(main_dict, 'Permanent Record')
    The book has been found
    True
    
    >>>get_book_by_title(main_dict, 'Hello World')
    The book has NOT been found
    False
    """
    
    for category in library: #checks all the categories
        for book in library[category]: #checks each book in the category
            if book.get('title', 0) == title: #checks to see if the title matches the book we're searching for
                print("The book has been found")
                return True
        
    print("The book has NOT been found")
    return False

def get_books_by_author(dictionary: dict, author: str) -> int:
    """
    Returns the number of books written by the given author in the given
    dictionary. Also prints the following:
    The author [author] has published the following books:
    Book 1: [Title], rate: [Rating]
    Book 2: [Title], rate: [Rating]
    Developed by Adam Saunders (101217748)
    
    >>>get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Barbara Allan')
    4
    The author Barbara Allan has published the following books:
    Book 1: "Antiques Roadkill: A Trash 'n' Treasures Mystery", rate: 3.3
    Book 2: Antiques Con rate: 4.8
    Book 3: Antiques Chop rate: 4.5
    Book 4: Antiques Knock-Off rate: 4.3
    
    >>>get_books_by_author(book_category_dictionary('google_books_dataset.csv'), 'Not a Real Author')
    0
    The author Not a Real Author has published the following books:
    
    """
    
    book_count = 0
    title_dict = {}
    print("The author", author, "has published the following books:")
    for category in dictionary:          # Checks through each category in the entire dictionary
        for inner_list in dictionary[category]:          # Goes through the list of individual book dictionaries in the category
            if inner_list['author'] == author:           # Finds the correct author   
                title_dict.update({inner_list['title']:inner_list['rating']})       # Updates a dictionary with the info. This is to prevent duplicates.
                
    for item in title_dict:         # Goes through each book in the new dictionary
        title,rating = item,title_dict[item]            # Retrieves the title and rating of each book
        book_count += 1             # Increments the counter
        print('Book', str(book_count)+':', title+',', 'rate:', rating)          # Prints "Book #: [Title], rate: [Rating]"
                
    
    return book_count

def get_books_by_publisher(dic: dict, pub: str)-> int:
    """
    Developed by Isaac Walberg (101234320)
    returns the total amount of books from a set publisher exluding duplicates, along with printing the title of each book along with the author under the set publisher
    >>>The publisher DC has published the following books:
    Book 1: Young Justice Vol. 1 by Art Baltazar
    Book 2: The Joker by Brian Azzarello
    2
    >>>The publisher Vintage has published the following books:
    Book 1: We Should All Be Feminists by Chimamanda Ngozi Adichie
    1
    """
    num = 0
    list_of_books = []
    print('The publisher', pub ,'has published the following books:')
    for category in dic:
        for book in dic[category]:
            if book['publisher'] == pub:
                list_of_books.append(book['title']+' '+'by'+' '+book['author'])
    list_of_books = list(dict.fromkeys(list_of_books))
    for i in list_of_books:
        print('Book',str(num+1)+':', i)
        num+=1
    return num

def get_all_categories_for_book_title(master_list:dict, book_title:str) -> str:
    """Takes a dictionary containing a series of books sorted by category and returns the categories for which a specific entry (book_title) belongs to.
    Developed By: Owen Petersen (101233850)
    
    >>>get_all_categories_for_book_title(book_category_dictionary("google_books_dataset.csv"), "Antiques Roadkill: A Trash 'n' Treasures Mystery")
    The book title Antiques Roadkill: A Trash 'n' Treasures Mystery belongs to the following categories:
    Category 1: Fiction
    Category 2: Detective
    Category 3: Mystery

    3
    """
    if type(book_title) == str:
        category_list = [] #the list used to keep track of all the categories for the specific list
        category_list_print = '' #the string used to make the print function easier later on
        for category in master_list: #iterates through each category in the main dictionary
            for book in master_list[category]: #iterates through each entry (or book) in the list for each category
                if book_title in book.values(): #checks if the book title matches the book the for-loop is currently looking at
                    category_list += [category] #adds the category to the category_list to keep track of them all
        for category_index in range(len(category_list)): #iterates over the range (or indices) of the list containing the categories for the specific book
            category_list_print += 'Category ' + str(category_index + 1) + ": " + str(category_list[category_index] + '\n') #formats the collected information neatly for it to be easily printed later
        print('The book title ', book_title, ' belongs to the following categories:\n', category_list_print, sep='') #prints the appropriate message and the information regarding the categories of the book        
        return len(category_list)
    else:
        print('book title must be type = str')

def test_addition(library: dict, info: tuple)-> bool:
    """
    Returns True if the exact book defined by info exists.
    Prints whether or not the book has been found to the console.
    Precondition: library is sorted by category and info contains a tuple containing the following:
    (title, author, language, publisher, category, rating, pages)
    Developed by Fiona Cheng (101234672)
    
    >>>test_addition({}, (1, 2, 3, 4, 5, 6, 7)
    The book has not been found.
    False
    
    >>>test_addition({'Food': [{'title': "Book", 'author': 'Jane Smith', 'rating': 3.4, 'publisher': 'Company Co.', 'pages': 321, 'language': 'English'}]}, ('Book', 'Jane Smith', 'English', 'Company Co.', 'Food', 3.4, 321))
    The book has been found.
    True
    """
    title, author, language, publisher, category, rating, pages = info #separating the new_book into associated variables
    
    for book in library[category]:
        if book['title'] == title:
            if book['author'] == author and book['rating'] == rating and book['publisher'] == publisher and book['pages'] == pages and book['language'] == language:
                print("The book has been found")
                return True
    print("The book has not been found.")
    return False

def test_removal(library: dict, title: str, category: str)-> bool:
    """
    Returns True if the title exists in the category.
    Prints whether or not the book has been found to the console.
    Precondition: library is sorted by category
    Developed by Fiona Cheng (101234672)
    
    >>>get_book_by_title(main_dict, 'Permanent Record', 'Biography')
    The book has been found
    True
    
    >>>get_book_by_title(main_dict, 'Hello World', 'Fiction')
    The book has NOT been found
    False
    """
    
    for book in library[category]: #checks each book in the category
        if book.get('title', 0) == title: #checks to see if the title matches the book we're searching for
            print("The book has been found")
            return True
        
    print("The book has NOT been found")
    return False

#Main Script
if __name__ == '__main__':
    library = book_category_dictionary('google_books_dataset.csv')
    total_passes_overall = 0
    
    #Testing add_book developed by Isaac Walberg (101234320)
    total_passed = 0
    total_passed += check_equal("add_book(library, ('I', 'love', 'English', 'ECOR','Thrillers','N/A',1042))", True, test_addition(add_book(library, ('I', 'love', 'English', 'ECOR','Thrillers','N/A',1042)), ('I', 'love', 'English', 'ECOR','Thrillers','N/A',1042)))
    total_passed += check_equal("add_book(library, ('Goldfish', 'Jacob A', 'English', 'Minotaur Books','Business',4.1,420))", True, test_addition(add_book(library, ('Goldfish', 'Jacob A', 'English', 'Minotaur Books','Business',4.1,420)), ('Goldfish', 'Jacob A', 'English', 'Minotaur Books','Business',4.1,420)))
    total_passed += check_equal("add_book(library, (\"Obama's Autobiography\", 'Barack Obama', 'English', 'Kensington Publishing Corp.','Biography',5,1000))", True, test_addition(add_book(library, ("Obama's Autobiography", 'Barack Obama', 'English', 'Kensington Publishing Corp.','Biography',5,1000)), ("Obama's Autobiography", 'Barack Obama', 'English', 'Kensington Publishing Corp.','Biography',5,1000)))
    print('Results from test_add_book:')
    print('Total tests: ', 3)
    print('Total tests passed: ', total_passed)
    print('Total tests failed: ', 3-total_passed, '\n')   
    total_passes_overall += total_passed
    
    #Testing remove_book developed by Owen Petersen (101233850)
    tests_passed = 0
    tests_passed += check_equal("remove_book(book_category_dictionary('google_books_dataset.csv'), 'Total Control', 'Mystery')", False, test_removal(remove_book(library, 'Total Control', 'Mystery'), 'Total Control', 'Mystery'))
    tests_passed += check_equal("remove_book(book_category_dictionary('google_books_dataset.csv'), 'Boy Erased: A Memoir', 'Biography')", False, test_removal(remove_book(library, 'Boy Erased: A Memoir', 'Biography'), 'Boy Erased: A Memoir', 'Biography'))
    print('------\nTests for remove_book:\nTotal Tests = {0}\nTests Failed = {1}\n'.format(2,2-tests_passed)) 
    total_passes_overall += tests_passed
    
    library = book_category_dictionary('google_books_dataset.csv')
    
    #Testing get_books_by_category developed by Fiona Cheng (101234672)
    tests_passed = 0
    tests_passed += check_equal("get_books_by_category(library, 'Adventure')", 7, get_books_by_category(library, 'Adventure'))
    tests_passed += check_equal("get_books_by_category(library, 'Traditional')", 1, get_books_by_category(library, 'Traditional')) #a category with only one item
    tests_passed += check_equal("get_books_by_category(library, 'Invisible')", 0, get_books_by_category(library, 'Invisible')) #nonexistent category
    tests_passed += check_equal("get_books_by_category(library, 'Fiction')", 39, get_books_by_category(library, 'Fiction')) #a category with many items

    print("Tests passed for get_books_by_category:", tests_passed, "\tTests failed:", 4-tests_passed, '\n')
    total_passes_overall += tests_passed
    

    # Setting up a small dictionary to be tested
    # There are 3 ratings between 3 (inclusive) and 4 (exclusive) (4 without duplicates, but duplicates should not count)
    # There are 2 instances of GenericTitle, in Crime and Horror

    test = { 'Crime' : [ {'title':'CrimeTitle_1', 'author':'CrimeAuthor_1','rating':4.3,'publisher':'CrimePublisher1','pages':115,'language':'English'} , {'title':'CrimeTitle_2', 'author':'CrimeAuthor_2','rating':4.0,'publisher':'CrimePublisher2','pages':273,'language':'English'} , {'title':'GenericTitle', 'author':'GenericAuthor','rating':2.999,'publisher':'GenericPublisher','pages':935,'language':'English'} ] , 'Horror' : [ {'title':'HorrorTitle_1', 'author':'HorrorAuthor_1','rating':3.7,'publisher':'HorrorPublisher1','pages':666,'language':'English'} , {'title':'GenericTitle', 'author':'GenericAuthor','rating':3,'publisher':'GenericPublisher','pages':256,'language':'English'} , {'title':'Sci-FiTitle_1', 'author':'Sci-FiAuthor_1','rating':0.9,'publisher':'Sci-FiPublisher2','pages':234,'language':'English'} , {'title':'HorrorTitle_1', 'author':'HorrorAuthor_1','rating':3.8,'publisher':'HorrorPublisher1','pages':666,'language':'English'} , {'title':'CrimeTitle_2', 'author':'CrimeAuthor_2','rating':3.0,'publisher':'CrimePublisher2','pages':273,'language':'English'} ] , 'Sci-Fi' : [ {'title':'Sci-FiTitle_1', 'author':'Sci-FiAuthor_1','rating':0.9,'publisher':'Sci-FiPublisher2','pages':234,'language':'English'} ] }

    #Testing get_books_by_rate developed by Adam Saunders (101217748)
    pass_counter = 0
    pass_counter += check_equal('get_books_by_rate(test, 3)', 3, get_books_by_rate(test, 3))      # Should Pass

    print(pass_counter, 'tests passed out of 1 for get_books_by_rate \n')
    total_passes_overall += pass_counter
    
    #Testing get_book_by_title developed by Isaac Walberg (101234320)
    total_passed = 0
    total_passed += check_equal('get_book_by_title(library, "The Memoirs of Sherlock Holmes")', True, get_book_by_title(library, 'The Memoirs of Sherlock Holmes'))
    total_passed += check_equal("get_book_by_title(library, 'I love ECOR 1042')", False, get_book_by_title(library, 'I love ECOR 1042'))
    total_passed += check_equal("get_book_by_title(library, 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)')", True, get_book_by_title(library, 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)'))
    print('Results from test_get_book_by_title:')
    print('Total tests: ', 3)
    print('Total tests passed: ', total_passed)
    print('Total tests failed: ', 3-total_passed, '\n')   
    total_passes_overall += total_passed
    
    #Testing get_books_by_author developed by Owen Petersen (101233850)
    tests_passed = 0
    tests_passed += check_equal('get_books_by_author Test 1;', 4, get_books_by_author(library, 'Barbara Allan'))
    tests_passed += check_equal('get_books_by_author Test 2;', 0, get_books_by_author(library, 'Not a Real Author'))
    print('------\nTests for get_books_by_author:\nTotal Tests = {0}\nTests Failed = {1}\n'.format(2,2-tests_passed))
    total_passes_overall += tests_passed
    
    #Testing get_books_by_publisher developed by Fiona Cheng (101234672)
    tests_passed = 0
    tests_passed += check_equal("get_books_by_publisher(library, 'Tor Books')", 2, get_books_by_publisher(library, 'Tor Books')) #one duplicate
    tests_passed += check_equal("get_books_by_publisher(library, 'Penguin')", 5, get_books_by_publisher(library, 'Penguin')) #two duplicates
    tests_passed += check_equal("get_books_by_publisher(library, 'Pan Macmillan')", 2, get_books_by_publisher(library, 'Pan Macmillan')) #four of the same
    tests_passed += check_equal("get_books_by_publisher(library, 'Bob Smith')", 0, get_books_by_publisher(library, 'Bob Smith')) #nonexistent category

    print("Tests passed for get_books_by_publisher:", tests_passed, "\tTests failed:", 4-tests_passed, '\n')
    total_passes_overall += tests_passed
    
    #Testing get_all_categories_for_book_title developed by Adam Saunders (101217748)
    #Uses the dictionary test defined on line 357
    pass_counter = 0
    pass_counter += check_equal('get_all_categories_for_book_title(test, "GenericTitle")', 2, get_all_categories_for_book_title(test, "GenericTitle")) # Should Pass

    print(pass_counter, 'tests passed out of 1 for get_all_categories_for_book_title \n')
    total_passes_overall += pass_counter
    
    print("Total number of tests for T015_P2_add_remove_search_dataset:", 20, "\nNumber of expected passes:", 20, "\nTests passed:", total_passes_overall, "\nTests failed:", 20 - total_passes_overall)