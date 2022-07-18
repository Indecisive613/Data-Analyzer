### ECOR 1042 Winter 2021-2022 README for Data Analyzer Version 1.0  
Date: April 11, 2022

Contact Information:   
Phone: 613 728 9288  
Email: fionacheng@cmail.carleton.ca

## <ins>Description:</ins>

The project contains a program that allows users to interact with a catalogue of books. Actions include sorting books by certain characteristics, the retrieval of books based on certain characteristics, and the addition and removal of books from the catalogue.  

The project is comprised of 10 files.  
* T015_P4_booksUI.py is the main file.
* T015_P2_add_remove_search_dataset.py, T015_P3_sorting_fun.py, and T015_P5_load_data.py are sub modules used by T015_P4_booksUI.py to interact with the catalogue of books.
google_books_dataset.csv, sorted_book_list.csv, T015_P3_sorting_test_one.csv, T015_P3_sorting_test_three.csv and T015_P3_sorting_test_two.csv are extra datasets used for testing in the sub modules.
* T015_check_equal.py is a sub module used by T015_P3_sorting_fun.py and T015_P2_add_remove_search_dataset.py for testing.

## <ins>Installation:</ins>
Python 3.10.1 or later must be installed.
Only built-in Python modules are used. No external modules must be loaded.

## <ins>Usage:</ins>
\> cd T015_data_analyzer  
\> python T015_P4_booksUI.py

When prompted, enter one of the following commands:
1. L) - This command allows user to load a file of their choosing.
2. A) - This command allows users to add a new book to the dictionary.
3. R) - This command allows users to remove a book from the dictionary.
4. G) - This command allows users to get books based on specific information. 
 * T) - This command allows users to get books by title.
 * R) - This command allows users to get books by rate.
 * P) - This command allows users to get books by author.
 * A) - This command allows users to get books by publisher.
 * C) - This command allows users to get book by category.
5. GCT) - This command allows users to get all categories for a book title.
6. S) - This command allows users to sort books based on specific characteristics.
 * T) - This command sorts the dictionary by title.
 * R) - This command sorts the dictionary by rate.
 * P) - This command sorts the dictionary by publisher.
 * C) - This command sorts the dictionary by category.
7. Q) - This command allows the user to exit the program.

Commands can be typed either capital or lowercase.  
It is recommended to load the file before proceeding with the other commands.

## <ins>Credits:</ins>
The following is a list of the contributors along with their associated functions:

Fiona Cheng (Student number 101234672)
* add_books
* remove_books
* sort_books_author
* add_book
* get_book_by_title
* check_equal
* test_addition
* test_removal

Isaac Walberg (Student number 101234320)
* get_books
* sort_books_title
* get_books_by_category
* get_books_by_publisher

Adam Saunders (Student number 101217748)
* GCT
* sort_books_publisher
* remove_book
* get_books_by_author

Owen Petersen (Student number 101233850)
* book_category_dictionary
* load_data
* sort_books
* dictionary_list
* sort_books_ascending_rate
* sorted_book_list_title
* get_books_by_rate
* get_all_categories_for_book_title

_Copyright 2022 by Fiona Cheng, Isaac Walberg, Adam Saunders and Owen Petersen_
