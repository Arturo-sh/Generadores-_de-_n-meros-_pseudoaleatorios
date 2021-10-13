# Author: Arturo Salas Hernández
from time import asctime, sleep
from random import randint
from os import system

def lanzamiento():
	i = 3
	while i > 0:
		print("\t\tEspere... {} Seg".format(i))
		sleep(1)
		i -= 1

def aleatorio(programa, opcion, a, b):
	fecha = asctime().replace(':', '-')
	nombre = fecha + ".txt"
	contenido = ""
	contador = 1

	while True:
		system("cls")
		print(programa)
		resultado = randint(a, b)
		if opcion == '1':
			input("Presione Enter para hacer el lanzamiento del dado...")
			lanzamiento()
			print("Se ha lanzado el dado y el resultado obtenido es: {}\n".format(resultado))
		else:
			input("Presione Enter para hacer el lanzamiento de la moneda...")
			lanzamiento()
			if resultado == 1:
				resultado = "Águila"
			else:
				resultado = "Sol"
			print("Se ha lanzado la moneda y el resultado obtenido es: {}\n".format(resultado))

		contenido += "Lanzamiento de prueba N°{} => [{}]\n".format(contador, resultado)
		contador += 1
		
		if input("¿Desea realizar otro intento?(Enter = Si, n = No): ") == "n":
			if input("¿Desea guardar los resultado obtenidos en un fichero de texto?(Enter = Si, n = No): ") != "n":
				contenido = fecha + "\n\n" + programa + "\n" + contenido
				with open(nombre, "w") as fichero:
					fichero.write(contenido)
			system("cls")
			break

while True:
	opcion = input("Menu de opciones \n1.- => Dado \n2.- => Moneda \n3.- => Salir \nDigite el numero del programa a ejecutar:  ")
	if opcion == '1':
		programa = "Programa que simula el lanzamiento de un dado, sabiendo que los numeros del dado van del 1 al 6\n"
		aleatorio(programa, opcion, 1, 6)
	elif opcion == '2':
		programa = "Programa que simula el lanzamiento de una moneda, sabiendo que solo hay dos posibles resultados (Águila o Sol)\n"
		aleatorio(programa, opcion, 1, 2)
	elif opcion == '3':
		input("Gracias por usar este programa, presiona Enter para continuar...")
		break
	else:
		system("cls")
		print("Por favor, digite solo numeros del menu!")