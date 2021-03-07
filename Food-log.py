##
## Create application to track and review food eaten
## Should calculate macros and calories

## Structure:
##    Journal table
##     meal table
##      item table
##
##    item - key table
##    meal - keys table

## create gui with pyQt

import sqlite
import os

#
# define initalisation function to
#  create directory in filesystem to store db
#  create db / tables
#

def move_to_directory():
    try:
        #move or make
        os.chdir('/tmp/food-log')
    except OSError:
        os.mkdir('/tmp/food-log')
        os.chdir('/tmp/food-log')

def initalise_database():
    #find program files and create directory
    move_to_directory()

    #run inital sql queries
    conn = sqlite3.connect("fdlg.db")
    cur = conn.cursor()

    try:
        cur.execute('''CREATE TABLE item
                    (item_id INTEGER PRIMARY KEY
                    ,calories REAL
                    ,protein REAL
                    ,carbohydrates REAL
                    ,fat REAL
                    ,type TEXT)'''
        )
        
        cur.execute('''CREATE TABLE meal
                   (meal_id INTEGER PRIMARY KEY
                   ,item_id INTEGER
                   ,amount REAL)'''
        )

        cur.execute('''CREATE TABLE journal
                   (journal_id INTEGER PRIMARY KEY
                   ,date_id INTEGER
                   ,meal_id INTEGER)'''
        )


        cur.execute('''CREATE TABLE item_key
                   (item_id INTEGER PRIMARY KEY
                   ,item_name TEXT)'''
        )


        cur.execute('''CREATE TABLE meal_key
                   (meal_id INTEGER PRIMARY KEY
                   ,meal_name TEXT)'''
        )


        cur.execute('''CREATE TABLE current_id
                   (journal_id INTEGER 
                   ,meal_id 
                   ,item_id)'''
        )


        cur.execute('''INSERT INTO current_id)
    
    conn.commit()
    conn.close()

def create_example_date():
    conn = sqlite3.connect("fdlg.db")

    
if __name__ == "__main__":
    move_to_directory()
    if not os.access("fdlg.db", os.F_OK):
        initalise_database()
        create_example_data()

    
