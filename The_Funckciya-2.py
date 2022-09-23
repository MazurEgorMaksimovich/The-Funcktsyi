def yest_day(date, month, year):

    """Возвращает вчерашнюю дату
    - Параметры:
        - date (int): сегодняшняя дата
        - month (int): сегодняшний месяц
        - year (int): сегодняшний год
    - Вернуть:
        - 'День'.'Месяц'.'Год' (str): вчершняя дата
    """
    
    yest_date = date
    yest_month = month
    yest_year = year
    month30 = [4, 6, 9, 11]
    month31 = [1, 3, 5, 7, 8, 10, 12]
    monthFebr = [2]

    if date != 1:
        yest_date = date - 1
    else:
        if month != 1:
            yest_month = month - 1
        else:
            yest_month = 12
            yest_year = year - 1
        if month-1 in month30:
            yest_date = 30
        elif month-1 in month31:
            yest_date = 31
        elif month-1 in monthFebr:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                yest_date = 29
            else:
                yest_date = 28
    return(str(yest_date) + '.' + str(yest_month) + '.' + str(yest_year))


def tomorr_day(date, month, year):

    """Возвращает завтрашнюю дату
    - Параметры:
        - date (int): сегодняшняя дата
        - month (int): сегодняшний месяц
        - year (int): сегодняшний год
    - Вернуть:
        - 'День'.'Месяц'.'Год' (str): завтрашнюю дата
    """

    tomorr_date = date
    tomorr_month = month
    tomorr_year = year
    month30 = [4, 6, 9, 11]
    month31 = [1, 3, 5, 7, 8, 10, 12]
    monthFebr = [2]

    if month in month30:
        last_day = 30
    elif month in month31:
        last_day = 31
    elif month in monthFebr:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                last_day = 29
        else:
            last_day = 28

    if date != last_day:
        tomorr_date = date + 1
    else:
        if month != 12:
            tomorr_month = month + 1
        else:
            tomorr_month = 1
            tomorr_year = year + 1
        tomorr_date = 1
    return(str(tomorr_date) + '.' + str(tomorr_month) + '.' + str(tomorr_year))


date, month, year = map(int, input().split())
print(yest_day(date, month, year))
print(tomorr_day(date, month, year))