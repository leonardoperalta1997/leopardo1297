#3.	Crea un programa en donde se consulte la cantidad de horas trabajadas en una semana. 
#El valor de la hora trabajada vale 14.00 $ y se deberá calcular el sueldo bruto 
#(horas trabajadas x valor de hora trabajada) y luego se deberá saber el sueldo neto, 
#el cual es un descuento del 9% por impuestos. 

input("Bienvenido rufian ( ͡° ͜ʖ ͡°)")

def calcular_sueldo(horas_trabajadas, valor_hora):
    sueldo_bruto = horas_trabajadas * valor_hora
    impuestos = sueldo_bruto * 0.09
    sueldo_neto = sueldo_bruto - impuestos
    return sueldo_bruto, sueldo_neto

horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas en una semana: "))
valor_hora = 14.00

sueldo_bruto, sueldo_neto = calcular_sueldo(horas_trabajadas, valor_hora)

print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Sueldo neto: ${sueldo_neto:.2f}")


