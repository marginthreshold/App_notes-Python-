import codecs
import csv


def add_notes():
    new_note = (input("Введите новую заметку и нажмите Enter\n"))
    with codecs.open("notes.csv", "a", "utf-8") as file:
        file.writelines(new_note + "\n")


def read_notes():
    with codecs.open("notes.csv", "r", "utf-8") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            print(f"{i + 1} {' '.join(row)}")


def dell_notes():
    dell_note = input("Введите номер строки заметки для удаления и нажмите Enter\n")
    with codecs.open("notes.csv", "r", "utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
    if not dell_note.isdigit() or int(dell_note) < 0 or int(dell_note) > len(rows):
        print("Неправильный номер строки")
        return
    else:
        rows.pop(int(dell_note) - 1)
    with codecs.open("notes.csv", "w", "utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print(f"Строка {dell_note} удалена.\n")


def correct_notes():
    corrected_note = input("Введите номер строки заметки для корректировки и нажмите Enter\n")
    with codecs.open("notes.csv", "r", "utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
    if not corrected_note.isdigit() or int(corrected_note) < 0 or int(corrected_note) > len(rows):
        print("Неправильный номер строки")
        return
    else:
        print(f"Заметка в строчке {int(corrected_note)}:\n {''.join(rows[int(corrected_note) - 1])}")
        print("Введите вместо нее новую заметку и нажмите Enter")
        rows[int(corrected_note) - 1] = [input()]
    with codecs.open("notes.csv", "w", "utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        print(f"Строка {corrected_note} изменена.\n")
