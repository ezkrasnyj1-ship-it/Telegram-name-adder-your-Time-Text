#!/bin/bash
# Syncer - скачивает файлы с GitHub и запускает синхронно с началом минуты

BASE_URL="https://raw.githubusercontent.com/ezkrasnyj1-ship-it/Telegram-name-adder-your-Time-Text/refs/heads/main"

echo "[Syncer] Проверяю наличие файлов..."

if [ ! -f "TimeAndNickUpdater.py" ]; then
    echo "[Syncer] TimeAndNickUpdater.py не найден, скачиваю..."
    curl -s -o TimeAndNickUpdater.py "$BASE_URL/TimeAndNickUpdater.py"
    echo "[Syncer] TimeAndNickUpdater.py скачан!"
else
    echo "[Syncer] TimeAndNickUpdater.py уже есть."
fi

if [ ! -f "AddText.py" ]; then
    echo "[Syncer] AddText.py не найден, скачиваю..."
    curl -s -o AddText.py "$BASE_URL/AddText.py"
    echo "[Syncer] AddText.py скачан!"
else
    echo "[Syncer] AddText.py уже есть."
fi

echo "[Syncer] Убиваю старый процесс если он есть..."

PID=$(pgrep -f TimeAndNickUpdater)

if [ -n "$PID" ]; then
    echo "[Syncer] Процесс найден! Убиваю..."
    pkill -f TimeAndNickUpdater
    sleep 1
    echo "[Syncer] Убил процесс, жду времени $(date +'%H:%M'):00 ..."
else
    echo "[Syncer] Старый процесс не найден, жду времени $(date +'%H:%M'):00 ..."
fi

SEC=$(date +%S)
WAIT=$((60 - 10#$SEC))
sleep $WAIT

echo "[Syncer] $(date +'%H:%M'):00"
echo "[Syncer] Запускаю через NoHup..."

nohup python3 TimeAndNickUpdater.py --run > tgnick.log 2>&1 &

echo "[Syncer] Готово! Время синхронизировано!"
