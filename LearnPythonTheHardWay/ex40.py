class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
# STUDY DRILL
    def reverse(self):
        for i in reversed(self.lyrics):
            print i

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


stages = Song(["If I was only wise enough",
                "To know everything",
                "Sure and true about myself"])
# STUDY DRILL
stages_var = ["If I was only wise enough",
                "To know everything",
                "Sure and true about myself"]

stages2 = Song(stages_var)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
stages.sing_me_a_song()
print '-' * 10
stages2.sing_me_a_song()
stages2.reverse()
