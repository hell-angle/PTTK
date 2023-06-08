import sqlite3

# Create a connection to the database file
conn = sqlite3.connect('movie_database.db')
cursor = conn.cursor()

# Insert a movie into the MOVIE table without specifying Movie_ID
cursor.execute('''
    INSERT INTO MOVIE (Title, Release_Date, Duration, Genre, Director, Cast, Showtime_ID)
    VALUES ('Movie 3', '2023-06-01', 120, 'Action', 'Director 1', 'Actor 1, Actor 2', 1)
''')

# Insert another movie into the MOVIE table without specifying Movie_ID
cursor.execute('''
    INSERT INTO MOVIE (Title, Release_Date, Duration, Genre, Director, Cast, Showtime_ID)
    VALUES ('Movie 4', '2023-06-02', 110, 'Drama', 'Director 2', 'Actor 3, Actor 4', 2)
''')
# Insert a movie into the MOVIE table without specifying Movie_ID
cursor.execute('''
    INSERT INTO MOVIE (Title, Release_Date, Duration, Genre, Director, Cast, Showtime_ID)
    VALUES ('Movie 5', '2023-06-01', 120, 'Action', 'Director 1', 'Actor 1, Actor 2', 1)
''')

# Insert another movie into the MOVIE table without specifying Movie_ID
cursor.execute('''
    INSERT INTO MOVIE (Title, Release_Date, Duration, Genre, Director, Cast, Showtime_ID)
    VALUES ('Movie 6', '2023-06-02', 110, 'Drama', 'Director 2', 'Actor 3, Actor 4', 2)
''')
# Commit the changes and close the connection
conn.commit()
conn.close()

