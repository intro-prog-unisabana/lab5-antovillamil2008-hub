
def promedio_estudiante(notas):
    if len(notas)==0:
        return 0.0
    promedio=sum(notas)/len(notas)
    return float(promedio)
print(promedio_estudiante([85, 92, 78]))

