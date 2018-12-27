# sem5-2016-packages

## Самостоятельная работа

## Инвариантное задание

1.1 Исследовать функционал одного из модулей стандартной библиотеки (string, re, datetime, math, random, os, и т.д.) и, используя инструмент Jupyter Notebook, создать документ с описанием и примерами использования его функционала. Опубликовать его в портфолио.

Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.

math.ceil(X) – округление до ближайшего большего числа.

math.copysign(X, Y) - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.

math.fabs(X) - модуль X.

math.factorial(X) - факториал числа X.

math.floor(X) - округление вниз.

math.fmod(X, Y) - остаток от деления X на Y.

math.frexp(X) - возвращает мантиссу и экспоненту числа.

math.ldexp(X, I) - X * 2i. Функция, обратная функции math.frexp().

math.fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.

math.isfinite(X) - является ли X числом.

math.isinf(X) - является ли X бесконечностью.

math.isnan(X) - является ли X NaN (Not a Number - не число).

math.modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.

math.trunc(X) - усекает значение X до целого.

math.exp(X) - eX.

math.expm1(X) - eX - 1. При X → 0 точнее, чем math.exp(X)-1.

math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

math.log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).

math.log10(X) - логарифм X по основанию 10.

math.log2(X) - логарифм X по основанию 2. Новое в Python 3.3.

math.pow(X, Y) - XY.

math.sqrt(X) - квадратный корень из X.

math.acos(X) - арккосинус X. В радианах.

math.asin(X) - арксинус X. В радианах.

math.atan(X) - арктангенс X. В радианах.

math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).

math.cos(X) - косинус X (X указывается в радианах).

math.sin(X) - синус X (X указывается в радианах).

math.tan(X) - тангенс X (X указывается в радианах).

math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).

math.degrees(X) - конвертирует радианы в градусы.

math.radians(X) - конвертирует градусы в радианы.

math.cosh(X) - вычисляет гиперболический косинус.

math.sinh(X) - вычисляет гиперболический синус.

math.tanh(X) - вычисляет гиперболический тангенс.

math.acosh(X) - вычисляет обратный гиперболический косинус.

math.asinh(X) - вычисляет обратный гиперболический синус.

math.atanh(X) - вычисляет обратный гиперболический тангенс.

math.erf(X) - функция ошибок.

math.erfc(X) - дополнительная функция ошибок (1 - math.erf(X)).

math.gamma(X) - гамма-функция X.

math.lgamma(X) - натуральный логарифм гамма-функции X.

math.pi - pi = 3,1415926...

math.e - e = 2,718281...

Примеры применения функций этого модуля:

Для работы с данным модулем его предварительно нужно импортировать.

```python
import math
```
Рассмотрим наиболее часто используемые функции.

##### math.ceil(x)

Возвращает ближайшее целое число большее, чем x.

```python
math.ceil(3.2)
4
```

##### math.fabs(x)

Возвращает абсолютное значение числа.

```python
math.fabs(-7)
7.0
```

##### math.factorial(x)

Вычисляет факториал x.

```python
math.factorial(5)
120
```

##### math.floor(x)

Возвращает ближайшее целое число меньшее, чем x.

```python
math.floor(3.2)
3
```

##### math.exp(x)

Вычисляет e**x.

```python
math.exp(3)
20.085536923187668
```

##### math.log(x[, base])

По умолчанию вычисляет логарифм по основанию e, дополнительно можно указать основание логарифма.

```python
>>> math.log2(8)
3.0
>>> math.log10(1000)
3.0
>>> math.log(5)
1.6094379124341003
>>> math.log(4, 8)
0.6666666666666667
```

##### math.pow(x, y)

Вычисляет значение x в степени y.

```python
math.pow(3, 4)
81.0
```

##### math.sqrt(x)

Корень квадратный от x.

```python
math.sqrt(25)
5.0
```

1.2 Создание пользовательского пакета для приложения «Гостевая книга» («Регистрация на конференцию») с прототипами методов, позволяющих взаимодействовать с JSON-файлом (создание, удаление, переименование, чтение, запись). Формирование отчета по практическому заданию и публикация его в портфолио.

```python
class GuestBook():

    def __init__(self):
        self.guests = list()


    def add(self, name, surname, age, country): #добавляем человечка с нужными нам параметрами(имя,фамилия,возраст,страна)
        self.guests.append({"guests_name": name,"guests_surname": surname, "guests_age": age, "guests_country": country})
    
    def udal(self, name): #тут удаляем человечка по нужному нам параметру, в данном случае у нас страна
        for guests in self.guests:
            if guests.get("guests_country") == country: 
                self.guests.remove(guests) 

    def zapis(self): #записываем всё в файлик
        import json
        with open("file1.json", 'a') as file:
            json_data = { "Guests": self.guests }
            file.write(json.dumps(json_data, indent=4))
            
if __name__ == "__main__":
    GuestBook = GuestBook()
    GuestBook.add("Ksenia", "Selivanova", 20, "ms.ksus@gmail.com")
    GuestBook.add("Ktoto", "Esho", 25, "ktoto@gmail.com")
    
    GuestBook.zapis()
```
![alt](https://github.com/herzenuni/sem5-2016-packages-KsushaSeliv/blob/master/SamRab/invar/14.JPG)

## Вариативное задание

Pandas – это библиотека, которая предоставляет очень удобные с точки зрения использования инструменты для хранения данных и работе с ними. Если вы занимаетесь анализом данных или машинным обучением и при этом используете язык Python, то вы просто обязаны знать и уметь работать с pandas.

Чтобы эффективно работать с pandas, необходимо освоить самые главные структуры данных библиотеки: DataFrame и Series. 

Структура/объект 
##### Series
представляет из себя объект, похожий на одномерный массив (питоновский список, например), но отличительной его чертой является наличие ассоциированных меток, т.н. индексов, вдоль каждого элемента из списка. Такая особенность превращает его в ассоциативный массив или словарь в Python.

```python
>>> import pandas as pd
>>> my_series = pd.Series([5, 6, 7, 8, 9, 10])
>>> my_series
0     5
1     6
2     7
3     8
4     9
5    10
dtype: int64
```

В строковом представлении объекта Series, индекс находится слева, а сам элемент справа. Если индекс явно не задан, то pandas автоматически создаёт RangeIndex от 0 до N-1, где N общее количество элементов. Также стоит обратить, что у Series есть тип хранимых элементов, в нашем случае это int64, т.к. мы передали целочисленные значения.

У объекта Series есть атрибуты через которые можно получить список элементов и индексы, это values и index соответственно.

```python
>>> my_series.index
RangeIndex(start=0, stop=6, step=1)
>>> my_series.values
array([ 5,  6,  7,  8,  9, 10], dtype=int64) 
```

Доступ к элементам объекта Series возможны по их индексу (вспоминается аналогия со словарем и доступом по ключу).

```python
>>> my_series[4]
9
```

Индексы можно задавать явно:

```python
>>> my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
>>> my_series2['f']
10
```

Делать выборку по нескольким индексам и осуществлять групповое присваивание:

```python
>>> my_series2[['a', 'b', 'f']]
a     5
b     6
f    10
dtype: int64
>>> my_series2[['a', 'b', 'f']] = 0
>>> my_series2
a    0
b    0
c    7
d    8
e    9
f    0
dtype: int64
```

Фильтровать Series как душе заблагорассудится, а также применять математические операции и многое другое:

```python
>>> my_series2[my_series2 > 0]
c    7
d    8
e    9
dtype: int64
>>> my_series2[my_series2 > 0] * 2
c    14
d    16
e    18
dtype: int64
```

Если Series напоминает нам словарь, где ключом является индекс, а значением сам элемент, то можно сделать так:

```python
>>> my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
>>> my_series3
a    5
b    6
c    7
d    8
dtype: int64
>>> 'd' in my_series3
True
```

У объекта Series и его индекса есть атрибут name, задающий имя объекту и индексу соответственно.

```python
>>> my_series3.name = 'numbers'
>>> my_series3.index.name = 'letters'
>>> my_series3
letters
a    5
b    6
c    7
d    8
Name: numbers, dtype: int64
```

Индекс можно поменять "на лету", присвоив список атрибуту index объекта Series

```python
>>> my_series3.index = ['A', 'B', 'C', 'D']
>>> my_series3
A    5
B    6
C    7
D    8
Name: numbers, dtype: int64
```

Имейте в виду, что список с индексами по длине должен совпадать с количеством элементов в Series.


##### DataFrame.

Объект DataFrame лучше всего представлять себе в виде обычной таблицы и это правильно, ведь DataFrame является табличной структурой данных. В любой таблице всегда присутствуют строки и столбцы. Столбцами в объекте DataFrame выступают объекты Series, строки которых являются их непосредственными элементами.

DataFrame проще всего сконструировать на примере питоновского словаря:

```python
>>> df = pd.DataFrame({
...     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
...     'population': [17.04, 143.5, 9.5, 45.5],
...     'square': [2724902, 17125191, 207600, 603628]
... })
>>> df
   country  population    square
0  Kazakhstan       17.04   2724902
1      Russia      143.50  17125191
2     Belarus        9.50    207600
3     Ukraine       45.50    603628
```

Чтобы убедиться, что столбец в DataFrame это Series, извлекаем любой:

```python
>>> df['country']
0    Kazakhstan
1        Russia
2       Belarus
3       Ukraine
Name: country, dtype: object
>>> type(df['country'])
<class 'pandas.core.series.Series'>
```

Объект DataFrame имеет 2 индекса: по строкам и по столбцам. Если индекс по строкам явно не задан (например, колонка по которой нужно их строить), то pandas задаёт целочисленный индекс RangeIndex от 0 до N-1, где N это количество строк в таблице.

```python
>>> df.columns
Index([u'country', u'population', u'square'], dtype='object')
>>> df.index
RangeIndex(start=0, stop=4, step=1)
```

В таблице у нас 4 элемента от 0 до 3. 

Индекс по строкам можно задать разными способами, например, при формировании самого объекта DataFrame или "на лету":

```python
>>> df = pd.DataFrame({
...     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
...     'population': [17.04, 143.5, 9.5, 45.5],
...     'square': [2724902, 17125191, 207600, 603628]
... }, index=['KZ', 'RU', 'BY', 'UA'])
>>> df
       country  population    square
KZ  Kazakhstan       17.04   2724902
RU      Russia      143.50  17125191
BY     Belarus        9.50    207600
UA     Ukraine       45.50    603628
>>> df.index = ['KZ', 'RU', 'BY', 'UA']
>>> df.index.name = 'Country Code'
>>> df
                 country  population    square
Country Code                                  
KZ            Kazakhstan       17.04   2724902
RU                Russia      143.50  17125191
BY               Belarus        9.50    207600
UA               Ukraine       45.50    603628
```

Как видно, индексу было задано имя - Country Code. Отмечу, что объекты Series из DataFrame будут иметь те же индексы, что и объект DataFrame:

```python
>>> df['country']
Country Code
KZ    Kazakhstan
RU        Russia
BY       Belarus
UA       Ukraine
Name: country, dtype: object
```

Доступ к строкам по индексу возможен несколькими способами:

.loc - используется для доступа по строковой метке
.iloc - используется для доступа по числовому значению (начиная от 0)

```python
>>> df.loc['KZ']
country       Kazakhstan
population         17.04
square           2724902
Name: KZ, dtype: object
>>> df.iloc[0]
country       Kazakhstan
population         17.04
square           2724902
Name: KZ, dtype: object
```

Можно делать выборку по индексу и интересующим колонкам:

```python
>>> df.loc[['KZ', 'RU'], 'population']
Country Code
KZ     17.04
RU    143.50
Name: population, dtype: float64
```

Как можно заметить, .loc в квадратных скобках принимает 2 аргумента: интересующий индекс, в том числе поддерживается слайсинг и колонки.

```python
>>> df.loc['KZ':'BY', :]
                 country  population    square
Country Code                                  
KZ            Kazakhstan       17.04   2724902
RU                Russia      143.50  17125191
BY               Belarus        9.50    207600
```

Фильтровать DataFrame с помощью т.н. булевых массивов:

```python
>>> df[df.population > 10][['country', 'square']]
                 country    square
Country Code                      
KZ            Kazakhstan   2724902
RU                Russia  17125191
UA               Ukraine    603628
```

Кстати, к столбцам можно обращаться, используя атрибут или нотацию словарей Python, т.е. df.population и df['population'] это одно и то же.

Сбросить индексы можно вот так:

```python
>>> df.reset_index()
  Country Code     country  population    square
0           KZ  Kazakhstan       17.04   2724902
1           RU      Russia      143.50  17125191
2           BY     Belarus        9.50    207600
3           UA     Ukraine       45.50    603628
```

pandas при операциях над DataFrame, возвращает новый объект DataFrame.

Добавим новый столбец, в котором население (в миллионах) поделим на площадь страны, получив тем самым плотность:

```python
>>> df['density'] = df['population'] / df['square'] * 1000000
>>> df
                 country  population    square    density
Country Code                                             
KZ            Kazakhstan       17.04   2724902   6.253436
RU                Russia      143.50  17125191   8.379469
BY               Belarus        9.50    207600  45.761079
UA               Ukraine       45.50    603628  75.377550
```

Не нравится новый столбец? Не проблема, удалим его:

```python
>>> df.drop(['density'], axis='columns')
                 country  population    square
Country Code                                  
KZ            Kazakhstan       17.04   2724902
RU                Russia      143.50  17125191
BY               Belarus        9.50    207600
UA               Ukraine       45.50    603628
```

Особо ленивые могут просто написать del df['density'].

Переименовывать столбцы нужно через метод rename:

```python
>>> df = df.rename(columns={'Country Code': 'country_code'})
>>> df
  country_code     country  population    square
0           KZ  Kazakhstan       17.04   2724902
1           RU      Russia      143.50  17125191
2           BY     Belarus        9.50    207600
3           UA     Ukraine       45.50    603628
```

В этом примере перед тем как переименовать столбец Country Code, убедитесь, что с него сброшен индекс, иначе не будет никакого эффекта.

Эта заметка демонстрирует лишь малую часть возможностей pandas. 
