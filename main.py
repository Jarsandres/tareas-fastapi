
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

"""
****Tarea***

* Creación de API de ejemplo
* Implementación en fast api
* Despliegue api manager prueba y creación ciclo de vida de la API creada.

"""

app = FastAPI()

"""
Clase de nuestro recurso Libro. Validará nuestro modelos de datos. 

"""
class Libro(BaseModel) :
    #Atributos
    titulo : str
    autor : str
    paginas : int
    editorial : str


#Simulación de una base de datos en memoria

libros_db = {
    1: Libro(titulo="Cien años de soledad", autor="Gabriel Garcia Marquez", paginas=471 ,editorial="Sudamericana"),
    2: Libro(titulo="La conjura de los necios", autor="John Kennedy Toole", paginas=389 ,editorial="Anagrama")
}

#Función que establecerá el get, mostrando mensaje
@app.get("/")
def mensaje() :
    return {"mensaje": "Hola estoy aprediendo a desarrolar APIS"}

#Función que solicitará los libros por id

@app.get("/libros/{id_libro}")
def mostrar_librosID (id_libro : int):
    if id_libro in libros_db :
        return libros_db[id_libro]
    else:
        raise HTTPException (status_code= 404, detail= "Libro no encontrado")

@app.get("/libros")
def librosLista ():
    return libros_db

#Función que establecerá el post, mostrando mensaje si se introdujo correctamente
@app.post("/libros")
def insertar_libro (libro : Libro) :
    if libros_db:
        nuevo_id = max(libros_db.keys())+1
    else:
        nuevo_id = 1
    libros_db[nuevo_id] = libro
    return {"mensaje": f"libro {libro.titulo} insertado correctamente"}

