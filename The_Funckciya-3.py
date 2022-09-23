def sortisator(s):

    """Возвращает статистику употребления символов в данном высказывании.
    - Параметры:
        - s (str): высказывание
    - Вернуть:
        - 'символ = количество повторений' (str): статистика употребления символов в данном высказывании
    """
    
    A = {}
    s = s.lower()
    for i in s:
        A[i] = A.get(i, 0) + 1
    w = []
    for i, j in sorted(A.items()):
        w.append((j, i))
    k = []
    for j, i in sorted(w):
        k.append(str(i) + ' = ' + str(j))
    return k

m = sortisator(input())
for _ in m:
    print(_)