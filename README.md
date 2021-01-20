# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм.
Бот в телеграм @cctereplbot

# Автоматизация
Я создал cron файл который будет запускать download_image.py каждый день в 13:00, а после этого, в 13:05, он запустит send_to_channel.py что отправит замены в канал. Команда выглядит приблезительно так:
`0 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для download_python.py <br />
`5 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для send_to_channel.py <br />

На Windows это можно реализовать через Диспетчер Задач.
