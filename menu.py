import check_errors as cher
import changes_in_notes as chnot


def show_menu():
    item = 1
    while item in range(1, 5):
        print(
            "\nВыберите пункт меню: \n1-создать заметку\n2-прочитать спискок заметок"
            "\n3-редактировать заметку\n4-удалить заметку"
            "\nДля выхода из меню нажмите любую клавишу")
        item = cher.check_int_number()
        if item == 1:
            chnot.add_notes()
        elif item == 2:
            chnot.read_notes()
        elif item == 3:
            chnot.correct_notes()
        elif item == 4:
            chnot.dell_notes()
