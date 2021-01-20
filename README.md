# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм. <br />
Бот в телеграм [@cctereplbot](https://t.me/cctereplbot)

# Автоматизация
Я создал [cron](https://crontab.guru/crontab.5.html) файл который будет запускать download_image.py каждый день в 13:00. Команда выглядит приблезительно так: <br />
`0 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
На Windows это можно реализовать через Диспетчер Задач.
