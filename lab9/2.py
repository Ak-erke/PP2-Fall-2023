import tkinter as tk
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(root, text="Next", command=self.next_music)
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_music)

        self.play_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.next_button.pack(pady=10)
        self.prev_button.pack(pady=10)

        self.current_song = 0
        self.songs = [
            r'C:\Users\user\PP2\lab9\Swedish House Mafia feat. The Weeknd - Moth To A Flame (Live From Copenhagen).mp3',
            r'C:\Users\user\PP2\lab9\The Weeknd feat. Lily Rose Depp - Dollhouse.mp3',
            r'C:\Users\user\PP2\lab9\The Weeknd,JENNIE,Lily-Rose Depp - One Of The Girls (with JENNIE, Lily Rose Depp).mp3'
        ]
        mixer.init()  # Initialize the mixer
        self.play_music()

        # Bind keyboard events
        root.bind("<space>", lambda event: self.play_music())
        root.bind("<KeyPress-s>", lambda event: self.stop_music())
        root.bind("<Right>", lambda event: self.next_music())
        root.bind("<Left>", lambda event: self.prev_music())

    def play_music(self):
        try:
            mixer.music.load(self.songs[self.current_song])
            mixer.music.play()
        except IndexError:
            print("No songs in the playlist.")

    def stop_music(self):
        mixer.music.stop()

    def next_music(self):
        self.current_song = (self.current_song + 1) % len(self.songs)
        self.play_music()

    def prev_music(self):
        self.current_song = (self.current_song - 1) % len(self.songs)
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
