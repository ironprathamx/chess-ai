"""UCI subprocess wrapper for the Stockfish chess engine."""

import subprocess


def get_best_move(fen):
    """Return Stockfish's best move for the given FEN position (UCI format)."""
    engine=subprocess.Popen(["stockfish"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    engine.stdin.write("uci\n")
    engine.stdin.flush()
    while True:
        line = engine.stdout.readline().strip()
        if line == "uciok":
            break

    engine.stdin.write("isready\n")
    engine.stdin.flush()
    while True:
        line = engine.stdout.readline().strip()
        if line=="readyok":
            break

    engine.stdin.write(f"position fen {fen}\n")
    engine.stdin.write("go movetime 1000\n")
    engine.stdin.flush()
    while True:
        line = engine.stdout.readline().strip()
        if line.startswith("bestmove"):
            move = line.split()[1]
            break

    engine.stdin.write("quit\n")
    engine.stdin.flush()
    engine.terminate()
    return move