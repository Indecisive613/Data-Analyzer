# Isaac Walberg 101234320 (Developer)
# Adam Saunders 101217748 (Reviewer)
# Fiona Cheng 101234672 (Reviewer)
# Owen Petersen 101233850 (Reviewer)

from T015_P5_load_data import *
from T015_P2_add_remove_search_dataset import *
from T015_P3_sorting_fun import*

def load_data()-> dict:
    """
    Returns a catalogue of books organized by category based on the file name provided by user input.
    Developed by Owen Petersen 101233850
    
    >>>load_data()
    Please enter a file to load: google_books_dataset.csv
    File loaded successfully
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'language': 'English'}, ...], ...}
    """

    file = book_category_dictionary(input('Please enter a file to load: '))
    print("File loaded successfully.")
    return file

def sort_books(catalogue: dict) -> None:
    """
    Prompts the user to enter a specific type of sorting and sorts catalogue based on user input.
    The user can sort by title, by rate, by publisher and by category.
    Prints the sorted dictionary to the console.
    Developed by Owen Petersen 101233850
    
    >>>sort_books(book_category_dictionary("google_books_dataset.csv"))
    Please type your command: s
    How do you want to sort? t
    ------------------------------
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'category': ['Fiction', 'Thrillers'], 'pages': 300}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'pages': 864},...]
    
    >>>sort_books(book_category_dictionary("google_books_dataset.csv"))
    Please type your command: s
    How do you want to sort? Title
    ------------------------------ 
    No such sub-command
    """
    user_input = input('How do you want to sort?').strip().upper()
    if user_input in sort_inputs:
        print(line_spacer)
        print(sort_inputs[user_input](catalogue))
    else:
        print(line_spacer, '\nNo such sub-command')
        
def get_books(catalogue: dict) -> None:
    """
    Prompts the user for input and executes the associated action for the dataset defined by catalogue.
    Developed by Isaac Walberg 101234320
    
    The following 5 descriptions contain the details for the possible actions.
    1. Getting books by title returns True if the title exists in the dictionary.
    2. Getting books by rate returns the number of books in a given dictionary of books which fall within the specified rating
    3. Getting books by author returns the number of books written by the given author. Also prints the following:
    The author [author] has published the following books:
    Book 1: [Title], rate: [Rating]
    Book 2: [Title], rate: [Rating]
    4. Getting books by publisher returns the total amount of books from a set publisher exluding duplicates, 
    along with printing the title of each book along with the author under the set publisher
    5. Getting books by category returns the total amount of books in a given catagory, 
    along with printing the title of each book along with the author under the set category
    
    >>>get_books(book_category_dictionary("google_books_dataset.csv"))
    What do you want to get: a
    What author do you want to get: Steven D. Levitt
    The author Steven D. Levitt has published the following books:
    Book 1: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything, rate: 3.8
    Book 2: Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain, rate: 4.3
    
    >>>get_books(book_category_dictionary("google_books_dataset.csv"))
    What do you want to get: t
    What title do you want to get: Not a title
    The book has NOT been found
    """
    user_input = input('What do you want to get: ').strip().upper()
    if user_input in get_inputs_sub:
        if user_input in get_inputs:
            if user_input == 'R':
                gotten = input(get_inputs_sub[user_input])
                if gotten in [str(1),str(2),str(3),str(4),str(5)]:
                    rates = get_inputs[user_input](catalogue,int(gotten))
                    print("Total number of books with ratings between {0} and {1}: {2}".format(gotten, int(gotten)+1, rates))
                else:
                    print('Input must be an integer')
            else:
                gotten = input(get_inputs_sub[user_input])
                books = get_inputs[user_input](catalogue,gotten)
                print("Total number of books within specified parameters:", books+0)
        else:
            print(line_spacer, '\nNo such sub-command')
    else:
        print(line_spacer, '\nNo such sub-command')    
            
def add_books(catalogue: dict) -> None:
    """
    Asks the user for book information and adds the book to catalogue.
    Developed by Fiona Cheng 101234672
    
    >>>add_books(book_category_dictionary("google_books_dataset.csv"))
    Please enter the title of the book: People
    Please enter the author of the book: Nancy N
    Please enter the language of the book: Spanish
    Please enter the publisher of the book: Knowledge House
    Please enter the category of the book: History
    Please enter the rating of the book: n/a
    Please enter the number of pages in the book: 22
    The book has been added correctly
    """
    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    language = input("Please enter the language of the book: ")
    publisher = input("Please enter the publisher of the book: ")
    category = input("Please enter the category of the book: ")
    rating = input("Please enter the rating of the book: ")
    if rating != 'n/a' and rating != 'N/A':
        rating = float(rating)
    pages = int(input("Please enter the number of pages in the book: "))
    new_book = (title, author, language, publisher, category, rating, pages)
    add_book(catalogue, new_book)
        
def remove_books(catalogue: dict) -> None:
    """
    Removes a book from catalogue based on input from the user.
    Developed by Fiona Cheng 101234672
    
    >>>remove_books(book_category_dictionary("google_books_dataset.csv"))
    Please enter the title of the book: Deadpool Kills the Marvel Universe
    Please enter the category of the book: Comics
    The book has been removed correctly
    
    >>>remove_book(book_category_dictionary("google_books_dataset.csv"))
    Please enter the title of the book: Google Chrome
    Please enter the category of the book: Biography
    There was an error removing the book. Book not found
    """
    title = input("Please enter the title of the book: ")
    category = input("Please enter the category of the book: ")
    remove_book(catalogue, title, category)
    
def GCT(catalogue: dict) -> None:
    """
    Prints all the categories for a title chosen by the user from catalogue. Also prints the total number of categories associated with the book.
    Developed by Adam Saunders 101217748
    
    >>>GCT(book_category_dictionary("google_books_dataset.csv"))
    Please type the Title: fkjdfjdl
    The book title fkjdfjdl belongs to the following categories:
    Total number of categories for fkjdfjdl: 0
    
    >>>GCT(book_category_dictionary("google_books_dataset.csv"))
    Please type the Title: Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain
    The book title Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain belongs to the following categories:
    Category 1: Business
    Total number of categories for Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain: 1
    """
    inputted_title = input('Please type the Title: ')
    print("Total number of categories for", inputted_title + ":", get_all_categories_for_book_title(catalogue, inputted_title))
    
valid_inputs = {'L':load_data, 'S':sort_books, 'G': get_books,'A':add_books, 'R':remove_books, 'GCT':GCT, 'Q':quit}
sort_inputs = {'T':sort_books_title, 'R':sort_books_ascending_rate, 'P':sort_books_publisher,'A':sort_books_author}
get_inputs = {'T': get_book_by_title,'R':get_books_by_rate,'A':get_books_by_author, 'P':get_books_by_publisher, 'C': get_books_by_category}
get_inputs_sub = {'T':'What title do you want to get: ', 'R' : 'What rate do you want to get (must be integer): ', 'A':'What author do you want to get: ', 'P':'What publisher do you want to get: ','C':'What Category do you want to get: '}
menu_list = ["The available commands are: ","\t1. L)oad file","\t2. A)dd Book","\t3. R)emove Book","\t4. G)et Books \n\t\tT)itle R)ate A)uthor P)ublisher C)ategory","\t5. GCT) Get all Categories for book Title","\t6. S)ort books \n\t\tT)itle R)ate P)ublisher A)uthor","\t7. Q)uit"]

#main script
line_spacer = '------------------------------'
loop = True
file = None

while loop:
    for line_text in menu_list:
        print(line_text)       
    print(line_spacer)
    user_input = input('Please type your command: ').strip().upper()
    if user_input == 'Q':
        loop = False
    elif user_input not in valid_inputs:
        print(line_spacer, '\nNo such command')
    elif file == None and user_input != 'L':
        print(line_spacer, '\nFile not loaded')
    elif user_input == 'L':
        file = load_data()
    else:
        valid_inputs[user_input](file)