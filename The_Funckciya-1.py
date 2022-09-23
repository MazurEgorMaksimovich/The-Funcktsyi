def get_lucky_tickets(a, b):
    """Возвращает количество счастливых билетов (кол. чётных цифр = кол. нечётных чисел)
    Параметры:
        - а, b (int): ограничения списка
    Вернуть:
        - List[int]: счасливые билеты от а до b
    """
    lucky_tickets = []
    for i in range(a, b+1):
        digits = 0
        number = i
        while number > 0:
            if number % 10 % 2 == 0:
                digits += 1
            number //= 10
        if 2 * digits == len(str(i)):
            lucky_tickets.append(i)
    return lucky_tickets

a, b = map(int, input().split())
print(*get_lucky_tickets(a, b))