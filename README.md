# TG02 Telegram Bot: media handling + translation (aiogram v3)

Учебный проект по теме: обработка входящих сообщений и отправка файлов в Telegram-боте.

**Автор:** Георгий Белянин (Georgy Belyanin) — georgy.belyanin@gmail.com

## Возможности

1. Сохраняет все присланные пользователем фото в папку `img/`.
2. Отправляет голосовое сообщение по команде `/voice` (файл `data/voice.ogg`).
3. Переводит любой текст пользователя на английский и отвечает переводом.

## Стек

- Python 3.10+
- aiogram 3
- python-dotenv
- deep-translator

## Быстрый старт (Windows 11)

### 1) Клонирование и установка

```bash
git clone <repo_url>
cd <repo_folder>

python -m venv .venv
.\.venv\Scripts\activate

pip install -U pip
pip install -r requirements.txt
```

### 2) Настройка переменных окружения

Скопируй `.env.example` в `.env` и вставь токен бота:

```bash
copy .env.example .env
notepad .env
```

Внутри `.env`:

```env
BOT_TOKEN=123456:ABCDEF_your_token_here
```

### 3) Запуск

```bash
python -m src.main
```

## Проверка функций

- `/start` — приветствие
- `/help` — справка
- Отправь фото — бот сохранит файл в `img/` и ответит именем файла
- Напиши любой текст — бот ответит переводом на английский
- `/voice` — бот отправит голосовое сообщение

## Структура проекта

```
.
├─ src/
├─ data/
├─ img/
├─ requirements.txt
└─ README.md
```

## Заметки

- Telegram может присылать фото в нескольких размерах; сохраняется максимальный.
- Для voice нужен формат OGG/opus (MP3 не подходит для voice).

