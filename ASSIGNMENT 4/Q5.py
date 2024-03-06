
def get_even_values(lst):
    return [num for num in lst if num % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_values(lst))
