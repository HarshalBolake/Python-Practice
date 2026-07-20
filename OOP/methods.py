class Calculator:
    def add(self,a,b):
        return a + b
    
    def mul(self,a,b):
        return a * b
    
calc = Calculator()
# print(calc.add(4,5))
# print(calc.mul(2,10))


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def celebrate_dirthday(self):
        self.age += 1
        print(f"Happy birthday {self.name} you are now {self.age}")

P1 = Person("Harshal",21)
# P1.celebrate_dirthday()



#Example
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    
    def add_song(self,song):
        self.songs.append(song)
        print(f"{self.songs} added to playlist")
    
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} remove from playlist")
    
    def show_playlist(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f"-{self.songs}")

P1 = Playlist("favourite")
P1.add_song("abra ka daabra")
P1.add_song("gili gili chuu")
P1.show_playlist()
P1.remove_song("gili gili chuu")
P1.show_playlist()

