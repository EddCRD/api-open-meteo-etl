import pandas as pd
import os

def fun_trasformacion(data):

	if not data or not data.get("hourly"):
		return pd.DataFrame()

	df = pd.DataFrame(data["hourly"])

	#Regla convertie el campo time a tipo datetime
	df["time"] = pd.to_datetime(df["time"])

	#Regla remombrer compos al español
	df.rename(columns={"time": "fecha","temperature_2m":"temperatura_c","precipitation":"precipitacion_mm"}, inplace=True)

	#Regla filtrar registros entre las horas 06:00 y a las 22:00
	df = df[(df["fecha"].dt.hour >= 6) & (df["fecha"].dt.hour <= 22)]

	#Regla de conteo registros  valores null o negativo en columnas precipitacion_mm y temperatura_c
	print(f"Valores Null: {(df['temperatura_c'].isna() | df['precipitacion_mm'].isna()).sum()}")
	print(f"Valores Negativos: {((df['temperatura_c'] < 0) | (df['precipitacion_mm'] < 0)).sum()}")


	#fun_generarArchivo(df)

	return  df


def fun_generarArchivo(df, carpeta="salida", nameFile="archivo.csv"):

    os.makedirs(carpeta, exist_ok=True)

    ruta = os.path.join(carpeta, nameFile)

    df.to_csv(ruta, index=False)

    print(f"Archivo guardado en: {ruta}")
