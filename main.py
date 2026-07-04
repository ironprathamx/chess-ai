"""CLI entry point for a human vs. Stockfish chess game."""

from core.game import Game
from core.player import EnginePlayer, HumanPlayer

color_human = str(input("Which colour would you like to play as? (all small)"))
human_player = HumanPlayer(color_human)
if color_human == "white":
    engine_player = EnginePlayer("black")
    g = Game(human_player, engine_player)
elif color_human == "black":
    engine_player = EnginePlayer("white")
    g = Game(engine_player, human_player)

while g.is_running():
    g.print_board()
    if g.get_curr_color() == color_human:
        move = str(input("Enter your move: "))
        human_player.set_move(move)

    success = g.request_turn()
    if success == False:
        print("Error!")
