# хранилище

import json
import tempfile
import argparse
import os

# парсим входящие аргументы
parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')

res = parser.parse_args()
key = res.key
val = res.val

# создаем путь к файлу
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def print_value(input_key):
    """

    :param input_key: ключ
    :return: выводим значение/-я ключа, если найдено, иначе None
    """
    if os.path.isfile(storage_path):
        with open(storage_path, 'r') as f:
            lstorage = json.loads(f.read())
        f.close()
        if input_key in lstorage.keys():
            print(*lstorage.get(input_key), sep=", ")
        else:
            print(None)
    else:
        print(None)


def add_and_print_value(input_key, input_val):
    """

    :param input_key: ключ
    :param input_val:  значение ключа для добавления
    :return: добавляем ключ и значение, если нет, или добавляем значение к существующему ключу
    """
    val1 = list()
    val1.append(input_val)
    my_storage = dict()
    # считали то, что есть в файле
    if os.path.isfile(storage_path):
        with open(storage_path, 'r') as f:
            my_storage = json.loads(f.read())
        f.close()

    # проверяем, есть ли уже такой ключ
    if input_key in my_storage.keys():
        # print("1")
        # проверяем есть ли такое значение в ключе, если нет, то добавляем
        if val in my_storage.get(input_key): #my_dict[input_key][0]
            None
        else:
            my_list = my_storage.get(input_key)
            my_list.append(input_val)
    # если такого ключа нет, то добавляем в my_storage
    else:
        my_storage.update({input_key: val1})
    # записываем
    with open(storage_path, 'w') as f:
        f.write(json.dumps(my_storage))
    f.close()


if val is None:
    print_value(key)
else:
    add_and_print_value(key, val)