# def calculator(a:int, b:int):
#     def main():
#         print("Setting")
#     def plus():
#         return a + b
    
#     main.plus = plus
#     return main

# calc = calculator(5, 10)

# print(calc.plus()) 
# import psycopg2
# def db():
#     database='fn22',
#     user='postgres',
#     password='fn2223',
#     host='localhost',
#     port=5432

#     def main():
#         print("Setting")

#     def connect():
#         conn=psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)
#         conn.autocommit=True
#     main.connect=connect
#     return main

# Db=db()
# print(Db.connect())

# import psycopg2

# def db():
#     database = 'fn22'
#     user = 'postgres'
#     password = 'fn2223'
#     host = 'localhost'
#     port = 5432

#     class Main:
#         def __init__(self):
#             self.conn = None

#         def connect(self):
#             try:
#                 self.conn = psycopg2.connect(dbname=database, user=user, password=password, host=host, port=port)
#                 self.conn.autocommit = True
#                 print("Connection established")
#             except Exception as e:
#                 print(f"Unable to connect: {e}")

#     return Main()

# Db = db()
# Db.connect()

from dataclasses import dataclass

@dataclass
class User:
    id:int
    first_name:str

    