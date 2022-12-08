from shennon import Shennon


_input = int(input('Ввод текста через консоль(1) или файл(2): '))

if _input == 1:
    string = str(input("Введите текст: "))
elif _input == 2:
    file_name = str(input("Введите название файла: "))
    with open(file_name, 'r') as f:
        string = ''.join(f.readlines())
else:
    print('Неверная команда')
    exit()

s = Shennon()
s.calc(string)
s.save_probs()
s.save_encoded(string)
