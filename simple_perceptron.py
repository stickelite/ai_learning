import numpy as np
import matplotlib.pyplot as plt

N = 6 # кол-во образов для обоих классов
x1=np.random.random(N) # генерируем массив случайных чисел от 0 до 1 размерности N
x2 = x1+[np.random.randint(10)/10 for i in range(N)] # x1 + случайное отклонение = x2 - просто рандомный генератор чисел, х1 х2 - всегда разные
C1 = [x1,x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10)/10 for i in range(N)] - 0.1
'''
Во втором классе минусы т.к. в теоретической части было определено, что с такой функцией активации и двумя входными сигналами
мы получаем следующую систему (x1*w1+x2*w2 >= 0 -> C1)(x1*w1+x2*w2 < 0 -> C2), тогда порогом будет следующее уравнение:
x1*w1+x2*w2 = 0  --> x2 = -(w1/w2) * x1 - это линейная функция y=kx --> рассмотрим пример разделяющей прямой или разделяющей гиперплоскости
это прямая проходящая через (0,0) координату, под углом 45 градусов --> чтобы один из классов был явно "ниже" на графике, ставятся минусы во
второй переменной x2. 
'''
C2 = [x1,x2]


f=[0,1] # сама разделяющая гиперплоскость/прямая

# т.к. у нас угол 45 градусов, веса должны быть одинаковы, но с противоположными знаками т.к. они определяют угловой коэф.
w = np.array([-1,1])
for i in range(N):
    x = np.array([C1[0][i],C1[1][i]]) # смотрим все образы выборки, у нас это двумерная матрица
    #тут указываем опционально, если указали C1, то ожидаем, что нейронная сеть определит точки в C1
    y = np.dot(w,x) # тут вычисляем скалярное произведение массивов, то-есть x1 * w1 + x2 * w2
    if y>=0:
        print("Класс C1")
    else:
        print("Класс C2")


plt.scatter(C1[0][:], C1[1][:], s = 30, c ='red', label='C1') # s - размер точки, [:] - все значения массива
plt.scatter(C2[0][:], C2[1][:], s = 30, c = 'blue', label='C2')
plt.plot(f) # строим график по функции
plt.grid(True) # размерная сетка
plt.legend()
plt.show() #отображаем график
