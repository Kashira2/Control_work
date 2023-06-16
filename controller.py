import view
import model as m

def run():
    while True:
        command = view.menu()
        if command == '7':
            break

        if command == '1':
            print('\nНаписать заметку:')
            m.add()
        elif command == '2':
            print('\nПоказать заметки:')
            m.show_all()
        elif command == '3':
            print('\nРедактировать заметку:')
            m.edit()
        elif command == '4':
            print('\nУдалить заметку:')
            m.remove()
        elif command == '5':
            print('\nВыбрать заметку по дате:')
            m.show_date()
        elif command == '6':
            print('\nНайти заметку по id:')
            m.show_id()
        else:
            print('\nКоманда не найдена')
