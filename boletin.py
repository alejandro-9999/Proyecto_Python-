# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Modulo de Funciones

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""

def cargar_matriz_estadisticas(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de estadisticas 
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """  
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = []
    for i in range(0,facultades+1):
        estadisticas.append([0]*(elementos+1))

    i = 0;
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,elementos+1):
            estadisticas[i][j] = datos[j].strip()
        i += 1 
        linea = archivo.readline()
    archivo.close()
    
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str)->list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0,oferentes+1):
        puestos.append([0] * (ocupantes+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,ocupantes+1):
            puestos[i][j] = datos[j].strip()
        i += 1 
        linea = archivo1.readline()
    archivo1.close()
    
    return puestos


#TODO Implemente las demas funciones de su programa
def cargar_matriz_dobles(ruta_archivo: str)->list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de dobles programas y la carga.
    Retorno: list
        La matriz de los dobles programas entre las carreras.
    """
    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    facultades_x = 35
    facultades_y = 35
    dobles = []
    for i in range(0,facultades_x+1):
        dobles.append([0] * (facultades_y+1))

    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0,facultades_y +1):
            dobles[i][j] = datos[j].strip()
        i += 1 
        linea = archivo2.readline()
    archivo2.close()
    
    return dobles

def cargar_puestos_atendidos(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes atendidos
    por una facultad en especifico
    """  
    
    
def cargar_puestos_ocupados(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes ocupados
    por una facultad en especifico
    """ 
def cargar_facultad_mas_servicial(puestos:list) -> None:
    """ Ejecuta la opcion de consultar la facultad mas servicial
    """
def cargar_hay_facultad_generosa(puestos:list) -> None:
    """ Ejecuta la opcion de consultar si existe una facultad generosa
    para una facultad en especifico
    """
def cargar_calcular_autocubrimiento(puestos:list, estadisticas:list) -> None:
    """ Ejecuta la opcion de calcular el autocubrimiento para todas
    las facultades
    """
def cargar_doble_mas_comun(dobles:list) -> None: 
    """ Ejecuta la opcion de consultar el doble programa mas comun
    """
def cargar_dobles_de_un_programa(dobles:list) -> None:
    """ Ejecuta la opcion de consultar todos los dobles programas
    de una facultad de su interes
    """    
def cargar_estadisticas_pga(estadisticas:list):
    """ Ejecuta la opcion de consultar la facultad con mayor pga, con
    menor pga y la que ocupa la mediana
    """    
    
def cargar_hay_facultad_con_porcentaje_estudiantes(estadisticas:list):
    """ Ejecuta la opcion de consultar si existe una facultad con un 
    porcentaje de estudiantes por genero mayor al requerido
    """      
    
    
   
    