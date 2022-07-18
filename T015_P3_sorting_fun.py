#Adam Saunders (101217748) (Reviewer)
#Owen Petersen (101233850) (Compiler)
#Isaac Walberg (101234320) (Reviewer)
#Fiona Cheng (101234672) (Reviewer)
from T015_P5_load_data import * 
import T015_check_equal


def dictionary_list(dictionary: dict) -> list:
    """
    Returns a list of all books in dictionary with each element of the list being a dictionary containing information for one book.
    Precondition: dictionary must be books sorted by category
    Developed by Owen Petersen (101233850)
    
    >>>dictionary_list(book_category_dictionary('google_books_dataset.csv'))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Thrillers'], 'pages': 544}, ...]
    """
    book_list = []
    for category in dictionary:
        for book in dictionary[category]:
            duplicate = (False, None)
            for i in range(len(book_list)):
                if book['title'] == book_list[i]['title']:
                    duplicate = (True, i)
            if not duplicate[0]:
                book_list += [{'title':book['title'],'author':book['author'],'language':book['language'],'rating':book['rating'],'publisher':book['publisher'],'category': [category],'pages':book['pages']}]
            elif duplicate[0]:
                book_list[duplicate[1]]['category'] += [category]
    return book_list

def sort_books_title(library: dict)-> list:
    """
    Returns an alphabeticaly sorted list the books from library based on title.
    Precondition: library is sorted by category.
    Developed by Isaac Walberg (101234320)
    
    >>>sort_books_title(book_category_dictionary('google_books_dataset.csv'))
    [{'title': "'Salem's Lot", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction', 'Detective', 'Mystery'], 'pages': 288}, {'title': "'Salem's Lot", 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Thrillers'], 'pages': 544},{ect...}]
    """
    master_list = dictionary_list(library)
    n = len(master_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if master_list[j]['title'] > master_list[j+1]['title']:
                master_list[j],master_list[j+1] = master_list[j+1],master_list[j]
    return master_list
    
def sort_books_author(library: dict) -> list:
    """
    Returns the books in library sorted alphabetically by author using the title in the case of ties.
    Precondition: library is sorted by category.
    Developed by Fiona Cheng (101234672)
    
    >>>sort_books_author({'Fiction': [{'author': 'Bob', 'title': "Bob's Adventures", 'publisher': "Smith Co.", 'pages': 100, 'rating': 2.3, 'language': 'English'}], 'Fantasy': [{'author': 'Abby', 'title': "Aimless Adventures", 'publisher': "Smith Co.", 'pages': 150, 'rating': 3.0, 'language': 'English'}]})
    [{'author': 'Abby', 'title': 'Aimless Adventures', 'publisher': 'Smith Co.', 'pages': 150, 'rating': 3.0, 'language': 'English', 'category': ['Fantasy']}, {'author': 'Bob', 'title': "Bob's Adventures", 'publisher': 'Smith Co.', 'pages': 100, 'rating': 2.3, 'language': 'English', 'category': ['Fiction']}]
    
    >>>sort_books_author({'Fiction': [{'author': 'Bob', 'title': "Bob's Adventures", 'publisher': "Smith Co.", 'pages': 100, 'rating': 2.3, 'language': 'English'}], 'Fantasy': [{'author': 'Bob', 'title': "Aardvark Adventures", 'publisher': "Smith Co.", 'pages': 150, 'rating': 3.0, 'language': 'English'}]})
    [{'author': 'Bob', 'title': 'Aardvark Adventures', 'publisher': 'Smith Co.', 'pages': 150, 'rating': 3.0, 'language': 'English', 'category': ['Fantasy']}, {'author': 'Bob', 'title': "Bob's Adventures", 'publisher': 'Smith Co.', 'pages': 100, 'rating': 2.3, 'language': 'English', 'category': ['Fiction']}]
    """
    book_list = dictionary_list(library)
    #Sorting book_list by author using the book title as a tiebreaker
    for i in range(len(book_list)):
        for j in range(len(book_list) - i - 1):
            if book_list[j]['author'] > book_list[j+1]['author']: 
                book_list[j], book_list[j+1]= book_list[j+1], book_list[j] #swaps order of books
            elif book_list[j]['author'] == book_list[j+1]['author'] and book_list[j]['title'] > book_list[j+1]['title']: #in case of a tie, check titles
                book_list[j], book_list[j+1]= book_list[j+1], book_list[j] #swaps order of books
    
    return book_list

def sort_books_publisher(dictionary: dict) -> list:
    """
    Returns a list of sorted books in the given dictionary alphabetically by publisher.
    In case of same publisher, sorts by title as a tiebreaker.
    Precondition: Dictionary must be sorted by Category.
    Developed by Adam Saunders (101217748)
    
    >>>sort_books_publisher({'Category':[{'title':'D','publisher':'D'},{'title':'A','publisher':'A'},{'title':'B','publisher':'A'}]})
    [{'title':'A','publisher':'A'},{'title':'B','publisher':'A'},{'title':'D','publisher':'D'}]
    """
    # Creating a list of every book
    book_list = dictionary_list(dictionary)
    # Sorting
    n = len(book_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if book_list[j]['publisher'] > book_list[j+1]['publisher']:         # Compares two adjacent entries by publisher
                book_list[j],book_list[j+1] = book_list[j+1],book_list[j]       # Swaps the entries
            elif book_list[j]['publisher'] == book_list[j+1]['publisher']:      # In case of same publisher
                if book_list[j]['title'] > book_list[j+1]['title']:                         # Compares by title
                    book_list[j],book_list[j+1] = book_list[j+1],book_list[j]     # Swaps the entries
    return book_list

def sort_books_ascending_rate(dictionary: dict) -> list:
    """
    Returns a list of the books in dictionary according to their rating in ascending order.
    Precondition: dictionary must contain books sorted by categories as keys with book information contained within a list which is the value of each key.
    Developed by Owen Petersen (101233850)
    
    >>>sort_books_ascending_rate(book_category_dictionary('google_books_dataset.csv'))
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics', 'Business']}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics', 'Management']}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': ['Economics']}, ...]
    """
    book_list = dictionary_list(dictionary)
    n = len(book_list)
    for i in range(n):
        for j in range(n-i-1):
            if book_list[j]['rating'] == 'N/A' and book_list[j+1]['rating'] != 'N/A':
                continue
            if ((((book_list[j]['rating'] == 'N/A' and book_list[j+1]['rating'] == 'N/A') and book_list[j]['title'] > book_list[j+1]['title']) or (book_list[j]['rating'] != 'N/A' and book_list[j+1]['rating'] == 'N/A')) or book_list[j]['rating'] > book_list[j+1]['rating']) or (book_list[j]['rating'] == book_list[j+1]['rating'] and book_list[j]['title'] > book_list[j+1]['title']):
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    return book_list

#Main Script
if __name__=='__main__':
    def sorted_book_list_title(filename: str) -> list:
        """Takes a file containing book data sorted by title and returns the books as a list of dictionaries.
        Developed By: Owen Petersen (101233850)
        
        >>>sorted_book_list_title('sorted_book_list.csv')
        [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'category': ['Fiction', 'Thrillers'], 'pages': 300}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'pages': 864}, ...]
        """
        file = open(filename, 'r')
        dictionary_list = []
        subsection = ['title', 'author', 'rating', 'publisher', 'pages', 'language', 'category']
    
        for line in file:
            line = line.rstrip('\n')
            if '"' in line:
                line_list_category = line[line.index('"'):]
                line_list = line[:line.index('"')]
            else:
                line_list_category = line[line.index('['):]
                line_list = line[:line.index('[')]
            line_list = line_list.strip(',').split(',')
            line_list_category = line_list_category.strip('"').strip('[').strip(']').split(',')
            for i in range(len(line_list_category)):
                line_list_category[i] = line_list_category[i].strip().strip("'")
                line_list += [line_list_category]
            if line_list[subsection.index('rating')] != 'N/A':
                line_list[subsection.index('rating')] = float(line_list[subsection.index('rating')])
            line_list[subsection.index('pages')] = int(line_list[subsection.index('pages')])

            book = {'title':line_list[0], 'author':line_list[1], 'language':line_list[5], 'rating':line_list[2], 'publisher':line_list[3], 'category':line_list[6], 'pages':line_list[4]}
            dictionary_list += [book]
        file.close()
        return dictionary_list

    dictionary = book_category_dictionary('google_books_dataset.csv')
    sorted_dictionary_list = sorted_book_list_title('sorted_book_list.csv')
    author_test = { 'Category 1': [ {'title':'B', 'author':'D','rating':5,'publisher':'D','pages':288,'language':'English'} , {'title':'A', 'author': 'F','rating':'N/A','publisher':'D','pages':288,'language':'English'} ] , 'Category 2': [ {'title':'C', 'author': 'M','rating':'N/A','publisher':'D','pages':288,'language':'English'} , {'title':'c', 'author':'M','rating':'N/A','publisher':'D','pages':288,'language':'English'} , {'title':'B', 'author':'D','rating':'N/A','publisher':'D','pages':288,'language':'English'} ] , 'Category 3': [ {'title':'A', 'author':'F','rating':'N/A','publisher':'D','pages':288,'language':'English'} , {'title':'G', 'author':'G','rating':'N/A','publisher':'D','pages':288,'language':'English'} ] }
    author_expected = [ {'title':'B', 'author':'D','rating':5,'publisher':'D','pages':288,'language':'English', 'category':['Category 1','Category 2']} , {'title':'A', 'author':'F','rating':'N/A','publisher':'D','pages':288,'language':'English', 'category':['Category 1', 'Category 3']} , {'title':'G', 'author':'G','rating':'N/A','publisher':'D','pages':288,'language':'English', 'category':['Category 3']} , {'title':'C', 'author':'M','rating':'N/A','publisher':'D','pages':288,'language':'English', 'category':['Category 2']} , {'title':'c', 'author':'M','rating':'N/A','publisher':'D','pages':288,'language':'English', 'category':['Category 2']} ]
    rate_test_expected_one = [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Business'], 'pages': 112}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'category': ['Money Management'], 'pages': 30}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'language': 'English', 'rating': 3.8, 'publisher': 'Penguin', 'category': ['Business'], 'pages': 272}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': 'English', 'rating': 4.0, 'publisher': 'Hachette UK', 'category': ['Crime'], 'pages': 448}, {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 416}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Mystery'], 'pages': 240}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'language': 'English', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'category': ['Business'], 'pages': 256}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.5, 'publisher': 'Blake Pierce', 'category': ['Detective'], 'pages': 250}]
    rate_test_expected_two = [{'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'category': ['Fiction'], 'pages': 288}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 240}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fantasy'], 'pages': 864}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'category': ['Thrillers'], 'pages': 400}]
    rate_test_expected_three = [{'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Business'], 'pages': 320}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'language': 'English', 'rating': 4.3, 'publisher': 'Macmillan', 'category': ['Fantasy'], 'pages': 1728}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'category': ['Thrillers'], 'pages': 300}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.5, 'publisher': 'Kensington Books', 'category': ['Mystery'], 'pages': 240}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'language': 'English', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'category': ['Humor'], 'pages': 112}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'category': ['Detective'], 'pages': 288}]
    publisher_test_one = {'Biography': [{'author': 'A', 'title': 'B', 'publisher':'C', 'rating': 4.4, 'pages': 24, 'language': 'English'}, {'author': 'M', 'title': 'N', 'publisher':'O', 'rating': 4.0, 'pages': 211, 'language': 'English'}], 'Science fiction': [{'author': 'X', 'title': 'Y', 'publisher':'Z', 'rating': 0.1, 'pages': 1, 'language': 'English'}]}
    publisher_expected_one = [{'author': 'A', 'title': 'B', 'publisher': 'C', 'rating': 4.4, 'pages': 24, 'language': 'English', 'category': ['Biography']}, {'author': 'M', 'title': 'N', 'publisher': 'O', 'rating': 4.0, 'pages': 211, 'language': 'English', 'category': ['Biography']}, {'author': 'X', 'title': 'Y', 'publisher': 'Z', 'rating': 0.1, 'pages': 1, 'language': 'English', 'category': ['Science fiction']}]
    publisher_test_two = {'Biography': [{'author': 'A', 'title': 'B', 'publisher':'C', 'rating': 4.4, 'pages': 24, 'language': 'English'}, {'author': 'M', 'title': 'N', 'publisher':'O', 'rating': 4.0, 'pages': 211, 'language': 'English'}], 'Science fiction': [{'author': 'X', 'title': 'Y', 'publisher':'C', 'rating': 0.1, 'pages': 1, 'language': 'English'}]}
    publisher_expected_two = [{'author': 'A', 'title': 'B', 'publisher': 'C', 'rating': 4.4, 'pages': 24, 'language': 'English', 'category': ['Biography']}, {'author': 'X', 'title': 'Y', 'publisher': 'C', 'rating': 0.1, 'pages': 1, 'language': 'English', 'category': ['Science fiction']}, {'author': 'M', 'title': 'N', 'publisher': 'O', 'rating': 4.0, 'pages': 211, 'language': 'English', 'category': ['Biography']}]
    publisher_test_three = {'Biography': [{'author': 'A', 'title': 'B', 'publisher':'C', 'rating': 4.4, 'pages': 24, 'language': 'English'}, {'author': 'M', 'title': 'N', 'publisher':'O', 'rating': 4.0, 'pages': 211, 'language': 'English'}], 'Science fiction': [{'author': 'X', 'title': 'Y', 'publisher':'C', 'rating': 0.1, 'pages': 1, 'language': 'English'}, {'author': 'A', 'title': 'B', 'publisher':'C', 'rating': 4.4, 'pages': 24, 'language': 'English'}]}
    publisher_expected_three = [{'author': 'A', 'title': 'B', 'publisher': 'C', 'rating': 4.4, 'pages': 24, 'language': 'English', 'category': ['Biography', 'Science fiction']}, {'author': 'X', 'title': 'Y', 'publisher': 'C', 'rating': 0.1, 'pages': 1, 'language': 'English', 'category': ['Science fiction']}, {'author': 'M', 'title': 'N', 'publisher': 'O', 'rating': 4.0, 'pages': 211, 'language': 'English', 'category': ['Biography']}]
    
    print()
    tests_passed = 0
    #sort by title (Developed by Owen Petersen (101233850))
    tests_passed += T015_check_equal.check_equal('sort_books_title Test;', sort_books_title(dictionary), sorted_dictionary_list) 
    
    #sort by author (Developed by Adam Saunders (101217748))
    tests_passed += T015_check_equal.check_equal('sort_books_author Test;', sort_books_author(author_test), author_expected)
    
    #sort by rate (Developed by Isaac Walberg (101234320))
    tests_passed += T015_check_equal.check_equal('sort_books_ascending_rate, test one',rate_test_expected_one,sort_books_ascending_rate(book_category_dictionary('T015_P3_sorting_test_one.csv')))
    tests_passed += T015_check_equal.check_equal('sort_books_ascending_rate, test two',rate_test_expected_two,sort_books_ascending_rate(book_category_dictionary('T015_P3_sorting_test_two.csv')))
    tests_passed += T015_check_equal.check_equal('sort_books_ascending_rate, test three',rate_test_expected_three,sort_books_ascending_rate(book_category_dictionary('T015_P3_sorting_test_three.csv')))
    
    #sort by publisher (Developed by Fiona Cheng (101234672))
    tests_passed += T015_check_equal.check_equal("sort_books_publisher Test One;", publisher_expected_one, sort_books_publisher(publisher_test_one))
    tests_passed += T015_check_equal.check_equal("sort_books_publisher Test Two;", publisher_expected_two, sort_books_publisher(publisher_test_two))
    tests_passed += T015_check_equal.check_equal("sort_books_publisher Test Three;", publisher_expected_three, sort_books_publisher(publisher_test_three))
    
    print('------\nSort Fuction Tests:\nTotal Tests = {0}\nTotal tests Passed = {1}\nTests Failed = {2}\n'.format(8,tests_passed, 8 - tests_passed))