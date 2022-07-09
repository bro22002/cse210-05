from game.scripting.action import Action

class ActorsAction(Action):
    """
    An update action that modifies actors over time.
    
    The responsability of ModifyActorsAction is to grow the length of each
    cycle's trail at a consistent rate.
    
    Attributes:
        _timer (int): An iterating, self-resetting value used to time.
        _is_game_over (bool): The state of the game, whether over or not."""

    def __init__(self):
        """Contructs a new ModifyActorsAction instance."""
        self._timer = 0
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the modify actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        update_actions = script.get_actions("update")
        handle_collisions_action = update_actions[1]
        self._is_game_over = handle_collisions_action.is_game_over()
        if not self._is_game_over:
            self._timer += 1

            if self._timer >= 20:
                self._timer = 0

                cycles = cast.get_actors("cycles")
                for cycle in cycles:
                    cycle.grow_trail(1)