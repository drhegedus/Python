## Creator: Daphne Hegedus
## Date: 04 / 01 / 2019
## Provides the Library class code that stores and updates a file of books' info





#for checking if a file already exists under a username
import os.path

class Library():
	"""stores a list of Book Objects"""

	def __init__(self, username):
		"""initializes the library book list from a file and number of books"""
		
		#if the username entered doesn't have an existing file/library -> create one
		if not os.path.exists(username + '.txt'):
			with open(username + '.txt', 'w'):
				print("Welcome " + username + "! A library under this username has been created for you.")
				self.books = []
				self.num_of_books = 0

		else:
			#otherwise open up the file -> read in the data
			try:
				self.books = []
				with open(username + '.txt') as file_object:
					for line in file_object:
						#reads file line by line and splits each info by ' ' character
						#makes a new book out of that info and adds it to the list
						#assumes format is "name author	genre " OR "name author genre publisher year" split by tabs
						book_info = line.strip().split("\t")
						
						#if length = 3 then 2 empty strings appended for publisher and year
						if len(book_info) == 3:
							book_info.append("")
							book_info.append("")
						elif len(book_info) == 4:
							try:
								#if length of 4 - is fourth the year (an int) or is it the publisher
								#if 4th is year -> add empty string before year
								year = int(book_info[3])
								book_info.append("")
								book_info[4] = str(year)
								book_info[3] = ""
							except ValueError:
								#4th is publisher add an empty string for year
								book_info.append("")

						#make a book and add it to library of books
						new_book = self.make_book(book_info)
						self.books.append(new_book)

				#sets the number of books in the library
				self.num_of_books = len(self.books)

			#handles exceptions
			except FileNotFoundError:
				print("Your Library could not be created because the file of books was not found.")
			
			#file was open successfully -> welcome back the returning user
			else:
				print("Welcome back, " + username + "!" )



	def make_book(self, book_info):
		"""makes a book out of a list of info"""
		#assumes the info is in the for [name, author, genre, publisher, year] = length of 5
		new_book = {}
		new_book['name'] = book_info[0]
		new_book['author'] = book_info[1]
		new_book['genre'] = book_info[2]
		new_book['publisher'] = book_info[3]
		new_book['year'] = book_info[4]
		return new_book

	def add_book(self, new_book):
		"""adds a book to the list and increments the number of books"""
		#new_book is a dictionary -> convert to str for file
		
		#try to open the file in append mode
		try:
			with open(self.filename, 'a') as file_object:

				#append the info to the end of the file
				file_object.write("\n" + new_book['name'] + "\t" + new_book['author'] + "\t" + new_book['genre'] + "\t" + new_book['publisher'] + "\t" + new_book['year'])
				#add the book to the list/library and increment the number of books
				self.books.append(new_book)
				self.num_of_books = self.num_of_books + 1
			print("Your book was added and stored to the original file.")

		except FileNotFoundError:
			print("Your book could not be added because the file of books was not found.")


	def get_matching_books(self, keyword, value):
		""""returns a list of books that have the same keyword : value pair"""
		
		matching_books = []
		#loop through the books for a match
		for book in self.books:
			try:
				if book[keyword.lower()].lower() == value.lower() or value.lower() in book[keyword.lower()].lower():
					#looks for full value of value as a substring of the full value
					matching_books.append(book)
			#catches the cases where a book may not have a specific keyword -> moves onto the next w/out alerting user
			except KeyError:
				pass
		return matching_books


	def padding(self, phrase):
		"""for formatting the full printed list of books nicely (each column is 30 long)"""
		amt = 30 - len(phrase)
		pad = " " * amt
		return pad

	def print_all_books(self):
		"""Prints out a full list of the books and their info to the screen using padding function^^ """
		print("\nThese are your books: ")
		print("Title" + self.padding("Title") + "Author" + self.padding("Author") + "Genre" + self.padding("Genre") + "Publisher" + self.padding("Publisher") + "Year\n")

		for book in self.books:
				print(book['name'].title() + self.padding(book['name']) + book['author'].title() + self.padding(book['author']) + book['genre'].title() + self.padding(book['genre']) + book['publisher'].title() + self.padding(book['publisher']) + book['year'])


				
