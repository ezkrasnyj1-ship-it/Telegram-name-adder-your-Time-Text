#!/bin/bash

BASE_URL="http://89.125.145.99:8080"

clear
echo "  ____                          "
echo " / ___|  _   _  _ __    ___  ___ _ __ "
echo " \___ \ | | | || '_ \  / __|/ _ \ '__|"
echo "  ___) || |_| || | | || (__|  __/ |   "
echo " |____/  \__, ||_| |_| \___|\___||_|   "
echo "          |___/                        "
echo ""
echo "         Created by t.me/qvrezikk"
echo ""

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
    echo "[Syncer] Убит."
else
    echo "[Syncer] Старый процесс не найден."
fi

NOW=$(date +'%H:%M:%S')
NEXT_MIN=$(date -d "+1 minute" +'%H:%M' 2>/dev/null || date -v+1M +'%H:%M')
echo "[Syncer] Время $NOW жду ${NEXT_MIN}:00 ..."

SEC=$(date +%S)
WAIT=$((60 - 10#$SEC))
sleep $WAIT

echo "[Syncer] Время стукнуло, запускаю ченджер через nohup..."
nohup python3 TimeAndNickUpdater.py --run > tgnick.log 2>&1 &

echo "[Syncer] Готово! Created by t.me/qvrezikk"
