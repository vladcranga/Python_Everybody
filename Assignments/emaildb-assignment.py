import sqlite3
from re import findall

# connect to the database
conn = sqlite3.connect('../Databases/email-assignment.sqlite')
cur = conn.cursor()

# run initial table queries
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# read and analyse file data
fname = input('Enter file name: ')
fhand = open(fname)

for line in fhand:
    if not line.startswith('From: '):
        continue
    line = line.strip()
    domain = findall('@([^ ]*)', line)
    cur.execute('SELECT count from Counts WHERE org = ? ', (domain[0],))

    # insert data into the database
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain[0],))
    else:
        cur.execute('UPDATE Counts set count = count + 1 WHERE org = ?',
                    (domain[0],))

# write to disk outside the loop for improved speed
conn.commit()

display_query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5'
for row in cur.execute(display_query):
    print(row[0], row[1])

cur.close()
