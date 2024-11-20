a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
    

suma = a + b
rizn = a - b
dobut = a * b
chastka = a / b if b != 0 else "На нуль ділити не можна!"
    

print(f"Сума: {suma}")
print(f"Різниця: {rizn}")
print(f"Добуток: {dobut}")
print(f"Частка: {chastka}")