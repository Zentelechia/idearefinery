import psycopg2
import os

def initSQL():
    global cursor
    global conn
    #establishing the connection
    conn = psycopg2.connect(
        database="defaultdb", user='avnadmin', password=os.getenv("AIVEN_PASS"), 
        host='pg-22832b80-simon-5c63.aivencloud.com', port='13197'
    )

    #Setting auto commit false
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

def getData(request):
    #Retrieving data
    cursor.execute(request)

    #Fetching 1st row from the table
    #result = cursor.fetchone();
    #print(result)

    #Fetching all from the table
    result = cursor.fetchall()
    # print(result)
    return result

def close():
    #Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()