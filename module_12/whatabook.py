""" 
    Title: what_a_book.py
    Author: Tristan Boetcher
    Date: 5/14/22
    Description: WhatABook program; Console program that interfaces with a MySQL database
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#  method to display main menu and get user input
def show_menu():
    print ("\n- Welcome to WhatABook -")
    print("\nMain Menu\n\t1. View Books\n\t2. View Store Locations\n\t3. My Account\n\t4. Exit Program")
      
    menu_selection = input("\nPlease enter your selection :\t") # user input

    while menu_selection not in ("1", "2", "3", "4"):
        menu_selection = input("\n*Invalid selection*\n\nPlease enter a selection between 1-4 :\t") # if selection is invalid

    if menu_selection == "1": # if 1 is selected it will show the books
        show_books(cursor)

    if menu_selection == "2": # if 2 is selected it will show the locations
        show_locations(cursor)

    if menu_selection == "3": # if 3 is selected it will allow you to enter user id
        user_id = validate_user(cursor)
        show_account_menu(cursor, user_id)

    if menu_selection == "4": # if 4 is selected you can exit the program
        print("\n\tExit WhatABook")
        exit()

#  method to get and display books
def show_books(_cursor):

    print("\n\t- BOOKS -\n") # print title
    
    cursor.execute("SELECT book_id, book_name, author, details " + # select statement for books
                    "FROM book ORDER BY book_id")

    books = cursor.fetchall()
    for book in books: # print information about the books
        print("\tBook ID:  {}\n\t\tBook Name:\t{}\n\t\tAuthor:\t\t{}\n\t\tDetails:\t{}\n".format(book[0], book[1], book[2], book[3]))

    show_menu() # show menu

#  method to get and display location information
def show_locations(_cursor):

    _cursor.execute("SELECT store_id, locale from store") # select statement for location

    locations = _cursor.fetchall()

    print("\n\t- STORE LOCATIONS -\n") # title

    for location in locations:
        print("\t{}\n".format(location[1])) # print location details
    
    show_menu() # show menu

#  method to get user id and validate
def validate_user(cursor):
    
    print ('\n\t- MY ACCOUNT -\n') # title

    cursor.execute("SELECT user_id FROM user") # select statement for users
    user_id_list = []
    query_results = cursor.fetchall()
    for row in query_results:
        user_id_list.append(str(row[0])) 

    user_id = input("\tPlease enter user id:\t ") # get user input

    while (user_id not in user_id_list):
        user_id = input("\n\t*Invalid user id*\n\n\tPlease enter a valid user id:\t ") # error message

    return user_id 

#  method to display account menu and get input
def show_account_menu(cursor, user_id):
    
    cursor.execute("SELECT first_name FROM user" + # select statement for account
                    " WHERE user_id = " + str(user_id))
    first_name = cursor.fetchall()
    
    print("\n\tAccount Menu\n\n\t1. Wishlist\n\t2. Add Book\n\t3. Main Menu") # print options

    menu_selection = input("\n\tPlease enter your selection:\t") # user input
    
    while menu_selection not in ("1", "2", "3"):
        menu_selection = input("\n\t*Invalid selection*\n\n\tPlease enter a valid selection:\t") # invalid error message

    if menu_selection == "1":
        show_wishlist(cursor, user_id) # if user selects 1 it will show the wishlist
    
    if menu_selection == "2": # if user selects 2 it will show the books that can be added to wishlist
        book_id = show_books_to_add(cursor, user_id)
        add_book_to_wishlist(cursor, user_id, book_id) # add book to wishlist option
    
    if menu_selection == "3": # if user selects 3 will bring user back to main menu
        show_menu() # show menu

#  method to show books in a users wishlist
def show_wishlist(cursor, user_id):
    
    print("\n\t\t- Your Wishlist -") # title
    
    cursor.execute("SELECT book.book_name, book.author" + # select statement for wishlist
                    " FROM book" +
                    " INNER JOIN wishlist ON book.book_id = wishlist.book_id" +
                    " INNER JOIN user ON wishlist.user_id = user.user_id" +
                    " WHERE user.user_id = " + user_id)

    user_wishlist = cursor.fetchall()
    
    for row in user_wishlist: # print title and author for wishlist items
        print(f"\n\tTitle: {row[0]}")
        print(f"\tAuthor: {row[1]}\n")

    show_account_menu(cursor, user_id)

#  method to display books that are not already in the wishlist and get input
def show_books_to_add(cursor, user_id):
    
    print("\n\t\t- Available Books -") # title

    cursor.execute("SELECT book_id, book_name, author, details FROM book" + # select statement for adding books to wishlist
                    " WHERE book_id NOT IN (SELECT book_id FROM wishlist" +
                    " WHERE user_id = " + str(user_id) + ")" +
                    " ORDER BY book_id")
    
    books_to_add = cursor.fetchall() # showing books to add

    for book in books_to_add: # print book information
        print(f"\nBook Id:    {book[0]}")
        print(f"\tTitle: {book[1]}")
        print(f"\tAuthor: {book[2]}")
        print(f"\tDetails: {book[3]}\n")

    books_to_add_ids = []
    for book in books_to_add:
        books_to_add_ids.append(str(book[0])) # append list

    book_id = input("\n\t\tEnter Book Id that you want to add to your list or X to return to your Account Menu:\t")
         
    while book_id not in books_to_add_ids and book_id.lower() != "x": # error message
        book_id = input("\n\t\t***Invalid selection.***\n\n\t\tEnter valid book id or X to return to the Account Menu:\t")

    if book_id.lower() == "x": # show account menu
        show_account_menu(cursor, user_id)
    else:
        return book_id # return to book ids

#  method to add books
def add_book_to_wishlist(cursor, user_id, book_id):

    # insert statement for wishlist
    cursor.execute("INSERT INTO wishlist (user_id, book_id)" + "VALUES (" + user_id + ", " + book_id + ")")

    db.commit() # commit changes

    cursor.execute("SELECT book_name FROM book WHERE book_id = " + book_id) # select statement for books
    book_names = cursor.fetchall() # get book names
    
    for row in book_names:
        book_name = row[0]
    
    # message to say that the book was added
    print ("\n\t\tBook id {}: {} was successfully added to your wishlist!".format(book_id, book_name))

    show_account_menu(cursor, user_id) # account menu
       
try:
    # connect to database
    db = mysql.connector.connect(**config)

    # cursor for MySQL queries
    cursor = db.cursor()
    
    # display Main Menu
    show_menu()


# error handling
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\tInvalid username or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\tInvalid database")

    else:
        print(err)

# close database connection
finally:
    
    db.close()
