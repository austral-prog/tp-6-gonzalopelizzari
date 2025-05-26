def remove_elements(list_to_remove_elements):
    list1 = list_to_remove_elements
    if len (list1) < 2:
        return []
    elif len (list1) < 5:
        return list1[1:]
    elif len (list1) ==5 : 
        return list1[1:-1]
    elif len (list1) == 6 :
        return list[1:-2]
    else:
        list1 = list1[1:5] + list1[7:]
        return list1


    

def add_elements(list_to_add_elements):
    list1 = list_to_add_elements
    list2 = ["Pink"]
    list2[1:-1] = list1
    list2 = list2[:] + ["Yellow"]
    
    return list2

   


def is_empty(list_to_check):
    list1 = list_to_check
    list2 = []
    if list1 == list2:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    list1 = list_to_compare1
    list2 = list_to_compare2
    if len(list1) > 2 and len(list2) > 2:
        if  list1[2] == list2[2]:
            return True
        else: 
            return False
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    list1 = list_of_lists_to_modify
    if len(list1 [0]) < 3:
        list1 [0] = list1 [0] [0:]
    else:
        list1 [0] = list1 [0] [0:2]
    if len(list1 [1] ) < 2:
        list1 [1] = []
    elif len(list1 [1]) < 5:
        list1 [1] = list1 [1] [1:]
    else:
        list1 [1] = list1 [1] [1:4]
    if len (list1 [2]) < 3:
        list1 [2] = list1 [2]
    else:
        list1 [2] = list1 [2] [-2:]
    return list1

