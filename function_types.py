def list_shift(lista, valor):
    """Suma un valor a cada elemento."""
    for i in range(len(lista)):
        lista[i] += valor
def calc_avg(lista):
    """Calcula el promedio de la lista de flotantes."""
    promedio = sum(lista) / len(lista)
    return promedio
def print_normalized(lista):
    """Imprime la lista de flotantes"""
    print(lista)



if __name__ == "__main__":
    datos = [2.0, 4.0, 6.0, 8.0]
    prom = calc_avg(datos)    
    list_shift(datos, -prom)       
    print_normalized(datos)        