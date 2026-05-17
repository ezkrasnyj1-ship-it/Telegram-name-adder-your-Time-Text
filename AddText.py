# -*- coding: utf-8 -*-
"""
Управление доп. текстом в нике на лету.
Запускай пока основной скрипт работает в фоне.
"""

import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("❌ config.json не найден! Сначала запусти основной скрипт.")
        exit(1)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

def main():
    cfg = load_config()

    print("=" * 40)
    print("  Управление доп. текстом в нике")
    print("=" * 40)
    print(f"\n👤 Базовое имя: {cfg.get('base_name', '?')}")
    print(f"✏️  Текущий доп. текст: {cfg.get('extra_text', '(нет)')}")
    print(f"\nПример ника: {cfg.get('base_name')} [22:17] | {cfg.get('extra_text') or 'текст'}")
    print("\nЧто хочешь сделать?")
    print("  1. Изменить доп. текст")
    print("  2. Убрать доп. текст")
    print("  3. Выйти")

    choice = input("\nВыбор (1/2/3): ").strip()

    if choice == "1":
        new_text = input("Новый доп. текст: ").strip()
        if new_text:
            cfg["extra_text"] = new_text
            save_config(cfg)
            print(f"\n✅ Готово! Следующий ник: {cfg['base_name']} [ЧЧ:ММ] | {new_text}")
        else:
            print("⚠️  Пустой текст, ничего не изменено.")

    elif choice == "2":
        cfg["extra_text"] = ""
        save_config(cfg)
        print(f"\n✅ Убрано! Следующий ник: {cfg['base_name']} [ЧЧ:ММ]")

    elif choice == "3":
        print("Выход.")
    else:
        print("❌ Неверный выбор.")

if __name__ == "__main__":
    main()
