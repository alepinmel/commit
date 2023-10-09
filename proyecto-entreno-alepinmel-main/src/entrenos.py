from collections import namedtuple
from datetime import datetime
import csv

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_fichero(ruta):
    res = []
    with open(ruta, encoding = "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for linea in lector:
            tipo = linea[0]
            fechahora = datetime.strptime(linea[1], "%d/%m/%Y %H:%M")
            ubicacion = linea[2]
            duracion = int(linea[3])
            calorias = int(linea[4])
            distancia = float(linea[5])
            frecuencia = int(linea[6])
            compartido = linea[7] == "S"
            tupla = Entreno(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido)
            res.append(tupla)
        return res