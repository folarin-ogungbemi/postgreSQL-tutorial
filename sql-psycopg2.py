import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# # Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# # Query 2 - Select only name from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# # Query 3 - Select 'Queen' from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# # Query 4 - Select 'ArtistId' from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# # Query 5 - Select only the "Albums" with 'ArtistId' #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen"
# from the "Track" table.
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# # fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
