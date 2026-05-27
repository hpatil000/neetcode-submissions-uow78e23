from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    for i in my_list:
        if i == my_list[index]:
            my_list.pop(index)
    return my_list
    pass


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    # for i in my_list:
    #     for n in range (len(my_list)): 
    #         my_list.pop(n-1)
    # return my_list
    for i in range(n):
        a = my_list.pop()
    return my_list
    
           
    pass


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
