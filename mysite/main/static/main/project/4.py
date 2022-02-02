print ("Привет, перед вами проект №4 (информация о биографии) 'Путь к успеху'!")

surname = str(input("Введите вашу Фамилию  :"))
name = str(input("Введите ваше Имя  :"))
secname = str(input("Введите ваше Отчество  :"))
plase_of_birst = str(input("Введите ваше место рождения  :"))
while True:
    try:
        year_of_birth = int(input("Введите ваш год рождения  :"))
        if (year_of_birth >= 1930) and (year_of_birth <= 2021):
            break
        elif  (year_of_birth <= 1930):
            print("Ошибка - вы столько не проживёте...")
        else:
            print("Неверный ввод, попробуйте ещё...")
    except:
        print("Ошибка - это не число")
vop = str(input("Введите город проживания, вашу специальность (через пробел)  :"))

q = (surname, name,secname, plase_of_birst, year_of_birth)
# split() - разбивает строку на элементы, слова (по пробелу).
q1 = vop.split()

# Создаём классы, в которых отображаем все интересующие параметры (ФИО, место рождения, год и т.д.)
class persona:
    # через функцию def init - инициализируем предметы, параметры
    def __init__(self, surname, name,secname, plase_of_birst, year_of_birth):
        self.surname = surname
        self.name = name
        self.secname = secname
        self.plase_of_birst = plase_of_birst
        self.year_of_birth = year_of_birth
    def print_info(self, n):
        # Встроенная функция range() используется для построения числовых последовательностей
        for i in range (n):
            print(f"Фамилия: {self.surname}")
            print(f"Имя: {self.name}")
            print(f"Отчество: {self.secname}")
            print(f"место рождения: {self.plase_of_birst}")
            print(f"год рождения: {self.year_of_birth}")
class persona1:
    def __init__(self, sity, prof):
        self.sity = sity
        self.prof = prof
    def print_info1(self, n):
        for i in range(n):
            print (f"Город: {self.sity}")
            print (f"Специальность: {self.prof}")
# переменная р1 = (класс persona, включая в себя функции и уже разбита по отдельным словам строка. )
# цифры 0, 1, 2, 3, 4 это указывают на очерёдность разбитых по отдельности слов в строке q
p1 = persona(q[0], q[1] , q[2], q[3], q[4])
p2 = persona1(q1[0], q1[1])
p1.print_info(1)
p2.print_info1(1)