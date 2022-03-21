print("Inserte el número que desea cifrar")
clave_bruto = int(input())
clave_inicial = clave_bruto
ceros = 1
suma_clave_cifrada = 0
clave_cifrada = 0
clave_de_cifrado = 0
clave_de_cifrado = clave_de_cifrado + (clave_bruto%10)
clave_bruto = clave_bruto//10
cantidad_digitos = 1

########################################################## sacar clave de cifrado
while clave_bruto > 0:
    clave_de_cifrado = clave_de_cifrado + (clave_bruto%10)
    clave_bruto = clave_bruto//10



clave_de_cifrado = clave_de_cifrado%10  #clave de cifrado#

print ("La clave de cifrado es: ")
print (clave_de_cifrado)

############################################## cifrar la clave
while clave_inicial > 0:
    suma_clave_cifrada = ((clave_inicial%10) + clave_de_cifrado)%10
    clave_inicial = clave_inicial//10
    suma_clave_cifrada = suma_clave_cifrada*ceros
    ceros = ceros*10
    clave_cifrada = clave_cifrada + suma_clave_cifrada
    cantidad_digitos = cantidad_digitos + 1



clave_cifrada = (clave_cifrada*10) + clave_de_cifrado   #####introducir el numero de cif

clave_cifrada = clave_cifrada/10 ** cantidad_digitos

print ("La clave cifrada es:" )
print (clave_cifrada)




#################################################### decifrar la clave



ceros = ceros*10
clave_cifrada = clave_cifrada * ceros
clave_de_cifrado = clave_cifrada % 10

clave_cifrada = clave_cifrada // 10

clave = 0
ceros2 = 1
clave = ((clave_cifrada % 10) + 10 - clave_de_cifrado)*ceros2 + clave
ceros2 = ceros2 * 10
clave_cifrada = clave_cifrada // 10

while clave_cifrada > 0:
    clave = ((clave_cifrada % 10) + 10 - clave_de_cifrado)*ceros2 + clave
    ceros2 = ceros2 * 10
    clave_cifrada = clave_cifrada // 10


print ("Su clave descodificada es:")
print (int(clave))
