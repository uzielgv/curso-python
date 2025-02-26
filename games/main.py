""" Programa principal de Games """
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main(archivo_torneo:str):
    """ Función principal de Games """
    if archivo_torneo != "":
        with open(archivo_torneo, "r", encoding="utf8") as f:
            torneo = json.load(archivo_torneo)
    else:
        players_mexico = ['Chicharito', 'Chucky', 'Ochoa', 'Tecatito', 'Guardado', 'Herrera', 'Layun', 'Moreno', 'Araujo', 'Oribe', 'Jimenez']
        players_espania = ['Casillas', 'Ramos', 'Pique', 'Iniesta', 'Silva', 'Isco', 'Busquets', 'Costa', 'Moreta', 'Asensio']
        lista_mexico = [Athlete(x) for x in players_mexico]
        lista_espania = [Athlete(x) for x in players_espania]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lista_mexico)
        espania = Team("España", soccer, lista_espania)
        juego = Game(mexico, espania)
        torneo = [juego.to_json()]
        archivo = "torneo.json"
        with open(archivo, "w", encoding="utf8") as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se escribió el archivo {archivo} satisfactoriamente.")
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)