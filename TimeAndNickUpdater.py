"""
Telegram Auto-Nickname Updater
Автоматически обновляет имя в Telegram каждую минуту.
Формат: Имя [22:17] | Текст
"""

import asyncio
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

try:
    from telethon import TelegramClient
    from telethon.tl.functions.account import UpdateProfileRequest
except ImportError:
    print("❌ Установи зависимости: pip install telethon")
    exit(1)

CONFIG_FILE = "config.json"


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def setup():
    print("=" * 50)
    print("  Telegram Auto-Nickname Updater  ")
    print("=" * 50)

    cfg = load_config()

    # API credentials
    if not cfg.get("api_id"):
        print("\n📌 Получи API ключи на https://my.telegram.org/apps")
        cfg["api_id"] = int(input("API ID: ").strip())
        cfg["api_hash"] = input("API Hash: ").strip()

    # Base name
    print(f"\n👤 Текущее базовое имя: {cfg.get('base_name', '(не задано)')}")
    base = input("Введи базовое имя (или Enter чтобы не менять): ").strip()
    if base:
        cfg["base_name"] = base

    # Optional extra text
    print(f"\n✏️  Текущий доп. текст: {cfg.get('extra_text', '(нет)')}")
    print("Пример итогового ника: Алекс [22:17] | нет войне")
    extra = input("Доп. текст после времени (или Enter чтобы убрать): ").strip()
    cfg["extra_text"] = extra if extra else ""

    # Timezone
    print(f"\n🌍 Текущий часовой пояс: {cfg.get('timezone', 'Europe/Moscow')}")
    print("Примеры: Europe/Moscow, Europe/Kiev, Asia/Almaty, America/New_York")
    tz_input = input("Часовой пояс (или Enter для текущего): ").strip()
    if tz_input:
        try:
            ZoneInfo(tz_input)
            cfg["timezone"] = tz_input
        except ZoneInfoNotFoundError:
            print(f"⚠️  Часовой пояс '{tz_input}' не найден, используется {cfg.get('timezone', 'Europe/Moscow')}")

    if "timezone" not in cfg:
        cfg["timezone"] = "Europe/Moscow"

    # Update interval
    print(f"\n⏱️  Интервал обновления: {cfg.get('interval', 60)} сек")
    interval = input("Интервал в секундах (или Enter для 60): ").strip()
    cfg["interval"] = int(interval) if interval.isdigit() else 60

    # Format
    print("\n📋 Формат ника:")
    print("  1. Имя [22:17]")
    print("  2. Имя • 22:17")
    print("  3. Имя (22:17)")
    fmt_choice = input("Выбери формат (1/2/3, Enter = 1): ").strip()
    formats = {"1": "[{time}]", "2": "• {time}", "3": "({time})"}
    cfg["time_format"] = formats.get(fmt_choice, "[{time}]")

    save_config(cfg)
    print("\n✅ Настройки сохранены в config.json")
    return cfg


def build_name(cfg):
    tz = ZoneInfo(cfg.get("timezone", "Europe/Moscow"))
    now = datetime.now(tz)
    time_str = now.strftime("%H:%M")

    time_part = cfg.get("time_format", "[{time}]").replace("{time}", time_str)
    extra = cfg.get("extra_text", "")

    name = f"{cfg['base_name']} {time_part}"
    if extra:
        name += f" | {extra}"

    # Telegram limits: first_name max 64 chars
    return name[:64]


async def run(cfg):
    client = TelegramClient(
        "session",
        cfg["api_id"],
        cfg["api_hash"]
    )

    print("\n🔌 Подключение к Telegram...")
    await client.start()
    print("✅ Авторизация успешна!")
    print(f"📡 Обновление каждые {cfg['interval']} секунд. Ctrl+C для остановки.\n")

    try:
        while True:
            new_name = build_name(cfg)
            await client(UpdateProfileRequest(first_name=new_name))
            print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Ник обновлён: {new_name}")
            await asyncio.sleep(cfg["interval"])
    except KeyboardInterrupt:
        print("\n⛔ Остановлено. Восстанавливаю оригинальное имя...")
        await client(UpdateProfileRequest(first_name=cfg["base_name"]))
        print(f"✅ Имя сброшено до: {cfg['base_name']}")
    finally:
        await client.disconnect()


if __name__ == "__main__":
    import sys

    cfg = load_config()

    if "--run" in sys.argv and cfg.get("base_name"):
        # Запуск без настройки
        asyncio.run(run(cfg))
    else:
        cfg = setup()
        print("\n🚀 Запускаю обновление ника...")
        asyncio.run(run(cfg))
