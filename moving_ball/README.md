# Moving Ball 🔴

Красный мяч, управляемый стрелками клавиатуры.

## Запуск

```bash
pip install pygame
python main.py
```

## Управление

| Клавиша | Действие         |
|---------|------------------|
| ← ↑ → ↓ | Движение (20px) |
| R       | Сброс в центр    |
| Q / ESC | Выход            |

## Ключевые концепции

- `pygame.draw.circle(surface, color, center, radius)` — рисование круга
- `event.type == pygame.KEYDOWN` + `event.key == pygame.K_UP` — стрелки
- Граничная проверка: `x - radius >= 0` и `x + radius <= width`
- `clock.tick(FPS)` — ограничение частоты кадров
