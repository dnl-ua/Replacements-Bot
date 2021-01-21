# Заменный бот
Бот берет изображение замен с сайта колледжа и отправляет в телеграм. <br />
Бот в телеграм: [@cctereplbot](https://t.me/cctereplbot) <br />
Канал в телеграм: [@ccterepls](https://t.me/ccterepls)

# Автоматизация
Я создал [cron](https://crontab.guru/crontab.5.html) файл который будет запускать [download_image.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/download_image.py) каждый день (кроме субботы) в 12:30, а после этого, в 12:35, он запустит [send_to_channel.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/send_to_channel.py) что отправит замены в канал. Команда выглядит приблезительно так: <br />

`30 12 * * 0-5 /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для [download_image.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/download_image.py) <br />
`35 13 * * 0-5 /PATH/TO/PYTHON/BINARY /PATH/TO/SCRIPT` <br />
для [send_to_channel.py](https://github.com/kagarlytskiy/cctereplbot/blob/main/send_to_channel.py) <br />

На Windows это можно реализовать через Диспетчер Задач.
