#declarar una lista unidimensional de frutas

frutas = ["Pera", "Manzana","Uva","Fresa"]

print(frutas)

#append
frutas.append("Melón")

print(frutas)

#acceder a elemento

print(frutas[4])

frutas[4] = "Arandano"

print(frutas[4])

# Ordenar una lista

digitos = [5,2,3,9,8,4,7,0,6]
print(digitos)

digitos.sort()
print(digitos)

digitosCero = 5*[0]
print(digitosCero)

#Tamaño de la lista

print("Cantidad de frutas ingresadas: ", len(frutas))