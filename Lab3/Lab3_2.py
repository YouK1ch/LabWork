a = input("Введіть число для перетворення на ціле: ")
    
try:
       
    integer_value = int(a)
    print(f"Перетворене число: {integer_value}")
    
except ValueError:
    print("Помилка: введено некоректне значення. Будь ласка, введіть ціле число.")
