
def quiengana(resultado):
    """
    Funcion que devuelve 1 -1 o 0 dependiendo del resultado del partido que se introduzca
    :param resultado: el resultado del partido
    :return: 1, -1 o 0 segun el resultado
    """
    goles_local, goles_visitante = map(int,resultado.split("-"))

    if goles_local > goles_visitante:
        return 1
    elif goles_local < goles_visitante:
        return -1
    else:
        return 0

def puntos(info):
    """
    Funcion que calcula la puntuacion de un equipo despues de que se le haya pasado los resultados del mismo
    :param info: las estadisticas del equipo
    :return: la puntuacion final del equipo
    """
    ganados, empatados, perdidos = info

    return ganados * 3 + empatados * 1

def infoequipos(datosliga, equipos):
    """
    Funcion que recopila toda las estadisticas e informacion del equipo y las devuelve como una lista
    :param datosliga: los resultados de todos los partidos de la liga
    :param equipos: el listado de equipos de la liga
    :return: un listado de equipos de la liga con sus resultados organizados
    """
    estadisticas = {}

    for equipo in equipos:
        estadisticas[equipo] = {
            'ganados': 0,
            'empatados': 0,
            'perdidos': 0
        }

        if quiengana(datosliga) == 1:
            estadisticas[equipo]['ganados']+=1
        elif quiengana(datosliga) == -1:
            estadisticas[equipo]['perdidos'] += 1
        else:
            estadisticas[equipo]['perdidos'] += 1

        puntuacion = puntos(estadisticas[equipo])

        estadisticas[equipo]['puntos'] = puntuacion
    return estadisticas