
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
    resultados = []

    for equipo in equipos:
            resultado = [0,0,0]
            for partido in datosliga:
                golesLHT, golesVHT = map(int,partido['HT'].split("-"))
                golesLFT, golesVFT = map(int,partido['FT'].split("-"))
                golesL = golesLFT + golesLHT
                golesV = golesVFT + golesVHT
                golesFinales = str(str(golesL) + "-" + str(golesV))
                if partido["Equipo 1"]==equipo and quiengana(golesFinales)==1:
                    resultado[0]+=1
                if partido["Equipo 1"]==equipo and quiengana(golesFinales)==-1:
                    resultado[2]+=1
                if partido["Equipo 1"]==equipo and quiengana(golesFinales)==0:
                    resultado[1]+=1
                if partido["Equipo 2"]==equipo and quiengana(golesFinales)==1:
                    resultado[0]+=1
                if partido["Equipo 2"]==equipo and quiengana(golesFinales)==-1:
                    resultado[2]+=1
                if partido["Equipo 2"]==equipo and quiengana(golesFinales)==0:
                    resultado[1]+=1
            resultado.append(puntos(resultado))
            resultados.insert(0,equipo)
            resultados.append(tuple(resultado))
    return resultados