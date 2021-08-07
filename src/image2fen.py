import chess
import image_slicer

from src.prediction import PiecePredictor


class Image2Fen:
    @staticmethod
    def get_fen(image_filename):
        tiles = Image2Fen.get_tiles(image_filename)

        piece_predictor = PiecePredictor()

        position = {}
        tiles_to_save = []
        for tile in tiles:
            image = tile.image
            predicted_piece, piece_confidence = piece_predictor.predict(image)
            if not predicted_piece:
                continue
            square = chess.square(tile.row - 1, 8 - tile.column)
            position[square] = predicted_piece
            print(predicted_piece, piece_confidence)
            tiles_to_save.append(tile)
        image_slicer.save_tiles(tiles_to_save, prefix='piece', format='png')
        chessboard = chess.Board()
        chessboard.set_piece_map(position)
        print(chessboard.fen())
        print(chessboard)

    @staticmethod
    def get_tiles(image_filename):
        tiles = image_slicer.slice(image_filename, col=8, row=8, save=False)
        # tiles = image_slicer.slice(image_filename, col=8, row=8, save=False)
        return tiles