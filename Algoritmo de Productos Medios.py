# Author: Arturo Salas Hernández - Algoritmo de Productos Medios - Simulación - 08 de octubre de 2021

x0 = input("Digite el valor de la primera semilla inicial (x0): ")
x1 = input("Digite el valor de la segunda semilla inicial (x1): ")
iteraciones = int(input("Digite el numero de iteraciones a realizar: "))
suma = len(x0) + len(x1)
cant_digitos = suma // 2

print("Cantidad de digitos:", cant_digitos)
x0 = int(x0)
x1 = int(x1)

for i in range(iteraciones):
	y0 = x0 * x1
	temp = str(y0)
	sec_numeros = len(temp)
	rango = int((sec_numeros - cant_digitos) / 2)

	xi = temp[rango:rango + cant_digitos]
	print("Y{} = ({}) ({}) = {}; \t X{} = {} \t r{} = 0.{}".format(i, x0, x1, y0, i + 1, xi, i + 1, xi))
	x0 = x1
	x1 = int(xi)