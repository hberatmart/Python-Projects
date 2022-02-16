import random

class Kinds:
    def __init__(self, kind, word, banned_word, banned_word1, banned_word2):
		self.kind = kind
        self.word = word
        self.banned_word = banned_word
        self.banned_word1 = banned_word1
        self.banned_word2 = banned_word2

def __to_string__()
	print("________type_________")
	print("word: {} \nbanned_word :{} \nbanned_word1 :{} \nbanned_word2 :{}".format(word, banned_word, banned_word1, banned_word2)

"""class RandomMovieGenerator():
	def getRandom(type):
		return"""

X = [["action","avangers","ironman"], ["action","avangers","ironman"], ["action","avangers","ironman"] ]
rand1= random.choice(X)
a,b,c=rand1
Obj1 = Kinds(a, b, c)
Obj1.__to_string__()



""""class ActionMovie(Kinds):
    pass
class ScienceFictionMovie(Kinds):
    pass

MovieKind = ['action']

Action = ['The_Forever_Purge', 'Fast_and_Furious', 'Jhon_Wick', 'Avengers']

ScienceFiction = ['Venom', 'Dune', 'Black Widow',]

ran = random.choice(MovieKind)
print(ran)

if ran == 'action':
    ActRan = random.choice(Action)
    if ActRan == 'The_Forever_Purge':
        The_Forever_Purge = ActionMovie('The Forever Purge', 'Actors Names', 'Director Names', 'IMDB')
        print("________Action_________")
        print("word: {} \nbonned_word :{} \nbonned_word1 :{} \nbonned_word2 :{}".format(The_Forever_Purge.word, The_Forever_Purge.bonned_word, The_Forever_Purge.bonned_word1, The_Forever_Purge.bonned_word2))

    elif ActRan == 'Fast_and_Furious':
        Fast_and_Furious = ActionMovie('Fast and Furious', 'Actors Names', 'Director Names', 'IMDB')
        print("________Action_________")
        print("word: {} \nbonned_word :{} \nbonned_word1 :{} \nbonned_word2 :{}".format(Fast_and_Furious.word, Fast_and_Furious.bonned_word, Fast_and_Furious.bonned_word1, Fast_and_Furious.bonned_word2))

    elif ActRan == 'Jhon_Wick':
        Jhon_Wick = ActionMovie('Jhon Wick', 'Actors Names', 'Director Names', 'IMDB')
        print("________Action_________")
        print("word: {} \nbonned_word :{} \nbonned_word1 :{} \nbonned_word2 :{}".format(Jhon_Wick.word, Jhon_Wick.bonned_word, Jhon_Wick.bonned_word1, Jhon_Wick.bonned_word2))

    elif ActRan == 'Avengers':
        Avengers = ActionMovie('Avengers', 'Actors Names', 'Director Names', 'IMDB')
        print("________Action_________")
        print("word: {} \nbonned_word :{} \nbonned_word1 :{} \nbonned_word2 :{}".format(Avengers.word, Avengers.bonned_word, Avengers.bonned_word1, Avengers.bonned_word2))"""