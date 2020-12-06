import threading
import pymongo
import random
import time
import datetime
from bson.objectid import ObjectId
from threading import Thread,Semaphore

#Funcion Añadir
def add(ver):
	global semaforo
	#Bloqueamos el semaforo
	semaforo.acquire();
	#Control 
	print(f"Hilo {ver} modificando")
	#Actualizamos el valor
	valor=documento[0]["Cantidad"]+1
	#Actualizamos en la base de datos
	coleccion.update_one({"_id":ObjectId(ID_doc)}, {"$set": {"Cantidad": valor }})						
	#Liberamos el semaforo
	semaforo.release();
						
def añadir(ver):
	#Creamos un hilo
	hilo = threading.Thread(target=add, args=(ver,))
	#Lo iniciamos
	hilo.start()	
	#Lo añadimos al array
	threads.append(hilo)
def mostrar():
	#Bloqueamos el semaforo	
	semaforo.acquire();
	valor=documento[0]["Cantidad"]
	print(f"La cantidad es :  {valor}")
	#Liberamos el semaforo
	semaforo.release();

tiempo_ini = datetime.datetime.now()
#Variables de apoyo
Mongo_baseDatos="ForoPrueba"
Mongo_coleccion="prueba"
semaforo = Semaphore(1);

try:
	#Conexion a mongoDb(Linea Obligatoria)
	#por temas de seguridad de la base de datos no podemos poner la URI de MongoDB Atlas
	cliente = "aqui va la URI de la base de datos para la conexion ya que esta va servir para poder obtener los datos y actualizarlos"
	print("conexion exitosa")
	#Obtenemos la base de datos a trabajar
	baseDatos=cliente[Mongo_baseDatos]
	#Obtenemos la coleccion a trabajar
	coleccion=baseDatos[Mongo_coleccion]
	#Id del documento en el cual modificaremos los datos
	ID_doc="5f931b16879144ec11b4446a"
	#Creamos el Objeto ID para que mongo lo reconozca
	idBuscar={"_id":ObjectId(ID_doc)}
	#Lo buscamos, lo devuelve como un arreglo de documento		
	documento=coleccion.find(idBuscar)
	
	#Creamos los hilos
	threads = []
	
	añadir(1)
	añadir(2)
	mostrar()
	añadir(3)
	mostrar()
	añadir(4)
	mostrar()
	#Recorremos el array de hilos para hacer que el main los espere
	for hilo in threads:	        
	    # El programa esperará a que este hilo finalice:
	    hilo.join() 

#Posibles errores	
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
	print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
	print ("Fallo al conectarse a mongodb "+errorConexion)

tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido " + str(tiempo_fin.second - tiempo_ini.second))






