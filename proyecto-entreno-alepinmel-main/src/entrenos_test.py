from entrenos import *

def test_lee_entrenos():
    print("Test de la funcion de lectura: lee_entrenos")
    lista_entrenos = lee_fichero("proyecto-entreno-alepinmel-main\data\entrenos.csv")
    print(f"Se han leido {len(lista_entrenos)} registros")
    print("Mostrando los 3 primeros")
    print(lista_entrenos[:3])
    print("Mostrando los 3 ultimos")
    print(lista_entrenos[-3:])

if __name__ == "__main__":
    test_lee_entrenos()