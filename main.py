import os

dictionary = {
    'А': 'X',
    'В': 'Y',
    'С': 'Z'
}

path = '/Users/romanlaptev/Desktop/testlatinic/'


def rename_file(file_name):
    new_file_name = ''
    for symbol in file_name:
        if symbol in dictionary:
            new_file_name += dictionary[symbol]
        else:
            new_file_name += symbol
    os.rename(path + file_name, path + new_file_name)


def get_file_names():
    files = [f for f in os.listdir(path)]
    return files


def contains_rus_symbol(file_name):
    for symbol in file_name:
        if symbol in dictionary:
            return True
    return False


if __name__ == '__main__':

    files = get_file_names()
    for f in files:
        if contains_rus_symbol(f):
            rename_file(f)
