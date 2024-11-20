import math

num = float(input("Введіть число для обчислення квадратного кореня: "))
    
if num >= 0:
    korin = math.sqrt(num)
    print(f"Квадратний корінь з {num}: {korin}")
else:
    print("Квадратний корінь з від'ємного числа не визначений!")