# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм. <br />
Бот в телеграм [@cctereplbot](https://t.me/cctereplbot)

# Автоматизация
<<<<<<< HEAD
Я создал cron файл который будет запускать download_image.py каждый день в 13:00, а после этого, в 13:05, он запустит send_to_channel.py что отправит замены в канал. Команда выглядит приблезительно так:
`0 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для download_python.py <br />
`5 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для send_to_channel.py <br />

=======
Я создал [cron](https://crontab.guru/crontab.5.html) файл который будет запускать [download_image.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/download_image.py) каждый день в 13:00. Команда выглядит приблезительно так: <br />
`0 13 * * * /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
>>>>>>> bfdeb19bd0af64600467fcd22c8dbb4b4551b3fc
На Windows это можно реализовать через Диспетчер Задач.
