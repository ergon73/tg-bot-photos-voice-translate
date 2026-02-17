"""Вспомогательные функции."""

import logging
import re
from pathlib import Path

from deep_translator import GoogleTranslator

logger = logging.getLogger(__name__)

# Запрещённые символы для имён файлов в Windows
_WIN_INVALID = r'[<>:"/\\|?*\x00-\x1f]'


def ensure_dir(path: str) -> None:
    """Создаёт директорию, если её нет."""
    Path(path).mkdir(parents=True, exist_ok=True)


def safe_filename(name: str) -> str:
    """Очищает имя от символов, запрещённых в Windows."""
    return re.sub(_WIN_INVALID, "_", name)


def translate_to_en(text: str) -> str:
    """Переводит текст на английский. При ошибке возвращает оригинал с пометкой."""
    if not text or not text.strip():
        return text
    try:
        result = GoogleTranslator(source="auto", target="en").translate(text)
        return result if result else f"{text} (translation failed)"
    except Exception as e:
        logger.warning("Translation failed: %s", e)
        return f"{text} (translation failed)"
