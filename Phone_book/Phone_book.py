# Открывать файл .тхт
# Сохранить файл
# Показать все контакты
# Добавить контакт
# Найти контакт
# Изменить контакт
# Удалить контакт
# Выход
# Имя телефон и коментарий
path = 'Phone_book.txt'


def open_file() -> list:
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.readlines()
    return text


def save_file(txt: str, operation) -> None:
    with open(path, 'w', encoding='UTF-8') as file:
        if operation == []:
            new_text = txt
        else:
            new_text = (''.join(operation)) + '\n' + txt
        file.write(new_text)


def print_phone_book(operation) -> None:
    new_text = ''
    for i in operation:
        new_text += i
    print(new_text)


def add_contact() -> str:
    first_name = input('Введите имя контакта: ')
    second_name = input('Введите фамилию контакта: ')
    phone_number = input('Введите телефон контакта: ')
    comment = input('Введите коментарий для контакта: ')
    new_contact_list = ' '.join([first_name, second_name, phone_number, comment])
    return new_contact_list


def search_contact():
    search = input('Если вы хотите осуществить поиск по имени и фамилии, поставьте знак +. Если по номеру знак -.')
    text = open_file()
    all_contact = [i.lower() for i in text]
    found_contact = ''
    if search == '+':
        first_name = input('Введите имя искомого контакта: ').lower()
        second_name = input('Введите фамилию искомого контакта: ').lower()
        for i in all_contact:
            if first_name in i and second_name in i:
                found_contact += i
    else:
        number = input('Введите номер искомого контакта: ')
        for i in all_contact:
            if number in i:
                found_contact += i
    if found_contact == '':
        print('Контакт не существует')
    return found_contact


def change_contact() -> str:
    text = open_file()
    all_contacts = ''
    for i in text:
        all_contacts += i
    print(f'Найденые контакты: \n{all_contacts}')
    what_to_change = input('Введите что хотите поменять: ')
    new_information = input('Введите новую информацию: ')
    new_contact = all_contacts.replace(what_to_change, new_information)
    return ''.join(new_contact)


def delete_contact():
    text = open_file()
    all_contacts = ''
    cnt = 1
    for i in text:
        all_contacts += str(cnt) + '.' + ' ' + i
        cnt += 1
    print(f'Найденые контакты: \n{all_contacts}')
    delete_name = int(input('Введите номер строки который хотите удалить: '))
    del text[delete_name - 1]
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(''.join(text))


def menu():
    print(
        'Доступные команды: /comand - показывает список команд, /all - все контакты, \n'
        '/add - добавить контакт, /search - поиск контакта, /change - изменить контакт, \n'
        '/delete - удалить контакт, /exit - выйти из программы')
    while True:
        menu = input('Введите действие: ')
        if menu == '/comand':
            print('Доступные команды: /comand - показывает список команд, /all - все контакты, \n'
                  '/add - добавить контакт, /search - поиск контакта, /change - изменить контакт, \n'
                  '/delete - удалить контакт, /exit - выйти из программы')
            continue
        if menu == '/all':
            print_phone_book(open_file())
            continue
        if menu == '/add':
            new_contact = add_contact()
            save_file(new_contact, open_file())
            print('Контакт успешно добавлен.')
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(open_file())
            continue
        if menu == '/search':
            found = search_contact()
            print(f'Нашли следующие варианты:\n{found}')
            continue
        if menu == '/change':
            change = change_contact()
            ans = input('Хотите сохранить изменения? Введите да/нет: ').lower()
            if ans == 'да':
                with open('Phone_book.txt', 'w', encoding='UTF-8') as file:
                    file.write(change)
                print('Успешно')
            else:
                print('Изменения отменены')
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(open_file())
            continue
        if menu == '/delete':
            delete_contact()
            print('Контакт успешно удален')
            print('Теперь телефонный справочник выглядит так: ')
            print_phone_book(open_file())
            continue
        if menu == '/exit':
            print('До скорых встреч')
            break


menu()
