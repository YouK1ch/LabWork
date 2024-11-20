def average(numbers):
    if not numbers:  
        return 0
    
    total = sum(numbers)  
    count = len(numbers)  
    return total / count 

   
a = input("Введіть числа через пробіл: ")
number_list = list(map(float, a.split())) 
    
result = average(number_list) 
print(f"Середнє значення: {result}")



