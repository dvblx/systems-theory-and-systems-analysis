# Алгоритм Пуро

## Начало работы
### Функция filling_choice
Вызывается перед началом каждого тура. Даёт пользователю выбрать способ ввода исходных данных: вручную либо через файл.

*Требования к оформлению файла*:

Первая строка - исходные объекты. Вводятся в строчку через пробел.

Следующие строки - объекты в порядке ранжирования. Вводятся в строчку через пробел. 
Строка пропускается, если объекты в ней не совпадают с исходными.
### Функция action_choice
Вызывается по завершении каждого тура. Даёт пользователю выбрать одно из двух действий: 
провести следующий тур либо завершить работу программы.
## Методы класса PuroAlgorithm
### Метод one_expert_ranking_filling_manually
Ранжирование объектов вручную. 

Принимает на вход номер эксперта, возвращает список ранжированных исходных объектов.
### Метод forming_ordering_matrix
Формирование матрицы упорядочивания. Принимает на вход список ранжированных объектов, возвращает матрицу упорядочивания.
Также в методе реализован вывод матрицы.
### Метод forming_difference_matrix
Формирование матрицы рассогласований. Принимает на вход список матриц упорядочивания, возвращает матрицу рассогласований.
Для подсчёта рассогласований внутри метода используется другой метод класса - kemeni.
### Метод kemeni
Принимает на вход пару матриц, которые нужно сравнить. Возвращает расстояние между упорядочиваниями. Рассчитывается по следующей формуле:
![](https://studfile.net/html/2706/206/html_PElSIV8XCi.u4wF/img-kAdFmN.png)
### Метод create_relationship_graph
Принимает на вход матрицу рассогласований. В методе вычисляется пороговое значение и строится граф, отображающий согласованность экспертов.
### Метод main
В методе main поочерёдно вызываются методы, в совокупности образующие полный шаг алгоритма.
# Алгоритмы классификации
### Метод division_into_classes
Используется в случае, если координаты классов не даны по условию.

Принимает на вход название txt-файла и количество классов.

*Требования к оформлению файла*: координаты вводятся построчно через пробел. Пример:

10 7 8 3 10

7 8 3 4 40

4 3 4 8 80

Возвращает словарь с парами номер класса: координаты.
### Классы _Class и _Object
Используются для хранения имён и координат классов и объектов.

Обязательные параметры при создании экземпляра класса необходимо указать в скобках имя, затем список координат.
## Начало работы
Для начала работы необходимо создать экземпляр класса ClassificationAlgorithms, 
указав в скобках список классов и список объектов, которые мы хотим классифицировать.
## Классификация по расстояниям 
### Метод distances 
Не принимает на вход никаких параметров, так как работает с полями класса.
Перебираются все пары класс-объект и выводится сообщение о том, к какому/каким классу/классам принадлежит конкретный объект,
Это определяется с помощью расстояния, которое вычисляется в методе distance.
### Метод distance
Принимает на вход экземпляр класса _Classes и экземпляр класс _Objects.
Возвращает расстояние от объекта до центра тяжести класса, рассчитанное по следующей формуле:

![Img](https://habrastorage.org/getpro/habr/post_images/aa4/6e7/d7b/aa46e7d7b544dbaa221a43bb671fb43c.jpg)
### Метод distance_calculation_output
Визуализация вычислений, производимых в методе distance. Принимает на вход те же параметры, ничего не возвращает.

## Классификация по скалярным произведениям
### Метод scalar_products
Не принимает на вход никаких параметров, так как работает с полями класса.
Перебираются все пары класс-объект и выводится сообщение о том, к какому/каким классу/классам принадлежит конкретный объект,
Это определяется с помощью скалярного произведения, которое вычисляется в методе scalar_product.
### Метод scalar_product
Принимает на вход экземпляр класса _Classes и экземпляр класс _Objects.
Возвращает скалярное произведение, рассчитанное по следующей формуле:
![](https://fsd.multiurok.ru/html/2018/04/09/s_5acbbd635478d/img8.jpg)
### Метод scalar_product_calculation_output
Визуализация вычислений, производимых в методе scalar_product. Принимает на вход те же параметры, ничего не возвращает.


## Классификация с использованием корреляционного метода
### Метод correlation_methods
Не принимает на вход никаких параметров, так как работает с полями класса.
Перебираются все пары класс-объект и выводится сообщение о том, к какому/каким классу/классам принадлежит конкретный объект,
Это определяется с помощью ?, которое вычисляется в методе r.
### Метод r
Принимает на вход экземпляр класса _Classes и экземпляр класс _Objects.
Возвращает ?, рассчитанное по следующей формуле:
### Метод r_calculation_output
Визуализация вычислений, производимых в методе r. Принимает на вход те же параметры, ничего не возвращает.
### Метод main
В методе main поочерёдно вызываются методы классификации, реализованные в классе.