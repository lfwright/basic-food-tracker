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

def run_sql(sql_file, verbose = False):
    try:
        conn = sqlite3.connect("fdlg.db")
        cur = conn.cursor()

        init_sql = read_statements(src_dir + "/" + sql_file)
        
        for sql in init_sql:            
            attempt_execution(cur, sql)
            if verbose:
                print(sql[0:30])
            
    except Exception as e:
        print('exception: {}'.format(e))
    finally:
        conn.commit()
        conn.close()


def initalise_database():
    #find program files and create directory
    move_to_directory()
    
    #create database initialisation statements

    print('initalising database')

    run_sql("init_database.sql", True)
    
def create_example_data():

    #load example data
    
    print('load example data')

    run_sql("example_data.sql")

    
if __name__ == "__main__":
    run_parser()

    src_dir = os.getcwd()

    move_to_directory()
    if not os.access("fdlg.db", os.F_OK):
        initalise_database()
        create_example_data()
