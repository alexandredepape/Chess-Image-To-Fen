from enum import Enum, auto

import chess

PIECES_LABEL_MAP = [
    chess.Piece(chess.PAWN, chess.BLACK),
    chess.Piece(chess.PAWN, chess.WHITE),
    chess.Piece(chess.BISHOP, chess.BLACK),
    chess.Piece(chess.BISHOP, chess.WHITE),
    chess.Piece(chess.KING, chess.BLACK),
    chess.Piece(chess.KING, chess.WHITE),
    chess.Piece(chess.QUEEN, chess.BLACK),
    chess.Piece(chess.QUEEN, chess.WHITE),
    chess.Piece(chess.KNIGHT, chess.BLACK),
    chess.Piece(chess.KNIGHT, chess.WHITE),
    chess.Piece(chess.ROOK, chess.BLACK),
    chess.Piece(chess.ROOK, chess.WHITE),
    None,
]

PREDICTION_TRESHOLD = 0.5

MODELS_DIRECTORY = 'models'

PIECE_MODEL_FILENAME = 'piece_model.h5'
COLOR_MODEL_FILENAME = 'color_model.h5'
