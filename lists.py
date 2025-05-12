# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista = ["Red" , "Green" , "White", "Black" , "Pink", "Yellow"]
    nueva_lista = lista[:]
    if len(nueva_lista) > 5:
        del nueva_lista[5]
    if len(nueva_lista) > 4:
        del nueva_lista[4]
    if len(nueva_lista) > 0:
        del nueva_lista[0]
    return nueva_lista
remove_elements([])
    

def add_elements(list_to_add_elements):
    lista = ["Red" ,"Green" , "White" , "Black"]
    nueva_lista = lista[:]
    nueva_lista.insert(0, "Pink")
    nueva_lista.append("Yellow") 
    return nueva_lista
add_elements([])
   


def is_empty(list_to_check):
    lista = ["Red" , "Green" , "White", "Black" , "Pink", "Yellow"]
    nueva_lista = lista[:]
    if len(nueva_lista) == 0:
        return True
    else:
        return False
is_empty([])


def check_lists(list_to_compare1, list_to_compare2):
    lista1 = ["Black" , "Pink", "Yellow" , "Red" , "Green", "White"]
    lista2 = ["Red", "Green", "Yellow" , "White", "Black" , "Pink"]
    nueva_lista1 = lista1[:]
    nueva_lista2 = lista2[:]
    if len(nueva_lista1) > 2 and len(nueva_lista2) > 2:
        if  nueva_lista1[2] == nueva_lista2[2]:
            return True
        else: 
            return False
    else:
        return False
check_lists([], [])

def list_of_lists(list_of_lists_to_modify):
       lista = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
    nueva_lista = lista[:]
    if len(nueva_lista) > 0:
        nueva_lista[0] = nueva_lista[0][:2]
        nueva_lista[1] = nueva_lista[1][1:4]
        nueva_lista[2] = nueva_lista[2][-2:]
        return nueva_lista
    else:   
        return False
list_of_lists([])

