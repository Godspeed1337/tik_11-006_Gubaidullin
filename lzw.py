def decompress(compressed_data):
    next_code = 256
    decompressed_data = ""
    string = ""

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

    return decompressed_data


if __name__ == '__main__':
    file_name = str(input('Введите имя файла: '))
    # тут будут содержаться цифры
    comressed = []
    with open(file_name, 'r') as f:
        while chars := f.read(8):
            print(chars)
            print(int(chars, 2))
            comressed.append(int(chars, 2))

    decompressed = decompress(comressed)
    print(decompressed)