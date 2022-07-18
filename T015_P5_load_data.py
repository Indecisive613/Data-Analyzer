#Owen Petersen (101233850) (Developer)
#Adam Saunders (101217748) (Reviewer)
#Fiona Cheng (101234672) (Reviewer)
#Isaac Walberg (101234320) (Reviewer)

def book_category_dictionary(filename: str) -> dict:
    """Takes a file containing a list of book data and returns a dictionary containing the data sorted by category.
    Duplicates are removed.
    Developed By: Owen Petersen
    
    >>>book_category_dictionary('google_books_dataset.csv')
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'language': 'English'}, ...], ...}
    """
    file = open(filename, 'r')
    book_dictionary = {}
    subsection = ['title', 'author', 'rating', 'publisher', 'pages', 'category', 'language']
    category_index = subsection.index('category')
    subsection_removed = subsection[:]
    subsection_removed.pop(category_index)
    
    for line in file:
        if 'title,author,rating,publisher,pages,category,language' not in line:
            line_list = line.rstrip('\n').split(sep=',')
            if line_list[subsection.index('rating')] != 'N/A':
                line_list.insert(subsection.index('rating'), float(line_list[subsection.index('rating')]))
                line_list.pop(subsection.index('rating') + 1)
            line_list.insert(subsection.index('pages'), int(line_list[subsection.index('pages')]))
            line_list.pop(subsection.index('pages') + 1)
            line_data = {}
            line_list_removed = line_list[:]
            line_list_removed.pop(category_index)
            for index in range(len(subsection_removed)):
                line_data.update({subsection_removed[index] : line_list_removed[index]})
            if line_list[category_index] in book_dictionary:
                if line_data not in book_dictionary[line_list[category_index]]:
                    book_dictionary[line_list[category_index]] = book_dictionary[line_list[category_index]] + [line_data]
            if line_list[category_index] not in book_dictionary:
                book_dictionary[line_list[category_index]] = [line_data]
    file.close()
    return book_dictionary