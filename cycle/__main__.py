from game.casting.cast import Cast
from game.casting.players import Players
from game.casting.score import Score
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.actors_action import ActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

def main():
    
    # # create the cast
    cast = Cast()
    setup = Players()
    setup.replay(cast)
    score1 = Score("player1")
    score2 = Score("player2")
    cast.add_actor("scores", score1)
    cast.add_actor("scores", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(keyboard_service, setup))
    script.add_action("update", ActorsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()