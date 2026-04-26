import requests

def fun_extraccion(url):
 try:

  response = requests.get(url,timeout=(3, 5))

  #Validamos conexion exitosa 200 a http
  if response.status_code == 200:
     print("Conexión exitoso: 200")

     response.raise_for_status() #metodo de la libreria request validamos el error de http

     dataJson = response.json() #la API la pasamos a un diccionario de python

   #print(dataJson) # con este print se valida que el json trae informaciòn solo descomentar

     return dataJson

 except requests.exceptions.HTTPError as e:
  print(f"Error HTTP: {e}")
 except requests.exceptions.Timeout:
  print(f"Timeout tiempo excedido en respuesta")
 except requests.exceptions.RequestException as e:
  print("Error en API:", e)
  return None
