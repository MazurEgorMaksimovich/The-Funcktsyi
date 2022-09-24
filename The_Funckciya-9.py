def summa_tsyfr(n):

    """Возвращает сумму цифр числа.
    - Параметры:
        - n(int): число
    - Вернуть:
        - m(int): сумму цифр числа
    """

    n = abs(n)
    if n == 0:
        return 0
    else:
        return summa_tsyfr(n//10) + n%10

def kolich_tsyfr(n):

    """Возвращает количество цифр в числе.
    - Параметры:
        - n(int): число
    - Вернуть:
        - m(int): количество цифр в числе
    """

    n = abs(n)
    if n == 0:
        return 0
    else:
        return kolich_tsyfr(n//10) + 1

n = int(input())
print(summa_tsyfr(n))
print(kolich_tsyfr(n))