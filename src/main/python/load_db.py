import psycopg2
from psycopg2.extras import execute_batch


def get_db_connection(db_name,user,password,host,port):
    try:
        connection = psycopg2.connect(dbname=db_name,
                                      user=user,
                                      password = password,
                                      host=host,
                                      port = port)
    except psycopg2.DatabaseError as e:
        print(f"Connection Error: {e}")
    return connection


if __name__=="__main__":
    connection = get_db_connection(db_name="tixito",
                                   user="postgres",
                                   password="root",
                                   host="localhost",
                                   port="5432")
    
    if connection:
        print("Connection Successful")
        cursor = connection.cursor()
        insert_query = "INSERT INTO events(EventID,EventName,EventDateTime,EventLocation) VALUES (%s, %s, %s, %s);"
        data_to_insert = (1,"Taylor Swift - The Life of a Showgirl", "2026-01-30 20:30:00-05","New York")
        cursor.execute(insert_query,data_to_insert)
        print("Inserted First Event into Events table")
        # Inserting Seats 
        insert_query_seat = "INSERT INTO seats (SeatIdentifier,EventID,status) VALUES (%s,%s,%s)" 
        seats = []
        for i in range(1,101,1):
            seats.append((i,1,'AVAILABLE'))
        psycopg2.extras.execute_batch(cursor,insert_query_seat,seats)

        connection.commit()
        print("Sucessfully Inserted 100 seats for Event")
        print(f"{cursor.rowcount} were inserted.")
        
        connection.close()
    else:
        print("Connection failed")


