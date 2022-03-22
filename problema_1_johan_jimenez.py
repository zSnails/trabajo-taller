fecha1 = 19282512#int(input("Ingrese la primera fecha: "))
fecha2 = 20031628#int(input("Ingrese la segunda fecha: "))
ano_fech1 = fecha1//10000
ano_fech2 = fecha2//10000
dia_fecha1 = fecha1%100 
dia_fecha2 = fecha2%100

i = 0

while i < 3:
    mes_fech1 = fecha1%10
    mes_fech2 = fecha2%10
    fecha1 = (fecha1-mes_fech1)//10
    fecha2 = (fecha2-mes_fech2)//10
    i = i+1
if (mes_fech1 < mes_fech2):
    anofinal = ano_fech2-ano_fech1
else:
    anofinal = (ano_fech2-ano_fech1)-1
if (mes_fech1 > mes_fech2):
    mesfinal = (mes_fech2+12)-mes_fech1
elif (mes_fech1 == mes_fech2):
    mesfinal = 0
else: 
    mesfinal = (mes_fech1+12)-mes_fech2
if (dia_fecha1 > dia_fecha2):
    diafinal = dia_fecha1-dia_fecha2
else:
    diafinal = dia_fecha2-dia_fecha1
fechafinal = ((anofinal*100)+mesfinal)
fechafinal = (fechafinal*100)+diafinal
print(fechafinal)
