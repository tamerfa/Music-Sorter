import os
import shutil
from pathlib import Path


class MusicDistributor:
    def __init__(self, source_path, min_songs_per_artist=3):
        self.source_path = source_path
        self.min_songs_per_artist = min_songs_per_artist
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.source_songs = os.listdir(source_path)
        self.artists_counts = {}

    def distribute(self):
        self._count_artists_songs()
        self._create_artist_folders()
        self._move_songs_to_folders()

    def _count_artists_songs(self):
        for song in self.source_songs:
            if '-' in song and '.mp3' in song:
                artist_name = song.split(' - ')[0].lower()
                self.artists_counts.setdefault(artist_name, 0)
                self.artists_counts[artist_name] += 1

    def _create_artist_folders(self):
        for artist, count in self.artists_counts.items():
            if count >= self.min_songs_per_artist:
                folder_path = os.path.join(self.current_directory, artist)
                Path(folder_path).mkdir(exist_ok=True)

    def _move_songs_to_folders(self):
        for song in self.source_songs:
            if '-' in song and '.mp3' in song:
                artist_name = song.split(' - ')[0].lower()
                if artist_name in self.artists_counts and self.artists_counts[artist_name] >= self.min_songs_per_artist:
                    source_song_path = os.path.join(self.source_path, song)
                    target_song_path = os.path.join(self.current_directory, artist_name, song)
                    shutil.move(source_song_path, target_song_path)
                    
                    

distributor = MusicDistributor('C:\\music_coding_tryout\\foreign_songs')
distributor.distribute()