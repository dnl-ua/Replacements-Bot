# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм. <br />
Бот в телеграм: [@cctereplbot](https://t.me/cctereplbot) <br />
Канал в телеграм: [@ccterepls](https://t.me/ccterepls)

# Установка
Зависимости: [python](https://command-not-found.com/python), [cron](https://command-not-found.com/crontab) (опционально). <br />
Библиотеки:  [aiogram](https://pypi.org/project/aiogram/), [urllib3](https://pypi.org/project/urllib3/)

```bash
git clone https://github.com/kagarlytskiy/cctereplbot
cd cctereplbot
python bot.py # или python3 bot.py
``` 
Перед тем как запустить бота нужно написать `config.py`. Вот какие параметры необходимо составить: <br />
```python
TOKEN =      # токен (в виде строки)
URL =        # url картинки с сайти
IMAGE_PATH = # путь к дириктории (папке) со скаченым изображением 
CHANNEL_ID = # id канала в который будет отсылаться изображение
```
<br />

# Автоматизация
Я создал [cron](https://crontab.guru/crontab.5.html) файл который будет запускать [download_image.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/download_image.py) каждый день (кроме субботы и пятницы) в 12:30, а после этого, в 12:35, он запустит [send_to_channel.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/send_to_channel.py) что отправит замены в канал. Команды которые нужно записать в `crontab -e` выглядят приблезительно так: <br />

`30 12 * * 0-4 /PATH/TO/PYTHON/BINARY /PATH/TO/download_image.py` <br />
для [download_image.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/download_image.py) <br />
`35 12 * * 0-4 /PATH/TO/PYTHON/BINARY /PATH/TO/send_to_channel.py` <br />
для [send_to_channel.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/send_to_channel.py) <br />

На Windows это можно реализовать через Диспетчер Задач. <br />
