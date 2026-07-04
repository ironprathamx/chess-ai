# Chess AI

A Python project focused on incrementally building a modular chess engine. Stockfish handles move selection today through a swappable interface, while evaluation and search are developed in `engine/` with the goal of replacing that dependency.

---

## Overview

The CLI is primarily a testing interface; the main objective is a native chess engine with its own search and evaluation. Move generation, legal move validation, and chess rules are provided by `python-chess`, so development can focus on engine architecture, evaluation, and search rather than reimplementing the rules.

Today, [Stockfish](https://stockfishchess.org/) fills the engine role. `engine/evaluation.py` provides a material-based evaluator, and `engine/search.py` is reserved for the search implementation. The `core/` layer handles board state, turns, and player abstractions so the engine backend can be swapped without touching game logic.

**Why this project?** I play chess regularly and wanted to understand how engines work from the inside - move generation, evaluation, search - rather than treating them as a black box. The project is built incrementally so each major component can be designed, implemented, and understood independently.

---

## Features

- **Material evaluation** - centipawn scoring with checkmate and draw detection (`engine/evaluation.py`). Implemented but not yet connected to move selection.
- **Engine interface** - `EnginePlayer` delegates to Stockfish over UCI (1 second per move). The same abstraction is intended to host a native engine later.
- **Board layer** - FEN setup, UCI move input, legal move validation, undo, and ASCII display (via `python-chess`).
- **Game logic** - turn alternation and game-over detection (checkmate, stalemate, draws).
- **CLI harness** - choose White or Black and enter moves in UCI format (e.g. `e2e4`, `e7e8q`) to exercise the engine interactively.

---

## Architecture

The game management layer and the engine layer are deliberately separate. `core/player.py` defines how a game requests moves; `engine/` defines how those moves are chosen. That boundary lets Stockfish serve as the engine today and a native implementation replace it later without rewriting board or turn logic.

| Component | Role |
|-----------|------|
| `main.py` | CLI entry point; wires up players and runs the game loop. |
| `core/board.py` | Wraps `python-chess` for moves, FEN, and board display. |
| `core/game.py` | Owns the board and two players; handles turns and game-over state. |
| `core/player.py` | `HumanPlayer` and `EnginePlayer` abstractions. |
| `engine/stockfish_engine.py` | Stockfish subprocess over the UCI protocol. |
| `engine/evaluation.py` | Static evaluation (material, mate, draws) for the native engine. |
| `engine/search.py` | Placeholder for search algorithms (not yet implemented). |

Stockfish runs as an external binary on your `PATH`. The native modules in `engine/` are the active development target.

---

## Installation

Requires **Python 3.10+** (3.11+ recommended) and **Stockfish** on your `PATH` as the `stockfish` command.

### 1. Clone the repository

```bash
git clone https://github.com/ironprathamx/chess_ai.git
cd chess_ai
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Stockfish

Stockfish is not a Python package; install it separately.

**macOS (Homebrew):**

```bash
brew install stockfish
```

**Linux (Debian/Ubuntu):**

```bash
sudo apt install stockfish
```

**Windows:** download a build from [stockfishchess.org/download](https://stockfishchess.org/download/) and ensure `stockfish.exe` is on your `PATH`.

Verify:

```bash
stockfish
# type "quit" to exit
```

### 5. Run

From the repository root (with the virtual environment activated):

```bash
python main.py
```

Enter `white` or `black` (lowercase) when prompted, then UCI moves on your turn.

---

## Project Structure

```
chess_ai/
├── core/                    # Game management (board, turns, players)
│   ├── board.py
│   ├── game.py
│   └── player.py
├── engine/                  # Engine implementation
│   ├── evaluation.py        # Position evaluation
│   ├── search.py            # Search (stub)
│   └── stockfish_engine.py  # Stockfish UCI adapter
├── main.py                  # CLI test harness
├── requirements.txt
└── README.md
```

---

## Technologies Used

- **Python 3**
- **[python-chess](https://python-chess.readthedocs.io/)** (`chess` on PyPI) - board representation, move generation, and validation
- **[Stockfish](https://stockfishchess.org/)** - external engine communicating via the [Universal Chess Interface (UCI)](https://backscattering.de/chess/uci/) protocol (system install, not pip)

---

## Roadmap / Upcoming Work

The next phases follow directly from the current code:

1. **Minimax search** - implement depth-limited search in `engine/search.py`
2. **Alpha-beta pruning** - cut redundant branches during search
3. **Move ordering** - search promising moves first to improve pruning efficiency
4. **Evaluation improvements** - extend beyond material (piece-square tables, king safety, etc.)
5. **Transposition tables** - cache evaluated positions to avoid redundant work
6. **Iterative deepening** - search to increasing depths within a time budget
7. **Native engine integration** - wire search + evaluation into `EnginePlayer` as a Stockfish alternative

---

## Current Status

Stockfish currently performs all move selection. A material-based evaluation module is implemented in `engine/evaluation.py` but not yet connected to gameplay. Search is the next major milestone; once in place, the native engine can replace Stockfish through the existing `EnginePlayer` interface.

---

## Contributing

Contributions are welcome. For larger changes, open an issue first to discuss direction.

1. Fork the repository and create a branch from `main`.
2. Make focused changes; match existing style and module layout.
3. Test locally: `pip install -r requirements.txt`, ensure Stockfish is on `PATH`, run `python main.py`.
4. Open a pull request with a clear description of what changed and why.

---

## License

No license file is included yet. The project is currently **unlicensed**; all rights reserved by the author until a license is added.

<!-- TODO: Add a LICENSE file once a license is chosen (e.g. MIT, Apache-2.0). -->
