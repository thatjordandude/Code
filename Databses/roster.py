import json
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

# Create the User, Course, and Member tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Read the roster_data.json file
filename = input('Enter file name: ')
if len(filename) < 1:
    filename = 'roster_data.json'

data = open(filename).read()

# Parse the JSON data
json_data = json.loads(data)

# Loop through the data and insert it into the tables
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert the user into the User table
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert the course into the Course table
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert the user and course into the Member table
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)''', (user_id, course_id, role))

    # Commit the changes to the database
    conn.commit()

# Run the given SQL queries
sqlstr = '''
SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
'''
for row in cur.execute(sqlstr):
    print(str(row[0]), str(row[1]), str(row[2]))

sqlstr = '''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1
'''
for row in cur.execute(sqlstr):
    print(str(row[0]))

cur.close()
