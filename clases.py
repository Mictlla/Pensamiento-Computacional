def run():
    # nombre = (input('¿Cual es tu nombre?: '))
    # bienvenida = f'Bienvenido {nombre}'
    # total_long = len(bienvenida)
    # print(bienvenida)
    # print(f'La longitud de la cadena es de {total_long} caracteres')


# num_1 = int(input('Escoge un numero entero: '))
# num_2 = int(input('Escoge otro numero entero: '))

# if num_1 > num_2:
#     print('El primer numero es mayor que el segundo')
# elif num_1 < num_2:
#     print('El segundo numero es mayor que el primero')
# else:
#     print('Los numeros son iguales')


    # usuario_1 = input('¿Cual es tu nombre?')
    # edad_1 = int(input('¿Cual es tu edad?'))
    # usuario_2 = input('¿Cual es tu nombre?')
    # edad_2 = int(input('¿Cual es tu edad?'))

    # if edad_1 > edad_2:
    #     print(f'{usuario_1} es mayor que {usuario_2}')
    # elif edad_1 < edad_2:
    #     print(f'{usuario_1} es menor que {usuario_2}')
    # else:
    #     print(f'{usuario_1} y {usuario_2} tienen la misma edad.')

    # x = 0.0
    # for i in range(10):
    #     x += 0.1

    # if x == 1.0:
    #     print(f'x = {x}')
    # else:
    #     print(f'x != {x}')


    # objetivo = int(input('Escoge un numero entero:'))
    # respuesta = 0

    # while respuesta**2 < objetivo:
    #     print(respuesta)
    #     respuesta += 1

    # if respuesta**2 == objetivo:
    #     print(f'la raiz cuada de {objetivo} es {respuesta}')
    # else:
    #         print(f'{objetivo} no tiene raiz cuadrada exacta')


    # objetivo = int(input('Escoge un numero: '))
    # epsilon = 0.01
    # paso = epsilon**2 
    # respuesta = 0.0

    # while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    #     # print(abs(respuesta**2 - objetivo), respuesta)
    #     respuesta += paso

    # if abs(respuesta**2 - objetivo) >= epsilon:
    #     print(f'No se encontro la raiz cuadrada {objetivo}')
    # else:
    #     print(f'La raiz cudrada de {objetivo} es {respuesta}')


    # objetivo = int(input('Escoge un numero: '))
    # epsilon = 0.01
    # bajo = 0.0
    # alto = max(1.0, objetivo)
    # respuesta = (alto + bajo) / 2

    # while abs(respuesta**2 - objetivo) >= epsilon:
    #     print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    #     if respuesta**2 < objetivo:
    #         bajo = respuesta
    #     else:
    #         alto = respuesta

    #     respuesta = (alto + bajo) / 2

    # print(f'La raiz cuadrada de {objetivo} es {respuesta}')


    def factorial(n):
        """ Calcula el factorial de n

        n int > 0
        returns n!
        """
        if n == 1:
            return 1
        return n * factorial(n-1)
    n = int(input('Escribre un entero:'))
    print(factorial(n))
    


if __name__ == "__main__":
    run()
