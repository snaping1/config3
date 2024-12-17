# **TOML Converter**  

Этот проект предназначен для обработки TOML-файлов, включающих комментарии и константы, и их преобразования в пользовательский конфигурационный формат.  

## **Особенности**
- Поддержка констант, которые автоматически заменяются на их значения.
- Обработка и сохранение комментариев в исходных данных.
- Преобразование TOML-файлов в пользовательский формат с удобным для чтения синтаксисом.
- Гибкость и возможность кастомизации.  

## **Структура проекта**
- **`constants.py`**  
  Модуль для управления константами:
  - Объявление новых констант.
  - Рекурсивная замена ссылок на константы в структуре данных.  

- **`converter.py`**  
  Модуль для преобразования TOML-данных:
  - Замена констант в строках.
  - Генерация пользовательского конфигурационного формата с сохранением комментариев.

- **`parser.py`**  
  Пользовательский парсер TOML:
  - Парсинг TOML-данных.
  - Извлечение комментариев.
  - Определение констант.

- **`main.py`**  
  Основной скрипт:
  - Чтение TOML-данных из ввода.
  - Обработка данных с использованием модулей.
  - Сохранение результата в указанный файл.

## **Установка**
1. Клонируйте репозиторий:  
   ```bash
   git clone <URL репозитория>
   cd <папка проекта>
   ```
2. Убедитесь, что установлен Python версии 3.8 или выше.  
3. Установите зависимости, если они указаны:  
   ```bash
   pip install -r requirements.txt
   ```

## **Использование**
1. Запустите скрипт `main.py`:  
   ```bash
   python main.py <имя выходного файла>
   ```
2. Введите данные TOML в консоль. Завершите ввод пустой строкой.  
3. Результат будет сохранен в указанном файле.

1-ый Пример входных данных TOML:  
```toml
[constants]
app_name = "MyApp" # Имя приложения
version = "1.0.0" # Версия приложения

[settings]
# Основные настройки
theme = "dark" # Тема оформления
timeout = 30 # Таймаут в секундах
description = "$app_name$ v$version$" # Использование констант
gg = [1,2,3,4]

```

Пример результата в пользовательском формате:  
```plaintext
constants = dict(
    app_name = MyApp,
    version = 1.0
)

settings = dict(
    app_name = MyApp : Имя приложения,
    version = 1.0 : Версия приложения
)
```

2-ой Пример входных данных TOML:  
```toml
[constants]
name = "Daniil"
surname = "Titov"
city="Moscow

[Person]
person_age = 18
person_name = "$name$"
person_surname = "$surname$"

[Adress]
living_in= "Russia"
city_contry="$city$"
```

Пример результата в пользовательском формате:  
```plaintext
Person = dict(
    person_age = 18
    person_name = "Daniil"
    person_surname = "Titov"
)
Adress = dict(
    living_in = "Russia"
    city_contry = "Moscow"
)
```

## **Тестирование**
Для проверки функционала используйте `pytest`. Тесты находятся в директории `tests`.  
Запустите тесты командой:  
```bash
pytest
```

![Тесты](https://i.imgur.com/caKZ4HW.png)