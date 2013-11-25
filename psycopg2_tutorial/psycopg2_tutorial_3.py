## Creating table using the convenience of executemany() method

import psycopg2
import sys

def main():

    conn_string = "host=localhost dbname=taiwan user=postgres password=060786" 
    cars = (
        (1, 'Audi', 52642),
        (2, 'Mercedes', 57127),
        (3, 'Skoda', 9000),
        (4, 'Volvo', 29000),
        (5, 'Bentley', 350000),
        (6, 'Citroen', 21000),
        (7, 'Hummer', 41400),
        (8, 'Volkswagen', 21600)
    )
    # Storing data in the database
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS test.cars")
        cursor.execute("CREATE TABLE test.cars(id INT PRIMARY KEY, name TEXT, price INT)")
        query = "INSERT INTO test.cars(id,name,price) VALUES (%s,%s,%s)"
        cursor.executemany(query,cars)
        conn.commit()
       
    except psycopg2.DatabaseError,e:
        if conn:
            conn.rollback()
        print ("Error %s" % e)
        sys.exit(1)
    #finally:
    #    if conn:
    #        conn.close()

    # Retrieving data from the database
    cursor.execute("SELECT * FROM test.cars")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if conn:
        conn.close()

    ##==============================================================
    # Retrieving data one by one
    conn_string = "host=localhost dbname=taiwan user=postgres password=060786"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test.cars")
    print("=====")
    while True:
        one_row = cursor.fetchone()
        if one_row == None:
            break
        print one_row[0], one_row[1], one_row[2]
    if conn:
        conn.close()



if __name__ == "__main__":
    main()