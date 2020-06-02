import logging
import os
import sys
import sqlite3
import threading
import time
import random
import string


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )

DB_FILENAME = 'test.db'

def create_db_table():
    with sqlite3.connect(DB_FILENAME) as conn:
        conn.execute("""CREATE TABLE BOOKS(author VARCHAR, title VARCHAR, id INTEGER PRIMARY KEY)""")

def reader():
    """
    Function to be threaded. Gets book name and author from the database, one at a time.
    """
    with sqlite3.connect(DB_FILENAME) as conn:
        i = 0
        while True:
            # keep track of each loop
            print('try to get a book', i)
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM BOOKS WHERE id={}""".format(i))
            #cursor.execute("SELECT * FROM BOOKS ORDER BY id DESC LIMIT 1")
            # have to iteratote through the cursor to get the result, but it
            # is only printing one thing.
            # If there is not a new book there yet, will get the last book
            for row in cursor:
                if row:
                    print(row)
                    i += 1
            if i > 99:
                break

    print('exit show_books')

def writer():
    """
    Function to be threaded. Over-the-top creating of a random words for author name and book name, 
    dropped into the database one at a time.
    """
    with sqlite3.connect(DB_FILENAME) as conn:
        for i in range(100):
            print('writing', i)
            cursor = conn.cursor()
            first_letter = random.choice(string.ascii_uppercase)
            author = first_letter + ''.join(random.choices(string.ascii_lowercase, k=random.choice(range(5,9))))
            first_letter = random.choice(string.ascii_uppercase)
            book = first_letter + ''.join(random.choices(string.ascii_lowercase, k=random.choice(range(4,12))))
            data = [author, book, i]
            cursor.execute("INSERT INTO BOOKS(author, title, id) VALUES (?, ?, ?)", data)
            conn.commit()
    print('exit writer')


if __name__ == '__main__':
    
    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)
    
    create_db_table()
    ready = threading.Event()
        
    # If you start the writer thread first, it will hog the thread similarly
    # In general, you will see that the database connection does not like to let go
    # Can you figure out how to get the connection to cooperate more? 
    # Under what circumstances are database transactions optimized by threading?

    threads = [
        threading.Thread(name="Reader", target=reader, args=()),
        threading.Thread(name="Writer", target=writer, args=()),
        ]
        
    [t.start() for t in threads]
        
    [t.join() for t in threads]
    print('exit')
