# Replace the "ANSWER HERE" with your answer

def remove_elements(lista):
    copia_lista_uno = lista[:] #copio la lista para no modificar la original

    #borro por índice, acordate de los desplazamientos
    if len(copia_lista_uno) > 5: #si tiene mas de 5 elementos
        del copia_lista_uno[5]  #borra el sexto elemento (índice 5)
    if len(copia_lista_uno) > 4: #si tiene mas de 4 elementos
        del copia_lista_uno[4]  #borra el quinto elemento (índice 4)
    if len(copia_lista_uno) > 0: #si tiene mas de 1 elemento
        del copia_lista_uno[0]  #borra el primer elemento (índice 0)

    return copia_lista_uno

def add_elements(lista):
    copia_lista_dos = lista[:]  #misma que función de arriba.
    copia_lista_dos.insert(0, 'Pink') #le pones elemento Pink en el primer índice.
    copia_lista_dos.append('Yellow') #le pones como ultimo elemento, el elemento Yellow.
    
    return copia_lista_dos #ahora se te modifico la variable copia_lista_dos que es una lista nueva que tiene Pink como primer elemento, y Yellow como último elemento.


def is_empty(lista):
    return len(lista) == 0 #sabes que esto es booleano, te va a dar true si la lista esta vacía (osea que tiene cero elementos) y false si tiene más de un elemento.


def check_lists(lista1, lista2):
    if len(lista1) >= 3 and len(lista2) >= 3: #si ambas listas tienen al menos 3 elementos.
        return lista1[2] == lista2[2] #fijate si es verdad que los terceros elementos (índices 2) de cada lista son el mismo.
    else: return False


def list_of_lists(listas):
    nueva = [] #lista vacía para guardar las 3 listas recortadas.

    #primera sublista: primeros 2 elementos
    if len(listas) >= 1:
        sublista1 = listas[0][:2]  
    else:
        sublista1 = []
    nueva.append(sublista1)

    #segunda sublista: del segundo al cuarto elemento (índices 1 al 3)
    if len(listas) >= 2:
        sublista2 = listas[1][1:4]  
    else:
        sublista2 = []
    nueva.append(sublista2)

    #tercera sublista: últimos 2 elementos
    if len(listas) >= 3:
        sublista3 = listas[2][-2:]  
    else:
        sublista3 = []
    nueva.append(sublista3)

    return nueva
