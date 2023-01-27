class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

#Создайте объект калькулятора
my_cl = Calculator()

while True:

    print("1: Сложение")
    print("2: Вычитание")
    print("3: Произведение")
    print("4: Деление")
    print("5: Выход")
    
    ch = int(input("Следующая операция: "))
    
    #Убедитесь, что пользователь ввел правильные данные
    if ch in (1, 2, 3, 4, 5):
        
        #Сначала проверьте, хочет ли пользователь выйти
        if(ch == 5):
            break
        
        #Если нет, то запросите входные данные и вызовите соответствующие методы       
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        
        if(ch == 1):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", my_cl.divide(a, b))
    
    else:
        print("Неверный ввод")