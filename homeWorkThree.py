import random

from main import print_hi


def quick_sort(list):
    if len(list) > 1:
        x = list[random.randint(0, len(list)-1)]
        low = [num for num in list if num < x]
        equal = [num for num in list if num == x]
        high = [num for num in list if num > x]
        list = quick_sort(low) + equal + quick_sort(high)
    return list


if __name__ == '__main__':
    list = [5, 8, 9, 4, 2, 9, 1, 8]
    print(quick_sort(list))


