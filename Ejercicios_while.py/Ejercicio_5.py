"""
Una actividad recibe ternas de capital C, tasa anual I y cantidad entera de años M. Una terna solo
se acepta si C es no negativo, 0 < I < 100 y M es positivo. Las ternas inválidas se descartan y se recibe
otra completa; el flujo garantiza una terna válida. Para la primera terna válida, muestre el saldo al
terminar cada año y el saldo final. Los intereses se incorporan al saldo una vez por año. La tasa I se
ingresa como porcentaje. Cada interés anual es el saldo anterior multiplicado por I y dividido entre 100;
el nuevo saldo es el saldo anterior más ese interés. Capital y saldos se expresan en una misma unidad
monetaria

Fórmula o relación: Saldo inicial = C. Saldo del año siguiente = saldo anterior x (1 + I / 100)

"""
while True:
    c = float(input("capital"))
    i = float(input("tasa anual "))
    m = int(input(" cantidad años"))
    if c > 0 and 0 < i < 100 and m > 0:
        break

saldo = c
año = 1
while año <= m:
    saldo * (1 + i/100)
    print(f"año {año}: {saldo}")
    año = año + 1

print(f"saldo final:{saldo}")

