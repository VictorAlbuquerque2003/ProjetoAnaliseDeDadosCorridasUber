import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="db_ncr_ride_bookings",
    user="postgres",
    password="12345678"
)

cursor = conn.cursor()