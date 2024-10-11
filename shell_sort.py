# shell_sort.py

def shell_sort(arr, ascending=True, callback=None):
    n = len(arr)
    gap = n // 2  # Brecha inicial

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Condición para ordenar ascendente o descendente
            if ascending:
                comparison = lambda a, b: a > b
            else:
                comparison = lambda a, b: a < b

            # Comparación y proceso del Shell Sort
            while j >= gap and comparison(arr[j - gap], temp):
                arr[j] = arr[j - gap]
                j -= gap

                # Callback para actualizar la interfaz después de cada iteración
                if callback:
                    callback(arr, i, j, gap, temp)

            arr[j] = temp

            # Callback después de mover el elemento final
            if callback:
                callback(arr, i, j, gap, temp)

        gap //= 2  # Reducimos la brecha

    return arr