from Casificacion import Clasificacion
from Equipos import Equipos
from InfoEquipos import infoequipos


def impClasificacion(datos):
    """
    Genera la clasificación final de la liga y la imprime
    por pantalla.
    """
    equipos = Equipos(datos)
    info = infoequipos(datos, equipos)
    clasif = Clasificacion(info)

    print(f"{'Pos':<4}{'Equipo':<20}{'G':<4}{'E':<4}{'P':<4}{'Pts':<5}")
    print("-" * 45)

    for i, equipo in enumerate(clasif, start=1):
        nombre, g, e, p, pts = equipo
        print(f"{i:<4}{nombre:<20}{g:<4}{e:<4}{p:<4}{pts:<5}")
