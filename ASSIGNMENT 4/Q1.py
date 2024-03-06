def second_largest_smallest(lst):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in lst:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num

    print(f'Second largest: {max2}')
    print(f'Second smallest: {min2}')
lst = [3, 7, 1, 9, 2, 5, 4, 6, 8, 10]
second_largest_smallest(lst)