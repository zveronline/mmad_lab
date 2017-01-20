import numpy as np
import math


# классификация методом k ближайших соседей
# X - обучающее множество.
#   Строки соответствуют объектам,
#   столбцы - признакам.
#   Последний столбец - номер класса
# k - количество ближайших соседей (не более числа объектов в X)
# obj - объект, который нужно классифицировать
def k_nearest(X, k, obj):

    # TODO: выполнить нормализацию каждого столбца (кроме последнего)
    #       матрицы X, пользуясь формулой с практики по k-means. Для этого удобно
    # сохранить часть матрицы X без последнего столбца в матрицу sub_X
    # Пример выбора всех столбцов, кроме последнего:
    # >>> a = np.arange(1, 7).reshape([2, 3])
    # >>> a
    # array([[1, 2, 3],
    #        [4, 5, 6]])
    # >>> a[:, 0:-1]    # <- первое двоеточие значит, что берём все строки, а запись 0:-1 - берём столбцы от самого первого (с индексом 0) до предпоследнего
    # array([[1, 2],
    #        [4, 5]])
    sub_X = X[:, 0:-1]
    m = np.mean(sub_X, axis=0)
    s = np.std(sub_X, axis=0)
    norm_X = (sub_X - m) / s
    # TODO: зная параметры среднего и среднеквадратического отклонения
    #       по каждому столбцу sub_X, выполнить нормализацию объекта obj
    norm_obj = (obj - m) / s
    # TODO: рассчитать евклидово расстояние от obj до каждого объекта sub_X (функция dist ниже).
    # Реализовать можно с помощью цикла for. Существуют разные варианты записи этого цикла, например, такой:
    # Пример реализации цикла for на Python. Здесь возводится в квадрат каждый элемент массива a
    # >>> a = np.array([1, 2, 3])
    # >>> b = [pow(i, 2) for i in a]
    # >>> b
    # [1, 4, 9]
    rast = [dist(norm_obj, i) for i in norm_X]
    # TODO: Получить с помощью функции np.argsort индексы соседей по мере их удаления от obj.
    # Для справки по функции argsort выполните в консоли Python команду help('numpy.argsort')
    # Пример вызова функции argsort:
    # >>> a = np.array([3, 2, 5])
    # >>> np.argsort(a)
    # array([1, 0, 2], dtype=int64)     # минимальный элемент 2 с индексом 1 в массиве a, затем 3 с индексом 0 и в конце 5 с индексом 2.
    sosed = np.argsort(rast)
    # TODO: выбрать в отдельный вектор классы k ближайших соседей
    # Нужно взять k строк из матрицы X, соответствующих ближайшим соседям.
    # Индексы строк ближайших соседей были получены на предыдущем шаге.
    # Из этих строк нас интересует только последнее значение (последний столбец матрицы X),
    # так как там хранится класс объекта. Пример выбора из матрицы строк по заданным индексам и последнего столбца:
    # >>> a = np.arange(1, 10).reshape([3, 3])  # создание матрицы 3*3
    # >>> a
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])
    # >>> a[[0, 2], -1]     # взяли первую и третью строки (индексы 0 и 2 соответственно), и в них последнее значение. Это будут значения 3 и 9.
    # array([3, 9])
    nearest_classes = X[sosed[0:k], 2]
    # TODO: определить наиболее часто встречающийся класс в этом векторе. Просто раскомментируйте код ниже:
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]

    # TODO: вернуть полученное значение из функции. Искомый класс объекта obj хранится в переменной object_class
    # return ...
    return object_class

# вычисление евклидова расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))
