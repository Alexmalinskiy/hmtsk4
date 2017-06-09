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
        inp = input_data("Введите команду. Для выхода наберите q. Список всех команд - help",False)
        if str(inp).lower() == "q":
            print("Сеанс завершён.")
            print("На выходе документы имеют вид:", documents)
            print("На выходе полки имеют вид:", directories)

            break
        
        elif str(inp).lower() == "help": 
            list_all_commands()
            
        elif str(inp).lower() == "p":
            num = input_data("Введите номер документа",True)        
            if num == None:
                print("Неверно введен номер документа")
                exit()
            Man = get_person_by_doc_number(documents, num)
            check_return(Man)
            
        elif str(inp).lower() == "l":
            list_all_docs(documents)
            
        elif str(inp).lower() == "s":
            num = input_data("Введите номер документа",True)        
            if num == None:
                print("Неверно введен номер документа")
                exit()          
            key = get_shelf_by_doc_number(directories, num)
            check_return(key)
            
        elif str(inp).lower() == "a":
            documents, directories = add_doc(documents, directories)
            
        elif str(inp).lower() == "d":
            num = input_data("Введите номер документа",True)        
            if num == None:
                print("Неверно введен номер документа")
                exit()  
            documents, directories = remove_doc_by_number(documents, directories, num)
        elif str(inp).lower() == "m":
            directories = move_doc(documents,directories)
            
        elif str(inp).lower() == "as":
            shelf_num = input_data("Введите номер полки",True)
            if shelf_num == None:
                print("Неверно введён номер полки")
                exit()
            directories = add_directory(directories,shelf_num)
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

def input_data(text, isdigit):
# функция ввода данных. передаем признак isdigit, если true значит должно принимать только числа, если false то буквы и числа
    print(text)
    inp = input()
    if isdigit == True:
        if inp.isalpha():
            return
    else:
        if inp.isdigit():
            return
    return inp
    
def add_directory(directories,shelf_num):
# добавляет полку
    Found_shelf = False
    for key,item in directories.items():
        if key == shelf_num:
            Found_shelf = True
            print("Такая полка уже есть")
    if Found_shelf == False:        
        directories[shelf_num] = []
    return directories

def add_doc(documents,directories):
# добавить документ на полку
    found = False # нашли ли полку по номеру
    
    type = input_data("Введите тип документа",False)        
    if type == None:
        print("Неверно введён тип документа")
        return documents, directories
    
    num = input_data("Введите номер документа", True)
    if num == None:
        print("Неверно введён номер документа")
        return documents, directories

    name = input_data("Введите имя", False)
    if name == None:
        print("Неверно введёно имя владельца")
        return documents, directories
    
    shelf_num = input_data("Введите номер полки",True)
    if shelf_num == None:
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

def move_doc(documents,directories):
# передвигает документ
    num = input_data("Введите номер документа",True)        
    if num == None:
        print("Неверно введен номер документа")
        exit()

    shelf_num = input_data("Введите номер полки",True)
    if shelf_num == None:
        print("Неверно введён номер полки")
        exit()

    Found_doc = False
    Found_shelf = False
    if get_shelf_by_doc_number(directories, num) != None:
        old_shelf_num = get_shelf_by_doc_number(directories, num)
        Found_doc = True

    if Found_doc == True:
        for key,item in directories.items():
            if key == shelf_num:
                Found_shelf = True
                directories[old_shelf_num].remove(num)
                item.append(num)
                break
        if Found_shelf == False:
            print("Полка не найдена!")
    else:
        print("Документ не найден")
    return directories    
    

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
