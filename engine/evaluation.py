import chess

PIECE_VALUES = {
    chess.PAWN:   100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK:   500,
    chess.QUEEN:  900,
    chess.KING:   0
}

MATE_SCORE=100000
DRAW_SCORE=0

def _material_score(board):
    score=0
    
    for piece_type in PIECE_VALUES:
        white_score=len(board.pieces(piece_type, chess.WHITE))
        black_score=len(board.pieces(piece_type, chess.BLACK))
        score+= (white_score-black_score)*PIECE_VALUES[piece_type]
    return score


def evaluate(board):
    if (board.is_checkmate()):
        if(board.turn==chess.WHITE):
            return -MATE_SCORE
        else:
            return MATE_SCORE
    if (board.is_fifty_moves() or board.is_stalemate() or board.is_insufficient_material() or board.is_repetition()):
        return DRAW_SCORE

    return _material_score(board)