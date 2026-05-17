
⏱️ TG Nickname Syncer
Автоматически добавляет текущее время в ник Telegram, синхронизированно с началом каждой минуты.
Пример: ник [23:00] | доп. текст
📦 Требования
Python 3.9+
Библиотека Telethon
API ключи с my.telegram.org/apps
Bash
🚀 Установка и запуск
1. Клонируй репозиторий
Bash
2. Первый запуск (настройка)
Bash
Скрипт спросит API ключи, имя, часовой пояс и формат.
3. Запуск с синхронизацией
Bash
syncer.sh автоматически:
Убивает старый процесс если он запущен
Ждёт до начала следующей минуты (:00 секунд)
Запускает скрипт через nohup в фоне
✏️ Смена доп. текста на лету
Пока скрипт работает в фоне:
Bash
Выбери 1 чтобы изменить текст, 2 чтобы убрать. Основной скрипт подхватит изменения через минуту.
🌍 Форматы и часовые пояса
Формат
Результат
[{time}]
qvrez [23:00]
• {time}
qvrez • 23:00
({time})
qvrez (23:00)
С доп. текстом: ник [23:00] | доп. текст
Город
Часовой пояс
Москва
Europe/Moscow
Екатеринбург
Asia/Yekaterinburg
Киев
Europe/Kiev
Алматы
Asia/Almaty
Лондон
Europe/London
⚠️ Важно
Не заливай config.json и session на GitHub — там твои личные данные!
Минимальный интервал — 30 секунд, иначе Telegram даст флуд-лимит
Первый запуск всегда вручную — Telegram попросит номер и код
📁 Файлы
Code
⏱️ TG Nickname Syncer
Automatically adds the current time to your Telegram nickname, synchronized to the start of each minute.
Example: qvrez [23:00] | Playing games
📦 Requirements
Python 3.9+
Telethon library
API keys from my.telegram.org/apps
Bash
🚀 Installation & Usage
1. Clone the repository
Bash
2. First run (setup)
Bash
The script will ask for API keys, base name, timezone and format.
3. Run with sync
Bash
syncer.sh automatically:
Kills the old process if it's running
Waits until the start of the next minute (:00 seconds)
Launches the script via nohup in the background
✏️ Change extra text on the fly
While the script is running in the background:
Bash
Choose 1 to change the text, 2 to remove it. The main script will pick up changes within a minute.
🌍 Formats & Timezones
Format
Result
[{time}]
qvrez [23:00]
• {time}
qvrez • 23:00
({time})
qvrez (23:00)
With extra text: qvrez [23:00] | Playing games
City
Timezone
Moscow
Europe/Moscow
Yekaterinburg
Asia/Yekaterinburg
Kyiv
Europe/Kiev
Almaty
Asia/Almaty
London
Europe/London
New York
America/New_York
⚠️ Important
Never upload config.json and session to GitHub — they contain your personal data!
Minimum interval is 30 seconds, otherwise Telegram will rate-limit you
First run must always be done manually — Telegram will ask for your phone number and code
