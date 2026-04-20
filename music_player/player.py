import pygame
import os


class MusicPlayer:

    def __init__(self, music_folder="music"):
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False
        self._load_playlist(music_folder)

    def _load_playlist(self, folder):
        if not os.path.exists(folder):
            print(f"[WARN] Папка '{folder}' не найдена. Создаём...")
            os.makedirs(folder, exist_ok=True)
            return

        supported = (".wav", ".mp3", ".ogg")

        for filename in sorted(os.listdir(folder)):
            if filename.lower().endswith(supported):
                full_path = os.path.join(folder, filename)
                self.playlist.append(full_path)

        print(f"[INFO] Загружено треков: {len(self.playlist)}")

    def get_track_name(self):
        if not self.playlist:
            return "Нет треков"
        path = self.playlist[self.current_index]
        name = os.path.basename(path)
        name = os.path.splitext(name)[0]
        return name

    def play(self):
        if not self.playlist:
            return

        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def pause(self):
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        if self.is_playing:
            self.is_playing = False
            self.is_paused = False
            self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        if self.is_playing:
            self.is_playing = False
            self.is_paused = False
            self.play()

    def get_position(self):
        if self.is_playing:
            ms = pygame.mixer.music.get_pos()
            return ms / 1000 if ms >= 0 else 0
        return 0

    def get_status(self):
        if not self.playlist:
            return "Плейлист пуст"
        if self.is_paused:
            return "⏸ Пауза"
        if self.is_playing:
            return "▶ Играет"
        return "⏹ Стоп"
