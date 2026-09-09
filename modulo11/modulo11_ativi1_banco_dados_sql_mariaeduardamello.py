import psycopg2

conn = psycopg2.connect("banco.db")
cursor = conn.cursor()

