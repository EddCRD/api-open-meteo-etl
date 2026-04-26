# api-open-meteo-etl
Consumir una API REST Open-Meteo (CDMX) y construir un ETL correcto, con sentido técnico.

# ETL Clima CDMX – Open-Meteo

Pipeline ETL desarrollado en Python para extraer, transformar y cargar datos climáticos desde una API pública, almacenándolos en SQLite para su análisis.

---

# Descripción

Este proyecto consume datos de la API Open-Meteo, procesa información de temperatura y precipitación, y genera un flujo ETL completo:

- Extracción desde API (requests)
- Transformación con pandas
- Exportación a CSV
- Carga a SQLite
- Consultas SQL para análisis

---

# Arquitectura

Pipeline ETL modular:
Extract → Transform → Load → SQL

---

 # Requisitos

- Python 3.x
- pandas
- requests
- SQLite3
