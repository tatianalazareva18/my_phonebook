#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
#для изменения и удаления данных.
'''
1. Создание файла:+++
    - открываем файл на дозапись # a+++
2. Добавление контакта: +++
        -запросить у пользователя данные контакта +++
        -открываем файл на дозапись # a  +++
        -добавить новый контакта  +++
3. Вывод данных на экран: +++
        -открыть файл на чтение # r +++
        -считать файла  +++    
        -вывести данные на экран  +++
4. Поиск контакта:
        - выбор варианта поиска
        -запросить данные для поиска
        -открываем файл на чтение
        -считываем данные контакта, сохранили в переменную
        - осуществляем поиск контакта
        - выводим на экран найденный контакта
5. Создание юзеринтерфейса(UI): +++
        -вывести меню на экран     +++ 
        -запросить у пользователя вариант действия +++
        - запустить соответстующую функцию +++
        -осуществить возможность выхода из программы +++
'''


def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес(город) контакта: ').title()

def read_phonebook(file = 'phonebook.txt'):
    with open(file, 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    return contacts_str.rstrip().split('\n\n')

def write_phonebook(contact_list):
    # print(str.join('\n\n', contact_list))
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write(str.join('\n\n', contact_list) + '\n\n')

def copy_data():
    file = input('Введите имя файла: ')
    idx = int(input('выберите индекс контакта: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1 ):
        print('некорректный ввод! Индекс должен быть меньше ' + len(contact_list))
        idx = input('выберите индекс контакта: ')

    contact = contact_list[idx]

    with open(file, 'a', encoding='utf-8') as file:
        file.write(contact + '\n\n')#дозаписываем контакт в файл



def make_contact(surname, name, patronymic, phone, address):
    return f'{surname} {name} {patronymic}: {phone}\n{address}' 

def edit_contact():
    idx = int(input('выберите индекс контакта: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1 ):
        print('некорректный ввод! Индекс должен быть меньше ' + len(contact_list))
        idx = input('выберите индекс контакта: ')

    contact = contact_list[idx]
    print('Изменить данные контакта: ')
    print(contact)

    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()

    contact_list[idx] = make_contact(surname, name, patronymic, phone, address)
    write_phonebook(contact_list)

def delete_contact():
    idx = int(input('выберите индекс контакта: '))
    contact_list = read_phonebook()
    while ( idx > len(contact_list) - 1 ):
        print('некорректный ввод! Индекс должен быть меньше ' + len(contact_list))
        idx = input('выберите индекс контакта: ')

    contact = contact_list[idx]
    print('Вы хотите удалить этот контакт? ')
    print(contact)
    var = input('если "Да" введите 1: ')
    if var == '1':
        contact_list.pop(idx)
        write_phonebook(contact_list)
    

def creat_contact():# создаем соответ.переменные и вызываем эти функции и получаем данные для создания контакта
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n' 


def add_contact():#создаем контакт в виде строки, сохраняем в переменную, открываем файл на дозапись 
    contact_str = creat_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)#дозаписываем контакт в файл
     
def print_contacts():#выводим контакты
    with open('phonebook.txt', 'r', encoding='utf-8') as file:#открываем файл на считывание
        contacts_str = file.read()#помещаем в переменную весь файл в виде одной строки
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')#строку контактов переделываем в список контактов.С помощью 
    for n, contact in enumerate(contacts_list, 1):      #rstrip убираем пробелы справа и нумеруем
        print(n, contact)
   
def search_contact():#поиск контакта.Выводим на экран возможные варианты поиска
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчетству\n'
            '4. По номеру телефона\n'
            '5. По адресу\n'
        )
    var = input('выберите вариант поиска: ')#пользователь выбирает выриант
    while var not in ('1', '2', '3', '4', '5'):#попадает в цикл, если вводит неверный вариант
            print('некорректный ввод!')
            var = input('выберите вариант поиска: ')
    i_var = int(var) - 1#преобазуем значение var в интовое значение и помещаем в переменную i_var (индекс)

    search = input('Введите данные для поиска: ').title()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    #print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)

                
def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):#открываем файл на дозапись Просто создает запись
        pass

    var = 0    
    while var != '6':#вариант выхода
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Редактирование контакта\n'
            '5. Удаление контакта\n'
            '7. Копирование данных\n'
            '6. Выход'
        )
        print()#пустая строка для красоты

        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5', '6', '7'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()
        
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '7':
                copy_data()
            case '6':
                print('До свидания!')
        print()
    
if __name__== '__main__': 
    interface()


       