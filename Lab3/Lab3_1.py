try:
        
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
        
        
    result = a / b
    print(f"Результат ділення {a} на {b}: {result}")
    
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна!")