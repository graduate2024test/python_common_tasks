# Написать функцию, которая переводит структуру всех
# таблиц существующей базы данных, в формат Json.

import sqlite3
import json
import collections

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

#cursor.execute("SELECT * FROM demo")
#results = cursor.fetchall()

#cursor.execute("DELETE FROM demo")
#results = cursor.fetchall()
#print(results)

cursor.execute("SELECT * FROM demo")
rows = cursor.fetchall()

rowarray_list = []
for row in rows:
    t = (row[0], row[1], row[2])
    rowarray_list.append(t)

j = json.dumps(rowarray_list)

with open("demo_rowarrays.js", "w") as f:
    f.write(j)

# Convert query to objects of key-value pairs
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["Name"] = row[1]
    d["Hint"] = row[2]
    objects_list.append(d)

j = json.dumps(objects_list)


with open("demo_rowarrays.js", "w") as f:
    f.write(j)

conn.close()
