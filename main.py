day = int(input("Введите день (day): "))  # Получаем день
month = int(input("Введите месяц (month): "))  # Получаем месяц
result = "определена как "  # Объявляем конструктор
if 1 <= day <= 31 and month == 3 or 1 <= day <= 30 and month == 4 or 1 <= day <= 31 and month == 5:  # Проверяем
    result += "Весна"  # Изменяем конструктор
elif 1 <= day <= 30 and month == 6 or 1 <= day <= 31 and month == 7 or 1 <= day <= 31 and month == 7: # Проверяем
    result += "Лето" # Изменяем конструктор
elif 1 <= day <= 30 and month == 9 or 1 <= day <= 31 and month == 10 or 1 <= day <= 30 and month == 11: # Проверяем
    result += "Осень" # Изменяем конструктор
elif 1 <= day <= 31 and month == 12 or 31 >= day >= 1 == month or 1 <= day <= 28 and month == 2: # Проверяем
    result += "Зима" # Изменяем конструктор
else: # Если любая из проверок не завершилась успешно
    result = "не " + result + "какой-либо сезон года."  # Обрабатываем исключение, изменяем конструктор
print(f"Введенная дата {result} ")  # Выводим собранную строку.
