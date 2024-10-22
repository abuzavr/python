def custom_write(file_name, strings):
    strings_positions = {}
    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding = 'utf-8') as file:

        for i, string in enumerate(strings, start = 1):
            byte_position = file.tell()  # Получаем текущую позицию байта перед записью
            file.write(string + '\n') # Записываем строку в файл с добавлением новой строки
            strings_positions[i, byte_position] = string # Сохраняем позицию и строку в словарь

    return strings_positions # Возвращаем словарь с номерами строк и байтов

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)