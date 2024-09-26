date_string = str(input('Введите дату формата "DD.MM", с которой необходимо провести анализ (date): '))  # Получаем дату
result = "определена как"  # Подготавливаем результат
if date_string.find('.') == 0:
    pass
else:
    date_date = date_string.split(".")  # Получаем массив, состоящий из дня и месяца
    date_int = int(date_date[1])  # Превращаем месяц в число
    if date_int == 1 or date_int == 2 or date_int == 12:  # Определяем время года
        date_string = "Зима"
    elif 3 <= date_int <= 5:
        date_string = "Весна"
    elif 6 <= date_int <= 8:
        date_string = "Лето"
    elif 9 <= date_int <= 11:
        date_string = "Осень"
    else:
        date_string = "Возникло исключение."  # Обработка исключения
        result = f"не {result} какое-либо время года."
print(f"Указанная дата {result} {date_string}")  # Выводим результат
