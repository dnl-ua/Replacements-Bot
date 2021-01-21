# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм. <br />
Бот в телеграм [@cctereplbot](https://t.me/cctereplbot)

# Автоматизация
Я создал [cron](crontab.guru/crontab.5.html) файл который будет запускать `download_image.py` каждый день (кроме субботы) в 12:30, а после этого, в 12:35, он запустит `send_to_channel.py` что отправит замены в канал. Команда выглядит приблезительно так: <br />
`0 13 * * 0-5 /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для `download_python.py` <br />
`5 13 * * 0-5 /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для `send_to_channel.py` <br />

На Windows это можно реализовать через Диспетчер Задач.
