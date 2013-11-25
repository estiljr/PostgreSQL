## Metadata

import psycopg2
import sys

con = None
try:
    con = psycopg2.connect("host=localhost dbname=taiwan user=postgres password=060786")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM test.cars")
    # We get the column names from the description property of the cursor object.
    col_names = [cn[0] for cn in cursor.description] # [0] refers to the column names metadata

    rows = cursor.fetchall()
    # This line prints three column names of the cars table.
    print ("%s %-10s %s" % (col_names[0], col_names[1], col_names[2]))
    # We print the rows using the for loop. The data is aligned with the column names.
    for row in rows:
        print("%2s %-10s %s" % (row))

except psycopg2.DatabaseError,e:
    print ("Error %s" % e)
    sys.exit(1)

finally:
    if con:
        con.close()