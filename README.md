# Practice 9 — Game Development with Pygame

Три классические игры на Pygame.

## Установка

```bash
pip install -r requirements.txt
```

## Проекты

### 1. Mickey's Clock (`mickeys_clock/`)
Часы с руками Микки Мауса. Демонстрирует поворот изображений (`pygame.transform.rotate`) и работу с системным временем.

```bash
cd mickeys_clock && python main.py
```

### 2. Music Player (`music_player/`)
Музыкальный плеер с клавиатурным управлением. Положи `.wav`/`.mp3` файлы в `music_player/music/`.

```bash
cd music_player && python main.py
```

| P | S | SPACE | N | B | Q |
|---|---|-------|---|---|---|
| Play | Stop | Pause | Next | Back | Quit |

### 3. Moving Ball (`moving_ball/`)
Красный мяч, управляемый стрелками. Демонстрирует `pygame.draw.circle` и граничные проверки.

```bash
cd moving_ball && python main.py
```

## Ключевые концепции Pygame

| Концепция | Где используется |
|-----------|-----------------|
| `pygame.transform.rotate()` | Mickey's Clock |
| `pygame.mixer.music` | Music Player |
| `pygame.draw.circle()` | Moving Ball |
| `event.type == KEYDOWN` | Все три игры |
| `clock.tick(FPS)` | Все три игры |

## Git

```bash
git add .
git commit -m "Add Practice9 - Pygame games: Mickey's clock, music player, moving ball"
git push origin main
```
