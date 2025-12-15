import csv

def LeerPartidos(nombre_archivo='liga.csv'):
    """
    Lee el archivo CSV de partidos y devuelve una lista de diccionarios.
    Cada diccionario representa un partido con claves: 'Fecha', 'Equipo 1', 'Equipo 2', 'FT', 'HT'.
    """
    partidos = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            partidos.append({
                'Fecha': fila['Fecha'],
                'Equipo 1': fila['Equipo 1'],
                'Equipo 2': fila['Equipo 2'],
                'FT': fila['FT'],
                'HT': fila['HT']
            })
    return partidos