##
## Create application to track and review food eaten
## Should calculate macros and calories

## Structure:
##    Journal table
##     meal table
##      item table
##
##    type key table
## 

## create gui with pyQt

import sqlite3
import os
import argparse
from shutil import rmtree

#
# define initalisation function to
#  create directory in filesystem to store db
#  create db / tables
#

def run_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", help = "rebuild the files and database", action="store_true")
    args = parser.parse_args()
    if args.rebuild:
        rmtree('/tmp/food-log')


def move_to_directory():
    try:
        #move or make
        os.chdir('/tmp/food-log')
    except OSError:
        os.mkdir('/tmp/food-log')
        os.chdir('/tmp/food-log')

def read_statements(path):
    f = open(path, 'r')
    stmt = (f.read()).split(';')
    return stmt
        
def attempt_execution(cur, sql):
    try:
        cur.execute(sql)
    except Exception as e:
        print('error in sql: {0} \n {1}'.format(e, sql))

def initalise_database():
    #find program files and create directory
    move_to_directory()
    
    #run inital sql statements

    conn = sqlite3.connect("fdlg.db")
    cur = conn.cursor()

    print('initalising database')
    try:
        init_sql = read_statements(src_dir + "/init_database.sql")
        for sql in init_sql:            
            attempt_execution(cur, sql)
            print(sql[0:30])
            
    except Exception as e:
        print('exception: {}'.format(e))
    finally:
        conn.commit()
        conn.close()

def create_example_data():
    conn = sqlite3.connect("fdlg.db")
    cur = conn.cursor()
    
    cur.execute('''INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
    values(0.23, 0.029, 0.013, 0.008, 'spinach', 0)'''
    )
    
    cur.execute('''INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
    values(8.84, 0, 0, 1, 'olive oil', 0)'''
    )
    
    cur.execute('''INSERT INTO item(calories, protein, carbohydrates, fat, item_name, type_id)
    values(0.19, 0, 0 , 0, 'red wine vinegar', 0)'''
    )
    
    cur.execute('''INSERT INTO meal(meal_id, item_id, amount, meal_name)
    values(1, 1, 140, 'spinach salad')'''
    )
    
    cur.execute('''INSERT INTO meal(meal_id, item_id, amount, meal_name)
    values(1, 2, 34, 'spinach salad')'''
    )
    
    cur.execute('''INSERT INTO meal(meal_id, item_id, amount, meal_name)
    values(1, 3, 17, 'spinach salad')'''
    )

    cur.execute('''INSERT INTO journal(meal_id)
    values(1)'''
    )

    
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    run_parser()

    src_dir = os.getcwd()
    move_to_directory()
    if not os.access("fdlg.db", os.F_OK):
        initalise_database()
        create_example_data()
