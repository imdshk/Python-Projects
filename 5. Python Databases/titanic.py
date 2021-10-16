import sqlite3
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

conn = sqlite3.connect("titanic.db")
cursor = conn.cursor()

# df.to_sql("titanic", conn)

first_five = cursor.execute('''SELECT * FROM titanic;''').fetchmany(5)
fifties = cursor.execute('''SELECT * FROM titanic WHERE Age = 50.0;''').fetchall()
femme = cursor.execute('''SELECT COUNT(PassengerID) FROM titanic WHERE Sex = 'female';''').fetchone()

new_df = pd.read_sql_query('''SELECT * FROM titanic;''', conn)
print(new_df)