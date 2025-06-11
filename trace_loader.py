# Cargador y visualización de referencias

def cargar_traza(path):
    referencias = []
    with open(path, 'r') as archivo:
        for linea in archivo:
            if linea.strip():
                partes = linea.strip().split()
                if len(partes) == 2:
                    direccion_hex, op = partes
                    try:
                        direccion = int(direccion_hex, 16)
                    except ValueError:
                        continue
                    if op in ['R', 'W']:
                        referencias.append((op, direccion))
    return referencias
