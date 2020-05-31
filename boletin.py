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

    i = 0
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

def cargar_puestos_atendidos(puestos:list,facultad) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes atendidos
    por una facultad en especifico
    """  
    oferentes = 11
    ocupantes = 12
    for i in range(0,oferentes +1 ):
        if (puestos[i][0]==facultad):
            total = 0
            for j in range(1,ocupantes+1):
                total += int(puestos[i][j])
            return total
    return -1        
       
def cargar_puestos_ocupados(puestos:list,facultad) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes ocupados
    por una facultad en especifico
    """ 
    oferentes = 11
    for i in range(0,oferentes+1):
        if (puestos[i][0]==facultad):
            total = 0
            
            for j in range (1,oferentes+1):
                total+= int(puestos[j][i])
            return total 
    return -1 
def cargar_facultad_mas_servicial(puestos:list) -> None:
    """ Ejecuta la opcion de consultar la facultad mas servicial
    """
    oferentes = 11
    ocupantes = 12
    Nombre = ""
    Mayor = 0
    for i in range(1,oferentes +1 ):
        total = 0
        for j in range(1,ocupantes+1):
                total += int(puestos[i][j])
        
        otras_facultades = total - int(puestos[i][i])
        porcentaje = (otras_facultades/total)*100
        print (puestos[i][0]+" " + str(otras_facultades) + "/"+str(total)+" = "+str(porcentaje))
        if porcentaje>Mayor:
            Mayor = porcentaje
            Nombre = puestos[i][0]
    Mayor = round(Mayor,2)        
    return (Nombre,Mayor)        
def cargar_hay_facultad_generosa(puestos:list,facultad, porcentaje) -> None:
    """ Ejecuta la opcion de consultar si existe una facultad generosa
    para una facultad en especifico
    """
    oferentes = 11
    Nombre = "" 
    Mayor = 0
    porcentaje = porcentaje/100   
    for i in range(0,oferentes + 1 ):
        if (puestos[i][0]==facultad):
            Mayor = int(puestos[i][i])*porcentaje
            total = 0                    
            for j  in range(1,oferentes + 1):
                 total += int(puestos[j][i])         
                 if (int(puestos[j][i])> Mayor and int(puestos[j][i]) != int (puestos[i][i])):
                     Mayor = int(puestos[j][i])
                     Nombre = puestos[j][0]
            if(Mayor == 0):
                return ("No existe facultad generosa", 0)
            else:
                Mayor = (Mayor/total)*100
                Mayor = round (Mayor,2)
                return (Nombre,Mayor)
def cargar_calcular_autocubrimiento(puestos:list, estadisticas:list) -> None:
    """ Ejecuta la opcion de calcular el autocubrimiento para todas
    las facultades
    """
    oferentes = 11
    auxiliar_estadisticas = estadisticas
    auxiliar_estadisticas[0].append("autocubrimiento")    
    for i in range (1,oferentes+1):
        ofrecidos = cargar_puestos_atendidos(puestos,puestos[i][0])
        ocupados = cargar_puestos_ocupados(puestos,puestos[i][0])
        autocubrimiemto = (ofrecidos/ocupados)*100
        autocubrimiemto = round(autocubrimiemto,2)
        auxiliar_estadisticas[i].append(float(autocubrimiemto))
    return auxiliar_estadisticas    
            
def cargar_doble_mas_comun(dobles:list) -> None: 
    """ Ejecuta la opcion de consultar el doble programa mas comun
    """
    facultades_x = 35
    facultades_y = 35
    Mayor_doble = 0
    Nombre_1 = ""
    Nombre_2 = ""
    for i in  range (1,facultades_y+1):
        Mayor = 0 
        for j in range(1,facultades_x+1):
            if int(Mayor) < int(dobles[i][j]):
                    Mayor = dobles[i][j]
                    Indice = j
        Mayor = int(Mayor) + int (dobles[Indice][i])
        if Mayor > Mayor_doble:
           Mayor_doble = Mayor
           Nombre_1 = dobles[i][0]
           Nombre_2 = dobles[0][Indice]
    cadena = Nombre_1 + "-"+ Nombre_2        
    return (cadena,Mayor_doble)               
        
def cargar_dobles_de_un_programa(dobles:list,programa) -> None:
    """ Ejecuta la opcion de consultar todos los dobles programas
    de una facultad de su interes
    """
    
    facultades_x = 35
    facultades_y = 35
    dicionario = {}
    for i in range (1,facultades_y +1 ):
        if dobles[i][0] == programa:
            for j in range(1,facultades_x + 1 ):
                if not dobles[0][j] == programa:
                    lib = {dobles[0][j]:float(dobles[i][j])}
                    dicionario.update(lib)
    return dicionario                
def cargar_estadisticas_pga(estadisticas:list):
    """ Ejecuta la opcion de consultar la facultad con mayor pga, con
    menor pga y la que ocupa la mediana
    """    
    facultades = 11
   
    Mayor = 0
    Menor =  101
    Igual = 0
    Nombre_Menor = ""
    Nombre_Mayor = ""
    Nombre_Igual = "No se encontro"
    PGA_mediana =float (estadisticas[7][6])
     
    print(PGA_mediana)
    mediana = round (PGA_mediana,2)
    print(mediana)
    for i in range (1,facultades+1):
        if float (estadisticas[i][6]) > Mayor:
            Mayor = float (estadisticas[i][6])
            Nombre_Mayor = estadisticas[i][0]
        if float (estadisticas[i][6]) < Menor:
            Menor = float (estadisticas[i][6])
            Nombre_Menor = estadisticas[i][0]
        if float (estadisticas[i][6]) == mediana:
            Igual = float(estadisticas[i][6])
            Nombre_Igual = estadisticas[i][0]
            
    dicionario = list()
    dicionario.append((Nombre_Mayor,Mayor))   
    dicionario.append((Nombre_Menor,Menor))    
    dicionario.append((Nombre_Igual,Igual))  
    return dicionario        

def cargar_hay_facultad_con_porcentaje_estudiantes(estadisticas:list,sexo,porcentaje):
    facultades = 11
    if (sexo == "m" or sexo == "hombre"  ):
        indice_sexo = 3
    elif(sexo == "f" or sexo == "mujer"):
        indice_sexo = 4
    for i in range (1,facultades +1 ):
        total = float (estadisticas[i][3]) + float (estadisticas[i][4])
        
        porcentaje_estudiantes = (float(estadisticas[i][indice_sexo])/total)*100
        porcentaje_estudiantes = round(porcentaje_estudiantes,2)
        if (porcentaje<porcentaje_estudiantes):
            return (True,estadisticas[i][0],porcentaje_estudiantes)
    return (False,0,0)    

    """ Ejecuta la opcion de consultar si existe una facultad con un 
    porcentaje de estudiantes por genero mayor al requerido
    """      
    
"""print (cargar_puestos_atendidos(cargar_matriz_puestos("matriz_puestos.csv"),"Medicina"))    
      
print (cargar_puestos_ocupados(cargar_matriz_puestos("matriz_puestos.csv"),"Ingenieria"))
print(cargar_facultad_mas_servicial(cargar_matriz_puestos("matriz_puestos.csv"))) 
print (cargar_hay_facultad_generosa(cargar_matriz_puestos("matriz_puestos.csv"),"Medicina",5))
print (cargar_calcular_autocubrimiento(cargar_matriz_puestos("matriz_puestos.csv"),cargar_matriz_estadisticas("estadisticas_facultades.csv") ))
print(cargar_doble_mas_comun(cargar_matriz_dobles("matriz_dobles.csv")))
print(cargar_dobles_de_un_programa(cargar_matriz_dobles("matriz_dobles.csv"),"Geociencias"))
print(cargar_estadisticas_pga(cargar_matriz_estadisticas("estadisticas_facultades.csv")))
print(cargar_hay_facultad_con_porcentaje_estudiantes(cargar_matriz_estadisticas("estadisticas_facultades.csv"),"f",60))"""