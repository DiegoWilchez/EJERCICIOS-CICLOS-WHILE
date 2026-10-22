"""
Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad

Fórmula o relación: Promedio = suma de las notas / cantidad de notas, solo cuando la cantidad sea


"""
suma = 0
cantidad = 0
nota = float(input("nota"))
while nota != -99:
    suma += nota
    cantidad += 1
    nota = float(input("nota"))
if cantidad > 0:
    print(f"cantidad: {cantidad}; promedio {suma/cantidad}")
else:
    print("cantidad: 0; sin notas")