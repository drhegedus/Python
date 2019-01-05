## Creator: Daphne Hegedus
## Date: 04 / 01 / 2019
## Provides the user interface and menu loop for the Library Project





#imports the Library class and the itemgetter method -> for sorting purposes
from Library import Library
from operator import itemgetter

class LibraryUserInterface():
	"""provides the user interface and main method/menu of the Library System"""

	def add_to_library(my_library):
		"""gets input from the user to make a new book and adds it to the library"""
		new_book = []
		name = input("\n\nEnter the name of your new book: ").strip()	
		author = input("\n\nEnter the author of " + name.title() + ": ").strip()	
		genre = input("\n\nWhat type of book is " + name.title() + "? ").strip()	
		new_book.append(name)
		new_book.append(author)
		new_book.append(genre)
					
		publisher = input("\n\nWho is the publisher of " + name.title() + "? (if not known press enter): ").strip()	
		new_book.append(publisher)
		year = input("\n\nWhat year was " + name.title() + " published? (if not known press enter): ")
		new_book.append(year)
		

		#with all of the info for a book in a list it makes a book (using the method in the Library class)		
		book_to_add = my_library.make_book(new_book)
		#it then adds the book to the library w/in the Library class (this also updates the file and the list)
		my_library.add_book(book_to_add)

		print("\nYou now have " + str(my_library.num_of_books) + " books.\n")


	def sort_books(my_library, keyword):
		"""gives the user the ability to sort the books (doesn't update the file, just the data for this run)"""
		
		#main menu only gives the option of name or author and this is hardcoded in = can assume keyword is one of these
		if keyword == 'name':
			#uses the itemgetter method in operator (imported in) to sort by the value of the 'name' keywords for each book
			my_library.books.sort(key=itemgetter('name'))
			print("Your books are now sorted alphabetically by name.\n")
			my_library.print_all_books()
		#the same is done for the author option
		elif keyword == 'author':
			my_library.books.sort(key=itemgetter('author'))
			print("Your books are now sorted alphabetically by author.\n")
			my_library.print_all_books()
			

	def find_matching_books(my_library):
		"""takes user input for a key:value pair to match to books and prints out those books"""
		while True:
		#loop is used for if the user wants to change their search before it is completed
			keyword = input("\nWhat keyword are you looking for? (this could be a name, author, genre, publisher, or year): ")
			phrase = input("What " + keyword + " are you searching for? ")
			
			#gives the user the option to change the search
			print("Verify that you are searching for a book with the " + keyword + " of " + phrase + ".") 
			correct = input("Press enter for yes or any other key followed by enter for no: ")
			#if the user verifies the search as correct -> exit loop with break, otherwise give another chance to search
			if correct == '':
				break

		#uses the get_matching_books function in Library class to match the key:value pair -> this returns a list 
		matching = my_library.get_matching_books(keyword, phrase)
		
		#if there are matching books -> print them out
		if len(matching) > 0:
			print("\nThese books match your search: ")
			for book in matching:
				print(book['name'].title() + " by " + book['author'].title() + " (" + book['genre'].title() + ")")
		#otherwise inform the use of unsuccessful search
		else:
			print("\nThere are no books in your library that match that search.")



	#-------------------------------------------------------------------------------------------------------------------------------------
	# Main Menu and interaction:

	print("\nWelcome to the Library System!")
	library_made = False

	#keeps asking for a username until a successful library (empty or filled) is created using a flag
	while not library_made:
		#makes a Library using the Library class -> __init__ deals with the username to username.txt conversion
		username = input("\nPlease enter your username (if new enter what would want as username): ")
		my_library = Library(username)
		if my_library:
			library_made = True
		else:
			print("\nPlease try again.")

	#uses a loop to keep repeating the menu options and operations until the 6th QUIT option is selected
	while True:
		print("\n--------------------------------------------------\n")
		print("Enter the number next to the option you would like to do:")
		print("1. Add a book to my library")
		print("2. Sort your books alphabetically by name")
		print("3. Sort your books alphabetically by author")
		print("4. Search through your books with a matching value")
		print("5. Print out all the books in your library")
		print("6. Quit the program")
		
		entered = input("Option: ")
		try:
			#make sure the input is an integer between 1-6
			choice = int(entered)
			if choice > 0 and choice < 7:
				if choice == 6:
					#terminates the loop and the program w/ break
					print("Thank you for using the Library System. Goodbye!")
					break

				#CALL CORRESPONDING METHODS ABOVE FOR EVERY MENU OPTION (see comments above)
				elif choice == 1:
					add_to_library(my_library)

				elif choice == 2:
					sort_books(my_library, 'name')

				elif choice == 3:
					sort_books(my_library, 'author')

				elif choice == 4:
					find_matching_books(my_library)

				elif choice == 5:
					my_library.print_all_books()

			# input is not valid (1-6) -> loop again
			else:
				print("Choice an option 1 - 5. Try again.")
		#if input not an integer -> loop again after error message
		except ValueError:
			print("Please enter a number. Try again.")


