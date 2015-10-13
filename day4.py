class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_baby = Song(["Happy birthday to you","I don't want to ger sued","So I'll stop right there"])

bulls_on_parade = Song(["They really around the farmily","With pockets full of shells"])

happy_baby.sing_me_a_song()
print "\n"
bulls_on_parade.sing_me_a_song()