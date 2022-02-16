import random

class Kinds():
    def __init__(self, kind,  movie_name, banned_word, banned_word1, banned_word2):
        self.kind = kind
        self.movie_name = movie_name
        self.banned_word = banned_word
        self.banned_word1 = banned_word1
        self.banned_word2 = banned_word2

class RandomMovie(Kinds):
    pass

Movielst = []
dosya = open("Movies.txt", "r")
Movielst = dosya.readlines()
Rand= random.choice(Movielst)
"""kind, movie_name, banned_word, banned_word1, banned_word2 = Rand"""
rnd = list(Rand)
print(rnd)
RandMovie = RandomMovie(Rand[0], Rand[2], Rand[4], Rand[6], Rand[8])
print("kind: {}, \nmovie_name: {}, \nbanned_word :{}, \nbanned_word1 :{}, \nbanned_word2 :{}".format(RandMovie.kind, RandMovie.movie_name, RandMovie.banned_word, RandMovie.banned_word1, RandMovie.banned_word2))

