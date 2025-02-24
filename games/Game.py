from Athlete import Athlete
from Sport import Sport
from Team import Team

class Game:
    ''' Clase Game'''
    sports_dict = {'LMP':[x for x in range(0, 11)], 
                   'NBA':[x for x in range(70, 121)], 
                   'NFL':[x for x in range(3, 50)],
                   'LMX':[x for x in range(0, 9)],
                   'MLB':[x for x in range(0, 11)]}

    def __init__(self, A:Team, B:Team):
        ''' Constructor de la clase Game '''
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        ''' Juego simulado entre equipos '''
        for s in self.sports_dict.values():
            print(s)

if __name__ == "__main__":
    dt = ['Jordan', 'Johnson', 'Pipen', 'Bird', 'Kobe']
    cz = ['Bjovik', 'Czack', 'Pfeizer', 'Leonard', 'Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x)for x in cz]
    basketball = Sport("NBA", 5, "DreamTeam")
    t = Team("Dream Team", basketball, players_a)
    c = Team("Czech Republic", basketball, players_b)
    game = Game(t, c)
    game.play()