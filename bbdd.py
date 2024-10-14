
import config
import pymysql.cursors

def modificar_db(query):
    coneccion=pymysql.connect(**config.conn_params_2)
    cursor= coneccion.cursor()  
    cursor.execute(query)     
    coneccion.commit()
    return

def consultar_db(query):
    conection=pymysql.connect(**config.conn_params_2)
    cursor= conection.cursor()
    cursor.execute(query)
    Result= cursor.fetchall() 
    return Result    