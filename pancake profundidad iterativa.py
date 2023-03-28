def juego_de_panqueques(estado_inicial, estado_objetivo):
    def voltear_pancakes(pancakes, i):
        return pancakes[:i+1][::-1] + pancakes[i+1:]

    def dfs(pancakes, profundidad, path):
        if profundidad == 0:
            return None
        if pancakes == estado_objetivo:
            return path

        for i in range(len(pancakes)):
            nuevas_pancakes = voltear_pancakes(pancakes, i)
            resultado = dfs(nuevas_pancakes, profundidad-1, path + [i])
            if resultado:
                return resultado

    # Búsqueda iterativa en profundidad
    for profundidad in range(1, 11):
        # Llamada a la función dfs con profundidad máxima `profundidad`
        resultado = dfs(estado_inicial, profundidad, [])
        if resultado:
            # Construir y devolver la lista de movimientos
            movimiento = []
            for i in range(len(resultado)):
                indice_volteo = resultado[i]
                estado_inicial = voltear_pancakes(estado_inicial, indice_volteo)
                movimiento.append(estado_inicial[:])
            return movimiento

    # Si no se encuentra una solución, devolver None
    return None


estado_inicial = ['d', 'b', 'c', 'a']
estado_objetivo = ['a', 'b', 'c', 'd']
movimiento = juego_de_panqueques(estado_inicial, estado_objetivo)
if movimiento:
    print("Pasos para llegar al resultado final:")
    for move in movimiento:
        print(move)
else:
    print("No se encontró una solución")
