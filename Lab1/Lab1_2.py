a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
    
    
if b != 0:
    zalysh = a % b
    print(f"Залишок від ділення {a} на {b}: {zalysh}")
else:
    print("На нуль ділити не можна!")