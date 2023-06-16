import datetime
import Note
import file

def write_note():
    head = input('Введите Название заметки: ')
    body = input('Введите Описание заметки: ')
    return Note.Note(head=head, body=body)

def add():
    note = write_note()
    array = file.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file.write_file(array, 'a')
    print('Заметка добавлена...')


def show_all():
    bul = True
    array = file.read_file()
    for notes in array:
        print(Note.Note.map_note(notes))
        bul = False    
    if bul == True:
        print('Заметок нет')


def show_date():
    bul = True
    array = file.read_file()
    for notes in array:
        date = input('Введите дату в формате дд.мм.гггг: ')
        if date in Note.Note.get_date(notes):
            print(Note.Note.map_note(notes))
            bul = False
    if bul == True:
        print('Заметок в эту дату нет')

def edit():
    id = input('Введите id необходимой заметки: ')
    array = file.read_file()
    bul = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            bul = False
            note = write_note()
            Note.Note.set_head(notes, note.get_head())
            Note.Note.set_body(notes, note.get_body())
            Note.Note.set_date(notes)
            print('Заметка отредактирована.')
    if bul == True:
        print('Такой заметки нет, введите верный id')
    file.write_file(array, 'a')

def remove():
    bul = True
    id = input('Введите id необходимой заметки, которую хотите удалить: ')
    array = file.read_file()
    for notes in array:
        if id == Note.Note.get_id(notes):
            bul = False
            array.remove(notes)
            print('Заметка удалена.')
    if bul == True:
        print('Такой заметки нет, введите верный id')
    file.write_file(array, 'a')

def show_id():
    bul = True
    id = input('Введите id необходимой заметки, которую хотите удалить: ')
    array = file.read_file()
    for notes in array:
        if id == Note.Note.get_id(notes):
            bul = False
            print(Note.Note.map_note(notes))
    if bul == True:
        print('Такой заметки нет, введите верный id')
    file.write_file(array, 'a')
