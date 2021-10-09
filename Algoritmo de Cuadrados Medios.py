# Author: Arturo Salas Hernández - Algoritmo de Cuadrados Medios - Simulación - 08 de octubre de 2021

x0 = input("Digite el valor de la semilla inicial (x0): ")
iteraciones = int(input("Digite el numero de iteraciones a realizar: "))
cant_digitos = len(x0)

print("Cantidad de digitos:", cant_digitos)
x0 = int(x0)

for i in range(iteraciones):
	y0 = x0 ** 2
	temp = str(y0)
	sec_numeros = len(temp)
	rango = int((sec_numeros - cant_digitos) / 2)

	xi = temp[rango:rango + cant_digitos]
	print("Y{} = ({})^2 \t X{} = {} \t r{} = 0.{}".format(i, x0, i + 1, xi, i + 1, xi))
	x0 = int(xi)