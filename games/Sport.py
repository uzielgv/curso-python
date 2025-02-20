""" Clase Sport """
class Sport:
    """ Clase para representar un deporte """
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if isinstance(players, int):
            self.players = players
        else:
            self.players = int(players)
        self.league = league

    def __str__(self)->str:
        """ Representación en string de Sport """
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)->str:
        """ Representación en string de Sport """
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        """ Convertir Sport a JSON """
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json)
    nfl = Sport("Football", "11", "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = {nfl, lmp, mlb, lmx, nba, s}
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
    sports_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sports_list.append(d)
    print(sports_list)
    print(sports_list[0].to_json())

    import json
    archivo_json = "deportes.json"
    sports_json = [sport.to_json() for sport in sports_list]
    with open(archivo_json, "w") as file:
        json.dump(sports_json, file, indent=4)
    sports_list_json = []
    with open(archivo_json, "r") as file:
        sports_list_json = json.load(file)
    print(sports_list_json)