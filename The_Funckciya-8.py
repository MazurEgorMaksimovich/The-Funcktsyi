def norekurs_stepen(n, m):
    
    """Возвращает число, возведённое в степень.
    - Параметры:
        - n и m (int): число и степень
    - Вернуть:
        - n**m (int): число, возведённое в степень
    """
    
    res = 1
    for _ in range(m):
        res *= n
    return res

def rekurs_stepen(n, m):
    
    """Возвращает число, возведённое в степень с помощью рекурсии.
    - Параметры:
        - n и m (int): число и степень
    - Вернуть:
        - n**m (int): число, возведённое в степень с помощью рекурсии
    """
    
    res = 1
    if m == 0:
        return res
    else:
        return rekurs_stepen(n, m-1) * n

n, m = [int(_) for _ in input().split()]
print(norekurs_stepen(n, m))
print(rekurs_stepen(n, m))