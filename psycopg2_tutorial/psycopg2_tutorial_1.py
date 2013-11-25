
# Small script to show PostgreSQL and Psycopg together

import psycopg2, psycopg2.extras
import sys
import pprint

def main():
    
    # Define our connection string
    conn_string = "host=localhost dbname=taiwan user=postgres password=060786"
    # Print the connection string we will use to connect
    print ("Connecting to database\n ->%s") % (conn_string)
    # Get a connection, if a connection cannot be made an exception will be raised
    try:
        conn = psycopg2.connect(conn_string)
    except:
        print ("I am unable to connect to the database")
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print ("Connected!\n")
    # conn.cursor will return a cursor object, you can use this cursor to perform queries 
    cursor.execute("SELECT * FROM bg_gi.water_course")
    # retrieve the records from the database
    records = cursor.fetchall()
    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    pprint.pprint(records)

if __name__ == "__main__":
    main()






