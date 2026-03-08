import random
import pickle

class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class MusicPlaylist:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev
            tail.next = new_song
            new_song.prev = tail
            new_song.next = self.head
            self.head.prev = new_song

    def delete_song(self, title):
        if not self.head:
            print("Playlist is empty.")
            return

        temp = self.head
        while True:
            if temp.title == title:
                if temp == self.head and temp.next == self.head:
                    self.head = None
                    self.current = None
                    return
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                if temp == self.current:
                    self.current = temp.next
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"Song '{title}' not found.")

    def show_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        print("Playlist:")
        temp = self.head
        while True:
            marker = "<-- current" if temp == self.current else ""
            print(f"  {temp.title} {marker}")
            temp = temp.next
            if temp == self.head:
                break

    def play_current(self):
        if self.current:
            print(f"Now playing: {self.current.title}")
        else:
            print("No song is currently selected.")

    def next_song(self):
        if self.current:
            self.current = self.current.next
            self.play_current()

    def previous_song(self):
        if self.current:
            self.current = self.current.prev
            self.play_current()

    def shuffle_playlist(self):
        if not self.head:
            return
        songs = []
        temp = self.head
        while True:
            songs.append(temp.title)
            temp = temp.next
            if temp == self.head:
                break
        random.shuffle(songs)
        self.head = None
        for song in songs:
            self.add_song(song)
        self.current = self.head
        print("Playlist shuffled.")

    def save_playlist(self, filename):
        songs = []
        if self.head:
            temp = self.head
            while True:
                songs.append(temp.title)
                temp = temp.next
                if temp == self.head:
                    break
        with open(filename, 'wb') as f:
            pickle.dump(songs, f)
        print("Playlist saved.")

    def load_playlist(self, filename):
        try:
            with open(filename, 'rb') as f:
                songs = pickle.load(f)
                self.head = None
                self.current = None
                for song in songs:
                    self.add_song(song)
            print("Playlist loaded.")
        except FileNotFoundError:
            print("No saved playlist found.")

def main():
    playlist = MusicPlaylist()
    while True:
        print("""
        1. Add Song
        2. Delete Song
        3. Show Playlist
        4. Play Current Song
        5. Next Song
        6. Previous Song
        7. Shuffle Playlist
        8. Save Playlist
        9. Load Playlist
        0. Exit
        """)
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter song title: ")
            playlist.add_song(title)
        elif choice == '2':
            title = input("Enter song title to delete: ")
            playlist.delete_song(title)
        elif choice == '3':
            playlist.show_playlist()
        elif choice == '4':
            playlist.play_current()
        elif choice == '5':
            playlist.next_song()
        elif choice == '6':
            playlist.previous_song()
        elif choice == '7':
            playlist.shuffle_playlist()
        elif choice == '8':
            playlist.save_playlist("playlist.dat")
        elif choice == '9':
            playlist.load_playlist("playlist.dat")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
