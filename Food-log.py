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
                    ,item_name TEXT NOT NULL
                    ,type_id INTEGER)'''
        )
        
        cur.execute('''CREATE TABLE meal
                   (meal_id INTEGER NOT NULL
                   ,item_id INTEGER NOT NULL
                   ,amount REAL
                   ,meal_name TEXT NOT NULL
                    PRIMARY KEY (meal_id, item_id)
                    FOREIGN KEY (item_id) REFERENCES item(item_id)
                   )'''
        )

        cur.execute('''CREATE TABLE journal
                   (journal_id INTEGER PRIMARY KEY
                   ,date_id INTEGER NOT NULL
                   ,meal_id INTEGER NOT NULL
                    FOREIGN KEY (meal_id) REFERENCES meal(meal_id)
                   )'''
        )

        cur.execute('''CREATE TABLE type_key
                   (type_id INTEGER PRIMARY KEY
                   ,type_name TEXT NOT NULL)'''
        )

        conn.commit()

        cur.execute('''INSERT INTO type_key(type_id, type_name)
                       (0, 'grams');

                       INSERT INTO type_key(type_id, type_name)
                       (1, 'single');

                       INSERT INTO type_key(type_id, type_name)
                       (2, 'volume');'''
        )
        conn.commit()
        conn.close()

def create_example_data():
    conn = sqlite3.connect("fdlg.db")
    cur = conn.cursor()

    cur.execute('''INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
                   (0.23, 0.029, 0.013, 0.008, 'spinach', 0);

                   INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
                   (8.84, 0, 0, 1, 'olive oil', 0);

                   INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
                   (0.19, 0, 0 , 0, 'red wine vinegar', 0);

                   INSERT INTO meal(meal_id, item_id, amount, meal_name)
                   (1, 1, 140, 'spinach salad');

                   INSERT INTO meal(meal_id, item_id, amount, meal_name)
                   (1, 2, 34, 'spinach salad');

                   INSERT INTO meal(meal_id, item_id, amount, meal_name)
                   (1, 3, 17, 'spinach salad');
                   '''
    )
    conn.commit()
    conn.close()

    
if __name__ == "__main__":
    move_to_directory()
    if not os.access("fdlg.db", os.F_OK):
#        initalise_database()
#        create_example_data()
