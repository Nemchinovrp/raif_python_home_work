from main import print_hi
# написать функцию, которая выводит которая выводит все числа от 1 до X без использования циклов

def printNumberRange(num):
    if num > 0:
        printNumberRange(num - 1)
        print(num)

if __name__ == '__main__':
    printNumberRange(10)
