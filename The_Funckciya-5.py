def liberty_kupes(w):

    """Возвращает список свободных купе в вагоне.
    - Параметры:
        - List[dict]: список купе в вагонах
    - Вернуть:
        - List[dict]: список свободных купе в вагоне
    """

    n = []
    for i in w:
        m = 0
        for j in i.values():
            if j == 'None':
                m += 1
        if m == 4:
            n.append(i)
    return n

def liberty_places(w):

    """Возвращает список свободных мест в вагоне.
    - Параметры:
        - List[dict]: список купе в вагонах
    - Вернуть:
        - List[str]: список свободных мест в вагоне
    """

    n = ''
    for i in w:
        for j, l in i.items():
            if l == 'None':
                n = n + str(j) + ', '
    return 'Свободные места:' + n

def liberty_places_vverkh_vniz(w):

    """Возвращает список свободных верхних и нижних мест в вагоне.
    - Параметры:
        - List[dict]: список купе в вагонах
    - Вернуть:
        - (str): список свободных верхних и нижних мест в вагоне
    """

    n = ''
    m = ''
    for i in w:
        for j, l in i.items():
            if l == 'None':
                if j % 2 == 0:
                    n = n + str(j) + ', '
                else:
                    m = m + str(j) + ', '
                
    return 'Нижние места: ' + str(m) + 'Верхние места: ' + str(n)

def liberty_places_muzhyki(w):

    """Возвращает список свободных мест в купе с исключительно мужской компанией в купе в вагоне.
    - Параметры:
        - List[dict]: список купе в вагонах
    - Вернуть:
        - (str): список свободных мест в купе с исключительно мужской компанией в купе в вагоне
    """

    n = ''
    for i in w:
        m = i.values()
        if 'м' in m and 'ж' not in m:
            for j, l in i.items():
                if l == 'None':
                    n = n + str(j) + ', '
                
    return 'Свободные места в мужских купе: ' + n

def liberty_places_women(w):

    """Возвращает список свободных мест в купе с исключительно женской компанией в купе в вагоне.
    - Параметры:
        - List[dict]: список купе в вагонах
    - Вернуть:
        - (str): список свободных мест в купе с исключительно женской компанией в купе в вагоне
    """

    n = ''
    for i in w:
        m = i.values()
        if 'ж' in m and 'м' not in m:
            for j, l in i.items():
                if l == 'None':
                    n = n + str(j) + ', '
                
    return 'Свободные места в женских купе: ' + n

a = [_ for _ in input().split()]
A = {}
w =[]
n = 1

for i in range(0, len(a)//4):
    for j in range(4):
        A[n] = a[j]
        n += 1
    w.append(A)
    a = a[4::]
    A = {}

print(*liberty_kupes(w))
print(liberty_places(w))
print(liberty_places_vverkh_vniz(w))
print(liberty_places_muzhyki(w))
print(liberty_places_women(w))