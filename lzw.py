from struct import *


def decode(path, n):
    # получение сжатого файла и количество битов из командной строки
    # открытие сжатого файла
    input_file, n = path, n
    file = open(input_file, "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""

    # Чтение сжатого файла
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data,) = unpack('>H', rec)
        compressed_data.append(data)

    # Создание и инициализация словаря
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    # перебор кодов
    # Алгоритм LZW
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    # сохранение распакованной строки в файл
    out = input_file.split(".")[0]
    output_file = open(out + "_decoded.txt", "w")
    for data in decompressed_data:
        output_file.write(data)

    output_file.close()
    file.close()


def encode(path, n):
    # берем входной файл и количество бит из командной строки
    # определение максимального размера таблицы
    input_file, n = path, n
    maximum_table_size = pow(2, int(n))
    file = open(input_file)
    data = file.read()

    # Создание и инициализация словаря
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    string = ""
    compressed_data = []

    # итерируемся по входным символам
    # Алгоритм LZW
    for symbol in data:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if len(dictionary) <= maximum_table_size:
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    # сохранение сжатой строки в файл
    out = input_file.split(".")[0]
    output_file = open(out + "_encoded.txt", "wb")
    for data in compressed_data:
        output_file.write(pack('>H', int(data)))

    output_file.close()
    file.close()


if __name__ == '__main__':
    encode("data2.txt", 8)
    decode("data2_encoded.txt", 8)
