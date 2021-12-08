Tris is geometry package from exc of open education 
course fall 2021.
Используется добавление методов, перегрузка операторов. Собрано в пакет.

Задача

Дан шаблон с классами Point, Line, Triangle.

Задание 1. Преобразовать файл, который хранит весь код, в пакет "geometry", который обеспечит следующий интерфейс доступа к классам и их методам:

1.1 Доступ к точке

from geometry.point import *

point1 = Point(0, 0)

1.2 Доступ к линии

from geometry.figures.line import *

point1 = Point(0, 0)

point2 = Point(0, 1)

my_line = Line(point1, point2)

1.3 Доступ к треугольнику

from geometry.figures.triangle import *

point1 = Point(0, 0)

point2 = Point(0, 1)

point3 = Point(1, 0)

my_triangle = Triangle(point1, point2, point3)

1.4 Также будет проверено наличие файлов "__init__.py" там где это необходимо.

Всего за задание 1 можно, соответственно получить 4 балла

Задание 2. Дописать реализацию методов:

2.1 Метода "length" класса "Line"

Проверка может происходить следующим образом

from geometry.figures.line import *

point1 = Point(0, 0)

point2 = Point(0, 1)

my_line = Line(point1, point2)

print(my_line.length())

Для данного примера ожидается вывод "1.0"

2.2 Метода "perimeter" класса "Triangle"

Проверка может происходить следующим образом

from geometry.figures.triangle import *

point1 = Point(0, 0)

point2 = Point(0, 1)

point3 = Point(1, 0)

my_triangle = Triangle(point1, point2, point3)

print(my_triangle.perimeter())

Для данного примера ожидается вывод "3.4142". Округляйте ваш ответ до 4-х знаков после запятой.

2.3 Метода "square" класса "Triangle"

Проверка может происходить следующим образом

from geometry.figures.triangle import *

point1 = Point(0, 0)

point2 = Point(0, 1)

point3 = Point(1, 0)

my_triangle = Triangle(point1, point2, point3)

print(my_triangle.square())

Для данного примера ожидается вывод "0.5". Округляйте ваш ответ до 4-х знаков после запятой.

Всего за задание 2 можно, соответственно получить 3 балла

Решение нужно запаковать архиватором zip
