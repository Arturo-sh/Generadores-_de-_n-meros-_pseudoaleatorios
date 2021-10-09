# Author: Arturo Salas Hernández - Algoritmo Congruencial Multiplicativo - Simulación - 08 de octubre de 2021

num_repetidos = []
def congruencial_multiplicativo(x, a, m, cont):
	if x in num_repetidos:
		return num_repetidos
	else:
		cont += 1
		temp = (a * x) % m
		intervalo = round(temp / (m - 1), 3)
		print("x{} = ({}*{}) mod {} = {}; \t r{} = {}".format(cont, a, x, m, temp, cont, intervalo))
		num_repetidos.append(x)
		return congruencial_multiplicativo(temp, a, m, cont)

x = int(input("Digite el valor de la semilla inicial (x0): "))
a = int(input("Digite el valor de la constante multiplicativa (a): "))
m = int(input("Digite el valor del modulo (m): "))

periodo_vida = congruencial_multiplicativo(x, a, m, 0) # El ultimo parametro es el contador de iteraciones
print("\n\tPeriodo Completo" if m // 4 == len(periodo_vida) else "Periodo Incompleto")