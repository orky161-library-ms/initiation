import sys

import mysql.connector
from dotenv import load_dotenv

load_dotenv()
import os

host = os.environ.get("DB_HOST")
port = int(os.environ.get("DB_PORT"))
user = os.environ.get("DB_USER")
passwd = os.environ.get("DB_PASSWORD")
dbName = os.environ.get("DB_NAME")

mydb = mysql.connector.connect(host=host, port=port, user=user, passwd=passwd, db=dbName)

with open(os.path.join(sys.path[0], dbName), "r") as f:
    query = f.read()

cursor = mydb.cursor(buffered=True)
results = cursor.execute(query, multi=True)

for cur in results:
    print('cursor:', cur)
    if cur.with_rows:
        print('result:', cur.fetchall())

mydb.commit()
mydb.close()
