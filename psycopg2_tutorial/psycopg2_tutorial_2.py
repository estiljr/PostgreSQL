import psycopg2
import sys

def main():

    conn_string = "host=localhost dbname=taiwan user=postgres password=060786"
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute("CREATE SCHEMA test")
        cursor.execute("CREATE TABLE test.cars(id INT PRIMARY KEY, name VARCHAR(20), price INT)")
        cursor.execute("INSERT INTO test.cars VALUES(1,'Audi',894378)")
        cursor.execute("INSERT INTO test.cars VALUES(2,'Mercedes',57127)")
        cursor.execute("INSERT INTO test.cars VALUES(3,'Skoda',9000)")
        cursor.execute("INSERT INTO test.cars VALUES(4,'Volvo',29000)")
        cursor.execute("INSERT INTO test.cars VALUES(5,'Bentley',350000)")
        cursor.execute("INSERT INTO test.cars VALUES(6,'Citroen',21000)")
        cursor.execute("INSERT INTO test.cars VALUES(7,'Hummer',41400)")
        cursor.execute("INSERT INTO test.cars VALUES(8,'Volkswagen',21600)")
        conn.commit()

    except psycopg2.DatabaseError,e:
        if conn:
            conn.rollback()
        print 'Error %s' % e
        sys.exit(1)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()