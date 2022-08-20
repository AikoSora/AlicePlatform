<h1 align="center">
AlicePlatform
</h1>
<p align="center">
Асинхронная платформа для создания навыков Алисы.
<br /><br />
<img alt="Python3.8" src="https://img.shields.io/badge/Python-3.8-blue">
<img alt="Sanic22.6.2" src="https://img.shields.io/badge/Sanic-22.6.2-green">
<img alt="SQLAlchemy1.4.40" src="https://img.shields.io/badge/SQLAlchemy-1.4.40-green">
<img alt="Alembic" src="https://img.shields.io/badge/Alembic-1.8.1-green">
</p>

## Установка

Установите зависимости платформы
```shell
pip install -r requirements.txt
```
<br />

Настройте ```settings.py``` файл
- url - Переменная по которой будет доступны post запросы для Алисы
- secretKey - Переменная для проксирования через Ngnix
- host - IP адрес для развертывания сервера Sanic
- port - Port для развертывания сервера Sanic
- debug - Режим разработчика
- appName - Название приложения для сервера Sanic

<br />

После всех настроек следует произвести миграцию моделей
```shell
alembic revision --autogenerate -m "migration name"
alembic upgrade head
```

## Запуск и тестирование навыка
Для тестирования навыка нам потребуется утилита [alice-nearby](https://github.com/azzzak/alice-nearby), в папке bin репозитория утилиты уже есть скомпилированные версии для MacOS и Windows

Запустим платформу командой
```shell
python3 main.py
```
По дефолту навык алисы будет доступен по адресу ```http://127.0.0.1:8000/alice```, зная все эти данные переходим к alice-nearby и начинаем тестирование навыка
```shell
./alice-nearby-macos-amd64 --webhook=http://127.0.0.1:8000/alice --port=3456
```
Теперь перейдя по ```http://localhost:3456/``` мы можем протестировать наш навык!

## Hello World!
Все команды для навыка находятся в папке [/bot/commands](https://github.com/YamioKDL/AlicePlatform/tree/main/bot/commands), в этой папке можно создавать свои py файлы, создадим новый с названием ```hello.py``` и впишем туда следующий код
```python3
from bot import handler

@handler.message(names="Hello")
async def _(msg, database):
    return msg("World!")
```
Переменная ```names``` принимает обьект list или str для инициализации команды и последующим поиском этой или нескольких строк в полученным платформой текстом, т.е. если человек скажет алисе - "Oh, Alice! Hello.", платформа получит этот текст и если есть команды с одним из этих слов или похожими словами в точности до (примерно) 80%, триггер команды сработает и скажет человеку "World!"

<br />

В файле ```default.py``` есть примеры команд, возьмем эту
```python3
@handler.message(names=["Включить", "свет"])
```
переменная ```names``` принимает list обьект (в простонароде массив), если человек что-то скажет Алисе и в этой команде будут эти два слова (включить/свет)
то Алиса ответит, эти слова по отдельности работать не будут (нужно писать отдельные команды)

```python3
return msg("World!")
```
Зачем нам возвращать обьект ```Message``` если можно вернуть просто текст? Попробуйте! Практика и тесты это хороший способ изучить что-либо!
Но функция msg (обьект Message) лишь обертка над json функцией Sanic, по сути мы возвращаем обычный готовый json, это проще, но никто не запрещает вам использовать функции Sanic!

Переменная ```database``` обьект SQLAlchemy, здесь не будут примеры для работы с данной библиотекой, все подобное вы можете найти в оффициальных доках от этой [либы](https://docs.sqlalchemy.org/en/14/#), но все же маленький пример есть в ```default.py```

Все модели создаются в папке [/database/models/](https://github.com/YamioKDL/AlicePlatform/tree/main/database/models).

## Послесловие (и известные проблемы)
- [Развертывание навыка на сервере (требуется SSL)](https://sanic.readthedocs.io/en/v20.12.1/sanic/nginx.html)
- [Настройка навыка в Яндекс Диалогах](https://dialogs.yandex.ru)
- Поиск похожих слов дает осечку в коротких словах, к примеру команда "пока", сработает если человек скажет "ока"
