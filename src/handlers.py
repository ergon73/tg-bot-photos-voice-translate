"""Обработчики сообщений бота."""

import logging
from pathlib import Path

from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message

from .utils import ensure_dir, safe_filename, translate_to_en

logger = logging.getLogger(__name__)

router = Router()

IMG_DIR = Path(__file__).resolve().parent.parent / "img"
VOICE_PATH = Path(__file__).resolve().parent.parent / "data" / "voice.ogg"


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    """Приветствие при /start."""
    name = message.from_user.full_name or "пользователь"
    await message.answer(
        f"Привет, {name}! Я сохраняю фото, перевожу текст на английский "
        "и могу отправить голосовое по /voice."
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Справка при /help."""
    await message.answer(
        "Команды:\n"
        "/start — приветствие\n"
        "/help — эта справка\n"
        "/voice — отправить голосовое сообщение\n\n"
        "Также:\n"
        "• Отправь фото — сохраню в img/\n"
        "• Напиши текст — переведу на английский"
    )


@router.message(Command("voice"))
async def cmd_voice(message: Message, bot: Bot) -> None:
    """Отправка голосового сообщения по /voice."""
    if not VOICE_PATH.exists():
        logger.warning("Voice file not found: %s", VOICE_PATH)
        await message.answer(
            "Файл data/voice.ogg не найден. Добавьте OGG/opus файл в репозиторий."
        )
        return
    try:
        voice_file = FSInputFile(VOICE_PATH)
        await message.answer_voice(voice=voice_file)
    except Exception as e:
        logger.exception("Failed to send voice: %s", e)
        await message.answer("Не удалось отправить голосовое сообщение.")


@router.message(F.photo)
async def handle_photo(message: Message, bot: Bot) -> None:
    """Сохранение фото в img/."""
    ensure_dir(IMG_DIR)
    photo = message.photo[-1]
    safe_name = safe_filename(photo.file_unique_id or "photo")
    filename = f"{safe_name}.jpg"
    filepath = IMG_DIR / filename
    try:
        await bot.download(photo, destination=filepath)
        await message.answer(f"Фото сохранено: {filename}")
    except Exception as e:
        logger.exception("Failed to save photo: %s", e)
        await message.answer("Не удалось сохранить фото.")


@router.message(F.text)
async def handle_text(message: Message) -> None:
    """Перевод входящего текста на английский."""
    text = message.text or ""
    translated = translate_to_en(text)
    await message.answer(translated)
