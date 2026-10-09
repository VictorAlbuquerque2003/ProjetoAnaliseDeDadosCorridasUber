import pandas as pd
from sqlalchemy import create_engine, text

conn = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/db_ncr_ride_bookings")

SQL_QUERY = pd.read_sql_query('SELECT * FROM ncr_ride_bookings_raw', conn)

df_completo = pd.DataFrame(SQL_QUERY)

# Removendo ID's duplicados de Bookings
df_sem_duplicidades = df_completo.drop_duplicates(subset='Booking_ID')

# Criando uma nova tabela no SQL contendo os dados já removidos de duplicidades
df_sem_duplicidades.to_sql(
    "ncr_ride_bookings",
    conn,
    if_exists="append",
    index=False
)