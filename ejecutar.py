# Importacion de archivos
from services.extracion import fun_extraccion
from services.trasformacion import fun_trasformacion, fun_generarArchivo
from modelo.model_loader import loader_file_sqlite

# URL correcta (usa forecast_days)
URL = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&hourly=temperature_2m,precipitation&forecast_days=3"

def main():
    raw = fun_extraccion(URL)

    if not raw:
        print("Error al extraer datos")
        return

    #print("Datos obtenidos correctamente")
    #print(raw["hourly"]["time"][:5])  #Carga datos desde la fuente

    stg_clear = fun_trasformacion(raw)

    print("Datos trasformados")
    #print(stg_clear)
    #print(stg_clear)

    #Generar archivo csv y guardo

    fun_generarArchivo(
        stg_clear,
        carpeta="reportes",
        nameFile="datos_clima_cdmx.csv"
    )

    #Carga - Loader a SQL
    #crear_tabla()
    loader_file_sqlite("reportes/datos_clima_cdmx.csv")

if __name__ == "__main__":
    main()
