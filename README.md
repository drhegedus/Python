# Python
First python project from a beginners online course


BEGINNER PYTHON COURSE PROJECT INFO:
Jan 2019
Daphne Hegedus


Notes to consider:
- I formatted my program to require a name, author, and genre but also accept either both or one of: publisher and year
- I also included the sort options purely because I wanted to know a quick way to sort dictionaries in lists via their values (sort doesn't update the file, just the usable data for that run)
- I used files as the way to store and retrieve data so that I could practice its use
	-> Also, I decided to use the username idea and store the books/library info under username.txt files
	-> at the start of the program the user is prompted to enter a username: if pre-existed it opens that file, otherwise it makes a new one
- adding a book updates the library list AND the file (uses append)
- searching looks for both a substring of or whole value entered and is not case sensitive
- to run: run from the LibraryUserInterface.py in IDLE or another IDE
- included is a dheg.txt file that I used to test the program 
	-> use it by moving that file to the same directory as the .py files and enter 'dheg' as the username when prompted



PROJECT INSTRUCTIONS:
from Tony Staunton's Python 3: A Beginners Guide to Python Programming Skillshare course (Jan 2019)

Your challenge is to create a book storage application. The application should allow users to manage their book collection.

To complete the challenge your application will need to have three main features:

	1. It must allow users to add new books to the collection

	2. The application must allow users to view all the books in their collection

	3. The application must allow users to find a book within their collection by any of its attributes

Here are some pointers to get you started

	Books should be dictionaries, and you can define the structure of the dictionary to be anything you like. For example you could choose to have books as dictionaries with the following keys:

	{

    	'name': 'Elon Musk',

    	'author': 'Ashlee vance',

    	'genre': 'biography'

	}

	Or you may choose to have more keys, such as:

	{

   		'name': 'Elon Musk',

    	'author': 'Ashlee vance',

    	'genre': 'biography',

    	'publisher': 'virgin',

    	'published date': '2015'

	}

How should books be stored?

	This is up to you, to complete the challenge a user should be able to print them to the screen, find and retrieve them. I would suggest that you use a list. If you are comfortable using files then you could go with that option.

How to find moves?

	With your structure defined, users should be able to "find all books published in 2015" or "find all movies that are biographies". To do this users should be able to tell your application what property they are looking for, is it name, genre, published date or something else. A user should also be able to tell your application Elon Musk, or biography for the examples above.

	With both property and the value, a user should be able to find all books that match both. The challenge does not close until January 30th so you have plenty of time to think about your solution. 

