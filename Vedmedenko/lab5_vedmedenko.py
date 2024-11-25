import string
import re
from tabulate import tabulate

def read_and_process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Виділення першого речення
        sentences = re.split(r'[.!?]', text)
        first_sentence = sentences[0].strip() if sentences else ""
        print("Перше речення:")
        print(first_sentence)

        # Видалення пунктуації, збереження дефісів та апострофів
        words = re.findall(r"[a-zA-Z\u0400-\u04FF'-]+", text)

        # Розділення українських і англійських слів
        ukrainian_words = [word for word in words if re.match(r'^[\u0400-\u04FF]', word)]
        english_words = [word for word in words if re.match(r'^[a-zA-Z]', word)]

        # Сортування слів
        ukrainian_words_sorted = sorted(set(ukrainian_words), key=str.casefold)
        english_words_sorted = sorted(set(english_words), key=str.casefold)

        # Таблиця для українських слів
        print("\nУкраїнські слова:")
        ukr_table_data = [[word] for word in ukrainian_words_sorted]
        print(tabulate(ukr_table_data, headers=["Слово"], tablefmt="grid"))

        # Таблиця для англійських слів
        print("\nАнглійські слова:")
        eng_table_data = [[word] for word in english_words_sorted]
        print(tabulate(eng_table_data, headers=["Word"], tablefmt="grid"))

        # Підсумкова інформація
        total_words = len(words)
        total_unique_words = len(set(words))
        print(f"\nЗагальна кількість слів (включно з повтореннями): {total_words}")
        print(f"Кількість унікальних слів: {total_unique_words}")
        print(f"Кількість унікальних українських слів: {len(set(ukrainian_words))}")
        print(f"Кількість унікальних англійських слів: {len(set(english_words))}")

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

file_path = 'text.txt'
read_and_process_file(file_path)
