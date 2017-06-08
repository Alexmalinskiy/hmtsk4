def main():
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}]
    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []}
    while True:
        print("Введите команду. Для выхода наберите q. Список всех команд - help")
        inp = input()
        if inp.lower() == "q":
            print("Сеанс завершён.")
            break
        elif inp.lower() == "help": 
            list_all_commands()
            
        elif inp.lower() == "p":
            print("Введите номер документа")
            num = input()        
            if num.isalpha():
                print("Неверно введен номер документа")
            Man = get_person_by_doc_number(documents, num)
            check_return(Man)
            
        elif inp.lower() == "l":
            list_all_docs(documents)
            
        elif inp.lower() == "s":
            print("Введите номер документа")
            num = input()
            if num.isalpha():
                print("Неверно введен номер документа")           
            key = get_shelf_by_doc_number(directories, num)
            check_return(key)
            
        elif inp.lower() == "a":
            documents, directories = add_doc(documents, directories)
            
        elif inp.lower() == "d":
            print("Введите номер документа")
            num = input()
            if num.isalpha():
                print("Неверно введен номер документа")    
            documents, directories = remove_doc_by_number(documents, directories, num)
            
##        elif inp.lower() == "m":
##
##        elif inp.lower() == "as":
##
        else:
            print("Неверная команда!")

def list_all_commands():
# вывести на экран все команды
    print("p : Личность человека по номеру документа")
    print("l : Список всех документов")
    print("s : Номер полки по номеру документа")
    print("a : Добавить новый документ в каталог")
    print("d : Удалить документ")
    print("m : Переместить документ")
    print("as : Добавить полку")
    print("q : Выйти из программы")
    print("help : Список всех команд")

def get_person_by_doc_number(documents, num):
# найти человека по номеру док-та
    for doc in documents:
        if doc["number"] == num:
            Man = doc["name"]
            return Man

def check_return(variable):
# проверяет переменную, если None то ошибка, а если нет то выводит переменную    
    if variable == None:
        print("Не найдено")
    else:
        print(variable)

def list_all_docs(documents):
# выводит список всех документов
    for doc in documents:
        to_print = ""
        for key,item in doc.items():
            to_print += item + " "
        print(to_print)

def get_shelf_by_doc_number(directories, num):
# найти полку по номеру док-та
    for key,item in directories.items():
        if num in item:
            return key

def add_doc(documents,directories):
# добавить документ на полку
    found = False # нашли ли полку по номеру
    
    print("Введите тип документа")
    type = input()
    if type.isdigit():
        print("Неверно введён тип документа")
        return documents, directories
    
    print("Введите номер документа")
    num = input()
    if num.isalpha():
        print("Неверно введён номер документа")
        return documents, directories
    
    print("Введите имя")
    name = input()
    if name.isdigit():
        print("Неверно введёно имя владельца")
        return documents, directories
    
    print("Введите номер полки")
    shelf_num = input()
    if shelf_num.isalpha():
        print("Неверно введён номер полки")
        return documents, directories
    
    for key,item in directories.items():
        if key == shelf_num:
            found = True
            item.append(num)
            documents.append({"type": type, "number": num, "name": name})
            break
    if found == False:
        print("Полка не найдена!")
    return documents, directories

def remove_doc_by_number(documents,directories,num):
# удаляет документ из списков по номеру
    Found = False
    for i,doc in enumerate(documents):
        if doc["number"] == num:
            Found = True
            documents.pop(i)
    if Found == True:
        if get_shelf_by_doc_number(directories, num) != None:
            directories[get_shelf_by_doc_number(directories, num)].remove(num)
    else:
        print("Документ не найден")    
    return documents, directories

main()
