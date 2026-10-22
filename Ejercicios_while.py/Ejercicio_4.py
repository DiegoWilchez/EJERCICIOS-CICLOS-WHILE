"""
Una nómina ficticia recibe primero el salario mensual de un trabajador. Cero termina el registro y
no requiere otros datos. Un salario mensual positivo se acompaña de días trabajados, entero de 0 a 30,
bonos no negativos y otras deducciones no negativas. Muestre el pago neto de cada trabajador, en
orden de lectura. La retención es 5 % y el aporte de seguridad es 12 % del devengado. Se garantiza que
las otras deducciones no superan el devengado después de esos descuentos 


El flujo termina con salario mensual cero. El salario proporcional corresponde al salario mensual multiplicado por los días
trabajados y dividido entre 30. El devengado es ese salario proporcional más los bonos. Tanto la
retención como el aporte se calculan sobre ese mismo devengado: se descuentan en total 17 %, queda
el 83 % y después se restan las otras deducciones. Todos los importes usan la misma unidad monetaria 
Sin trabajadores, informe «Sin trabajadores»

Fórmula o relación: Salario proporcional = mensual x días / 30. Devengado = salario proporcional +
bonos. Neto = devengado x 0,83 - otras deducciones


"""
trabajadores = 0

while True:
    salario = float(input("Salario mensual "))
    if salario == 0:
        break

    dias = int(input("Días trabajados "))
    bonos = float(input("Bonos "))
    otras = float(input("Otras deducciones "))

    devengado = salario * dias / 30 + bonos
    neto = devengado * 0.83 - otras
    print(f"Neto: {neto}")
    trabajadores = trabajadores + 1

if trabajadores == 0:
    print("Sin trabajadores")