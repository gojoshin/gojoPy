# task 1: line 75
# task 2: line 271
# task3: 
# from PIL import Image

# img = Image.open("Hanamura.jpg")

# # Show the image size (width, height)
# print("Image size:", img.size)

from PIL import Image

class Song:
    def __init__(self, name, artist, genre, length_seconds, album, cover_image=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.length_seconds = length_seconds
        self.album = album
        self.cover_image = cover_image

    def play(self):
        print(f"Now playing: {self.name} by {self.artist}")

    def get_length_minutes(self):
        minutes = self.length_seconds // 60
        seconds = self.length_seconds % 60
        return f"{minutes} minutes and {seconds} seconds"

    def show_cover(self):
        if self.cover_image:
            self.cover_image.show()
        else:
            print("No cover image available.")

# Load a cover image (optional)
cover = Image.open("Memories_Do_Not_Open.jpg")  

# 3 Songss
song1 = Song("Paris", "The Chainsmokers", "Pop", 221, "Memories...Do Not Open", cover)
song2 = Song("Something Just Like This", "The Chainsmokers & Coldplay", "Pop", 247, "Memories...Do Not Open", cover)
song3 = Song("Break Up Every Night", "The Chainsmokers", "Pop", 186, "Memories...Do Not Open", cover)

# method
for song in [song1, song2, song3]:
    song.play()
    print("Length:", song.get_length_minutes())
    song.show_cover()
    print()





