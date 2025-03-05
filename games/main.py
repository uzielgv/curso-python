""" Programa principal de Games """
import json
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import game_logic as gl

def main(archivo_torneo:str):
    """ Función principal de Games """
    if archivo_torneo != "":
        with open(archivo_torneo, "r", encoding="utf8") as f:
            torneo = json.load(f)
    else:
        gl.create_gamefile()
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "r", encoding="utf8") as f:
            torneo = json.load(f)
    gl.play_game(torneo)
    # Calcular el tablero de puntuación
    tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)