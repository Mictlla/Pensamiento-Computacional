"""Como metodo para programacion defensiva es un recurso bastante util ya que nos permite limitar el uso de la funcion a los parametros que nosotros le indicquemos evitando bugs a posterior
"""
# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_palabras):
    primeras_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, 'f{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])
    
    return primeras_letras