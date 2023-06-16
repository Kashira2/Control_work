import datetime

def write_note():
    id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')