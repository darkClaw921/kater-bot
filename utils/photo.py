import os
from typing import Dict, List, Optional

# Словарь с путями к фотографиям
PHOTOS = {
    "welcome": "photos/Фото 1.jpg",
    "wakesurfing": ["photos/Фото2.jpg", "photos/Фото2.1.jpg", "photos/Фото2.2.jpg"],
    "wakeboarding": ["photos/Фото3.jpg","photos/Фото 3.1.jpg", "photos/Фото 3.2.jpg", "photos/Фото 3.3.jpg"],
    "myths": ["photos/Фото 4.jpg", "photos/Фото 4.1.jpg", "photos/Фото 4.2.jpg", "photos/Фото 4.3.jpg", "photos/Фото 4.4.jpg", "photos/Фото 4.5.jpg", "photos/Фото 4.6.jpg"],
    "children": "photos/Фото 5.jpg",
}

def get_photo_path(photo_key: str) -> Optional[str]:
    """
    Возвращает путь к фотографии по ключу
    """
    if photo_key in PHOTOS:
        photo = PHOTOS[photo_key]
        if isinstance(photo, list):
            return photo[0]  # Возвращаем первое фото из списка
        return photo
    return None

def get_photo_paths(photo_key: str) -> List[str]:
    """
    Возвращает список путей к фотографиям по ключу
    """
    if photo_key in PHOTOS:
        photo = PHOTOS[photo_key]
        if isinstance(photo, list):
            return photo
        return [photo]
    return []

def check_photos_exist() -> Dict[str, bool]:
    """
    Проверяет наличие всех фотографий на диске
    """
    result = {}
    for key, paths in PHOTOS.items():
        if isinstance(paths, list):
            result[key] = all(os.path.exists(path) for path in paths)
        else:
            result[key] = os.path.exists(paths)
    return result 