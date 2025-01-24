import ctypes
import sys
import subprocess
import time

class AudioSettingsManager:
    def __init__(self):
        self.media_types = {
            "music": [5, 6, 5, 6, 5],
            "movie": [4, 6, 4, 6, 4],
            "game": [6, 6, 6, 6, 6],
            "voice": [3, 4, 3, 4, 3]
        }
        self.current_settings = [5, 5, 5, 5, 5]  # Default equalizer settings

    def change_volume(self, level):
        print(f"Changing system volume to: {level}")
        # Simulating volume change (Windows specific)
        try:
            volume_command = f"nircmd setsysvolume {level}"
            subprocess.run(volume_command, shell=True)
        except Exception as e:
            print(f"Failed to change volume: {e}")

    def equalize_audio(self, media_type):
        if media_type in self.media_types:
            self.current_settings = self.media_types[media_type]
            print(f"Equalizer settings adjusted for {media_type}: {self.current_settings}")
        else:
            print(f"Unknown media type: {media_type}")

    def display_current_settings(self):
        print(f"Current equalizer settings: {self.current_settings}")

def main():
    manager = AudioSettingsManager()
    if len(sys.argv) < 2:
        print("Usage: python InfoView.py [media_type] [volume_level]")
        sys.exit(1)

    media_type = sys.argv[1]
    volume_level = int(sys.argv[2]) if len(sys.argv) > 2 else 50000  # Default volume level

    manager.change_volume(volume_level)
    manager.equalize_audio(media_type)
    manager.display_current_settings()

if __name__ == "__main__":
    main()