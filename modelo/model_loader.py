from bd.conn_bd import fun_connection
import pandas as pd


def loader_file_sqlite(ruta_csv):

    conn = fun_connection()

    try:
        df = pd.read_csv(ruta_csv)

        if df.empty:
            print("El CSV está vacío")
            return

        df.to_sql("clima", conn, if_exists="replace", index=False)

        print("CSV cargado a SQLite correctamente")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
