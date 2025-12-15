
def quiengana(resultado):
    goles_local, goles_visitante = map(int,resultado.split("-"))

    if goles_local > goles_visitante:
        return 1
    elif goles_local < goles_visitante:
        return -1
    else:
        return 0

def puntos(info):
    ganados, empatados, perdidos = info

    return ganados * 3 + empatados * 1

def infoequipos(datosliga, equipos):

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