import random
class Kinds:
    def __init__(self, kind, movie_name, banned_word, banned_word1, banned_word2):
        self.kind = kind
        self.movie_name = movie_name
        self.banned_word = banned_word
        self.banned_word1 = banned_word1
        self.banned_word2 = banned_word2

    def Moviefunc(self):
        print("____--" + self.kind + "--____")
        print("kind: {} \nmovie_name: {} \nbanned_word :{} \nbanned_word1 :{} \nbanned_word2 :{}".format(
            self.kind, self.movie_name, self.banned_word, self.banned_word1,
            self.banned_word2))


lst = []
cntr = 0
with open('Movies.txt', "r") as file:
    for line in file:
        lst.append(line)
        cntr += 1
    num = random.randint(0, cntr - 1)
    Rand = lst[num].split()
Ran = Kinds(Rand[0], Rand[1], Rand[2], Rand[3], Rand[4])
Ran.Moviefunc()
