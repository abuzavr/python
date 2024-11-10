class WordsFinder:

    def __init__(self, filename):
        #сохраняем имена файлов в атрибут
        self.filename = filename

    def get_all_words(self):
        #словарь для хранения слов
        all_words = {}

        for file_name in self.filename:
                try:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation, ' ')
                # Разбиваем текст на слова
                words = text.split()
                # Добавляем слова файла в словарь
                all_words[file_name] = words
            except FileNotFoundError:
            print(f"Файл {file_name} не найден.")
            all_words[file_name] = []


