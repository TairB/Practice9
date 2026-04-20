"""
Класс Player — управляет плейлистом и воспроизведением.

pygame.mixer.music работает только с ОДНИМ треком за раз.
Методы:
  load(path)  — загружает файл
  play()      — воспроизводит
  stop()      — останавливает
  pause()     — пауза
  unpause()   — снять паузу
  get_pos()   — позиция в миллисекундах
"""

import pygame
import os


class MusicPlayer:
    """
    Управляет плейлистом: загрузка, воспроизведение, переключение.
    """

    def __init__(self, music_folder="music"):
        """
        music_folder — папка с MP3/WAV файлами
        """
        self.playlist = []          # список путей к файлам
        self.current_index = 0      # индекс текущего трека
        self.is_playing = False     # флаг воспроизведения
        self.is_paused = False      # флаг паузы

        # Загружаем все треки из папки
        self._load_playlist(music_folder)

    def _load_playlist(self, folder):
        """Сканирует папку и добавляет все .wav и .mp3 файлы."""
        if not os.path.exists(folder):
            print(f"[WARN] Папка '{folder}' не найдена. Создаём...")
            os.makedirs(folder, exist_ok=True)
            return

        # Поддерживаемые форматы
        supported = (".wav", ".mp3", ".ogg")

        for filename in sorted(os.listdir(folder)):
            if filename.lower().endswith(supported):
                full_path = os.path.join(folder, filename)
                self.playlist.append(full_path)

        print(f"[INFO] Загружено треков: {len(self.playlist)}")

    def get_track_name(self):
        """Возвращает имя текущего трека (без папки и расширения)."""
        if not self.playlist:
            return "Нет треков"
        path = self.playlist[self.current_index]
        name = os.path.basename(path)           # "track1.wav"
        name = os.path.splitext(name)[0]        # "track1"
        return name

    def play(self):
        """Воспроизводит текущий трек."""
        if not self.playlist:
            return

        if self.is_paused:
            # Снимаем паузу вместо перезапуска
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            # Загружаем и запускаем трек
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

        self.is_playing = True

    def stop(self):
        """Останавливает воспроизведение."""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def pause(self):
        """Ставит на паузу или снимает с паузы."""
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def next_track(self):
        """Переключает на следующий трек (с зацикливанием)."""
        if not self.playlist:
            return
        # % len(playlist) — когда дойдём до конца, вернёмся к началу
        self.current_index = (self.current_index + 1) % len(self.playlist)
        if self.is_playing:
            self.is_playing = False
            self.is_paused = False
            self.play()

    def prev_track(self):
        """Переключает на предыдущий трек."""
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        if self.is_playing:
            self.is_playing = False
            self.is_paused = False
            self.play()

    def get_position(self):
        """
        Возвращает позицию воспроизведения в секундах.
        get_pos() возвращает миллисекунды, делим на 1000.
        Возвращает 0 если не играет.
        """
        if self.is_playing:
            ms = pygame.mixer.music.get_pos()
            return ms / 1000 if ms >= 0 else 0
        return 0

    def get_status(self):
        """Возвращает строку-статус для отображения."""
        if not self.playlist:
            return "Плейлист пуст"
        if self.is_paused:
            return "⏸ Пауза"
        if self.is_playing:
            return "▶ Играет"
        return "⏹ Стоп"
