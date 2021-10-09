# Author: Arturo Salas Hernández - Algoritmo Congruencial Lineal - Simulación - 08 de octubre de 2021

num_repetidos = []
def congruencial_lineal(x, a, c, m, cont):
	if x in num_repetidos:
		return num_repetidos
	else:
		cont += 1
		temp = (a * x + c) % m
		intervalo = round(temp / (m - 1), 3)
		print("x{} = ({}*{}+{}) mod {} = {}; r{} = {}".format(cont, a, x, c, m, temp, cont, intervalo))
		num_repetidos.append(x)
		return congruencial_lineal(temp, a, c, m, cont)

x = int(input("Digite el valor de la semilla inicial (x0): "))
a = int(input("Digite el valor de la constante multiplicativa (a): "))
c = int(input("Digite el valor de la constante aditiva (c): "))
m = int(input("Digite el valor del modulo (m): "))

periodo_vida = congruencial_lineal(x, a, c, m, 0) # El ultimo parametro es el contador de iteraciones
print("\n\tPeriodo Completo" if len(periodo_vida) == m else "Periodo Incompleto")