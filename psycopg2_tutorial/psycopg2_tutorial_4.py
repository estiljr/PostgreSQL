## The default cursor returns the data in a tuple of tuples. 
## When we use a dictionary cursor, the data is sent in a form of Python dictionaries. 
## This way we can refer to the data by their column names.
import psycopg2
import psycopg2.extras
import sys

def main():
    conn_string = "host=localhost dbname=taiwan user=postgres password=060786"
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM test.cars"
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print (row['id'], row['name'], row['price'])
        
    except psycopg2.DatabaseError,e:
        print ("Error %s" % e)
        sys.exit(1)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
