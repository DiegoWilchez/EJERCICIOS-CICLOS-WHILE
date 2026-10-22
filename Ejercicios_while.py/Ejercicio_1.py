"""
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores»

Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.

"""
a = int(input(" escriba A"))
b = int(input(" escriba B"))

i = a + 1
if i >= b: 
    print("no hay enteros interiores")
else:
    print("")