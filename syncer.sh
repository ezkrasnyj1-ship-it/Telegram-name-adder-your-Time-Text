#!/bin/bash
# Syncer - запускает tg_nickname_sync.py синхронно с началом минуты

echo "[Syncer] Убиваю старый процесс если он есть..."

PID=$(pgrep -f tg_nickname)

if [ -n "$PID" ]; then
    echo "[Syncer] Процесс найден! Убиваю..."
    pkill -f tg_nickname
    sleep 1
    echo "[Syncer] Убил процесс, жду времени $(date +'%H:%M'):00 ..."
else
    echo "[Syncer] Старый процесс не найден, жду времени $(date +'%H:%M'):00 ..."
fi

# Ждём до начала следующей минуты
SEC=$(date +%S)
WAIT=$((60 - 10#$SEC))
sleep $WAIT

echo "[Syncer] $(date +'%H:%M'):00"
echo "[Syncer] Запускаю через NoHup..."

nohup python3 tg_nickname_sync.py --run > tgnick.log 2>&1 &

echo "[Syncer] Готово! Время синхронизировано!"
