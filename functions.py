
def promdedio_estudiante(notas):
    if len(notas)==0:
        return 0.0
    promedio=sum(notas)/len(notas)
    return float(promedio)
print(promdedio_estudiante([85, 92, 78]))


#Corregir 