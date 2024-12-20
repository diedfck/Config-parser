## Программа обработки конфигураций и вычисления выражений

Эта программа обрабатывает текстовый файл конфигурации, интерпретирует выражения в формате постфиксной
нотации (Reverse Polish Notation, RPN) и преобразует их в выходной файл формата TOML.

## Описание работы

**Входные данные:**
Файл конфигурации в формате input.txt.
В файле могут быть указаны переменные, массивы, строковые значения и арифметические выражения такие как:

Сложение 
вычитание
умножение 
ord() - вывод код буквы по таблцие ASCI 
pow() - возведение в степень


**Выходные данные:**
Файл output.toml, содержащий обработанные данные из входного файла.

**Поддерживаемые выражения:**
Арифметические операции: +, -, *.
Операция A X pow для возведения в степень.
Операция char ord для получения ASCII-кода символа.

Все арифметические операции выполняются для постфиксной формы выражения

**Особенности:**
Поддерживаются массивы и строковые значения.
Обрабатываются ошибки, связанные с некорректными операндами или выражениями.

**Работа программы:**

![Alt text](https://github.com/diedfck/config-parser/blob/main/1.PNG)
![Alt text](https://github.com/diedfck/config-parser/blob/main/2.PNG)
