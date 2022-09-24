def vybory_vybory(a):

    """Возвращает результаты совершенно некорумпированных выборов.
    - Параметры:
        - List[int]: список голосов
    - Вернуть:
        - 'Партия | количество проголосовавших | процент от всех голосов' (str): результаты совершенно некорумпированных выборов
    """
    
    A = {}
    for i in a:
        A[i] = A.get(i, 0) + 1
    w = []
    for i, j in sorted(A.items()):
        w.append((-j, i))
    k = []
    for j, i in sorted(w):
        if i != '-1':
            s = 'Партия №' + str(i) + '        '
        else:
            s = 'Испорченые бланки'
        k.append(s + ' | ' + str(-j) + ' | ' + str(-j*(100 / len(a))))
    return k

m = vybory_vybory(input().split())
for _ in m:
    print(_)