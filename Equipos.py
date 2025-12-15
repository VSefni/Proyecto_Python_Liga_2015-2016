def Equipos(datosliga):
    """
    Recibe la lista de partidos y devuelve un conjunto con todos los equipos únicos.
    """
    equipos = set()
    for partido in datosliga:
        equipos.add(partido['Equipo 1'])
        equipos.add(partido['Equipo 2'])
    return equipos