import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made.. 
    
    The responsibility of Score is to display the number of points each player has earned by winning 
    games. It contains a method for showing points.

    Attributes:
        _player (string): Represents either player 1 or player 2
    """
    def __init__(self, player):
        super().__init__()
        self._player = player
        self.add_points()
        if self._player == "player2":
            self.set_position(Point(-100, 0))

    def add_points(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if self._player == "player1":
            self.set_text(f"Player One: {constants.PLAYER1_SCORE}")
        if self._player == "player2":
            self.set_text(f"Player Two: {constants.PLAYER2_SCORE}")