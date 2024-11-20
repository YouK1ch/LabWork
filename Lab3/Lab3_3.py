import math

a = input("Введіть число для обчислення квадратного кореня: ")
    
try:
    num = float(a)
        
    if num < 0:
        raise ValueError("Квадратний корінь з від'ємного числа не визначений!")
        
        
    sqrt_value = math.sqrt(num)
    print(f"Квадратний корінь з {num}: {sqrt_value}")
    
except ValueError as e:
    print(f"Помилка: {e}")