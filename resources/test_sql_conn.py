import pymysql

# Define your connection parameters
connection_params = {
    'host': '',
    'user': 'webapp',
    'password': '',
    'database': 'webapp',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Connect to the database
try:
    connection = pymysql.connect(**connection_params)

    # Create a cursor object
    with connection.cursor() as cursor:
        # SQL query to select all contents from the users table
        sql = "SELECT * FROM user"

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of dictionaries
        results = cursor.fetchall()

        # Iterate through the result and print each row
        for row in results:
            print(row)

except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
    # Make sure to close the connection
    if connection:
        connection.close()
