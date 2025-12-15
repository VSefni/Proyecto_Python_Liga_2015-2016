from LeerPartidos import LeerPartidos
from Imprimir import impClasificacion

if __name__ == '__main__':
    liga = LeerPartidos()
    print(liga)
    impClasificacion(liga)