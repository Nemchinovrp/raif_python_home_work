from main import print_hi

#  написать функцию, которая находит заданный ключ в словаре и выдаёт значение этого ключа на экран (словарь в файле dict_task.py), если ключа нет в словаре на всех уровнях вложенности то обработать сценарий и сообщить об этом в выводе

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def recursive_keys(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_keys(value)
        else:
            yield (key, value)


def findKey(fkey):
    for key, value in recursive_keys(site):
        if (key == fkey):
            print(value)
            return
    print('key dont find')


if __name__ == '__main__':
   findKey('body')
