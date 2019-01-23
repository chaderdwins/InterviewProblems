import sqlite3
conn = sqlite3.connect("friends.db")

#creating cursor
c = conn.cursor()
#executing SQL code
#c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

form_first = "chad"
form_last = "erdwins"
form_age = 10
data = ("Steve", "Irwin", 9)
people = [
    ("Sara","Erdwins",10),
    ("Sonny","Erdwins",10),
    ("Brenda","Erdwins",10),
    ("Shannon","Erdwins",10),
    ("Trey","Suarez",7)
]
people2 = [
    ("Bonnie","Erdwins",10),
    ("Duke","Erdwins",10),
    ("Clyde","Erdwins",10),
    ("Sofi","Erdwins",10),
    ("Chicken","Suarez",7)
]
#f-string uses ? to sanitize the variable in case of injection
query = "INSERT INTO friends (first_name, last_name, closeness) VALUES (?,?,?)"
#have to pass in a tuple as the second param bc it needs an iterable
# c.execute(query, (form_first,form_last,form_age))
# c.execute(query, data)
# c.executemany(query, people)
# for person in people2:
#     c.execute(query, person)
c.execute("SELECT * FROM friends")
# for result in c:
#     print(result)
li = c.fetchall()
print(li)
#commit the executed code to the db
conn.commit()

#closing the db connection
conn.close()
