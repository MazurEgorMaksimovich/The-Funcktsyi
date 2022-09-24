def plus_minus(s):

    """Возвращает два списка чисел: отсортировынные по убыванию отрицательные и возрастанию неотрицательные.
    - Параметры:
        - List[int]: список чисел
    - Вернуть:
        - 'отсортированные неотрицательные '\n' отсортированные отрицательные' (str): отсортировынные по убыванию отрицательные и возрастанию неотрицательные
    """

    plus = []
    minus = []
    strplus = ''
    strminus = ''
    
    while s != []:
        if s[0] < 0:
            minus.append(s[0])
        else:
            plus.append(s[0])
        s = s[1::]
    
    plus = sorted(plus)
    for i in range(0, len(minus)):
        minus[i] = -minus[i]
    minus = sorted(minus)
    for i in range(0, len(minus)):
        minus[i] = -minus[i]

    for i in plus:
        strplus = strplus + str(i) + ' '
    for i in minus:
        strminus = strminus + str(i) + ' '
    strvsyo = strplus + '\n' + strminus
    return strvsyo

print(plus_minus([int(s) for s in input().split()]))