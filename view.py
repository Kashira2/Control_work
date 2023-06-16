def run():
    while True:
        command = input('1 - Написать заметку\n'
                        '2 - Показать заметку\n'
                        '3 - Редактировать заметку\n'
                        '4 - Удалить заметку\n'
                        '5 - Показать все заметки\n'
                        '6 - Выход\n' +
                        'Выберете пункт: ')
        if command == '6':
            break

        if command == '1':
            print('\nНаписать заметку:')
            
        elif command == '2':
            print('\nПоказать заметку:')
           
        elif command == '3':
            print('\nРедактировать заметку:')

        elif command == '4':
            print('\nУдалить заметку:')

        elif command == '5':
            print('\nСписок всех заметок:')
        else:
            print('\nКоманда не найдена')
