import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A trail emmiting cycle.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _segments (list): A list of actors that work together to make up the cycle's trail.
    """
    def __init__(self, player):
        super().__init__()
        self._segments = []
        self._player = player
        self._prepare_cycle()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        for i in range(number_of_segments):
            trail = self._segments[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._player == "player1":
                segment.set_color(constants.RED)
            elif self._player == "player2":
                segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        # prevent cycle from turning back on itself
        head_velocity = self._segments[0].get_velocity()
        head_x = head_velocity.get_x()
        head_y = head_velocity.get_y()
        vel_x = velocity.get_x()
        vel_y = velocity.get_y()

        if head_x == 15 and vel_x == -15:
            pass
        elif head_x == -15 and vel_x == 15:
            pass
        elif head_y == 15 and vel_y == -15:
            pass
        elif head_y == -15 and vel_y == 15:
            pass
        else:
            self._segments[0].set_velocity(velocity)
    
    def _prepare_cycle(self):
        if self._player == "player1":
            x = int(constants.MAX_X / 3)
            y = int(constants.MAX_Y / 4)
            color = constants.RED
        elif self._player == "player2":
            x = int(constants.MAX_X / 3)
            y = int(constants.MAX_Y - constants.MAX_Y / 4)
            color = constants.GREEN

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)