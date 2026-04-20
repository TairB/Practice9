# Mickey's Clock 🕐

Цифровые часы с руками Микки Мауса.

## Запуск

```bash
pip install pygame
python main.py
```

## Структура

```
mickeys_clock/
├── main.py          — главный файл, game loop
├── clock.py         — класс MickeyClock
├── images/
│   └── mickey_hand.png  — изображение руки (замените на реальное)
└── README.md
```

## Ключевые концепции

- `pygame.transform.rotate(image, angle)` — поворот изображения
- `surface.get_rect(center=point)` — центрирование после поворота
- `datetime.datetime.now()` — получение системного времени
- Угол = `(value / max_value) * 360` градусов

## Управление

| Клавиша | Действие |
|---------|----------|
| Q / ESC | Выход    |
