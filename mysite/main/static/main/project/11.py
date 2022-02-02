print ("Привет, перед вами проект №11 (тексты к песням) 'Путь к успеху'!")
print ("Добро пожаловать на вечерний огонёк! \nВыберите любимого исполнителя:")
print("1.Ленинград\n2.Сектор газа\n3.Отава ё")
set= input("Введите цифру или исполнителя : ")
q = (set.lower())
q = q.replace(" ","")

if q== '1' or q =='ленинград':
    print ("1.Баба Бомба\n2.www\n3.Менеджер")
    set1= input("Выберите трэк : ")
    q1 = (set1.lower())
    q1 = q1.replace(" ", "")
    if q1=='1'or q1=='бабабомба':
        bomba = open('bomba.txt', encoding='utf-8')
        print(bomba.read())
    if q1=='2'or q1=='www':
        www = open('www.txt', encoding='utf-8')
        print(www.read())
    if q1=='3'or q1=='менеджер':
        menedger = open('menedger.txt', encoding='utf-8')
        print(menedger.read())

if q== '2' or q == 'секторгаза':
    print("1.30 Лет\n2.Вальпургиева ночь\n3.Твой звонок")
    set1 = input("Выберите трэк : ")
    q1 = (set1.lower())
    q1 = q1.replace(" ", "")
    if q1 == '1' or q1 == '30лет':
        let = open('30let.txt', encoding='utf-8')
        print(let.read())
    if q1 == '2' or q1 == 'вальпургиеваночь':
        noch = open('noch.txt', encoding='utf-8')
        print(noch.read())
    if q1 == '3' or q1 == 'твойзвонок':
        zvonok = open('zvonok.txt', encoding='utf-8')
        print(zvonok.read())
if q== '3' or q =='отавае':
    print("1.Ой Дуся Маруся\n2.Сумецкая\n3.Про Ивана")
    set1 = input("Выберите трэк : ")
    q1 = (set1.lower())
    q1 = q1.replace(" ", "")
    if q1 == '1' or q1 == 'ойдусямаруся':
        dusya = open('dusya.txt', encoding='utf-8')
        print(dusya.read())
    if q1 == '2' or q1 == 'сумецкая':
        sumetskaya = open('sumetskaya.txt', encoding='utf-8')
        print(sumetskaya.read())
    if q1 == '3' or q1 == 'проивана':
        proivana = open('proivana.txt', encoding='utf-8')
        print(proivana.read())
