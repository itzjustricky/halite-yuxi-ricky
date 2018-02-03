import hlt
import logging
from data_boss import algorithm

# GAME START
# Here we define the bot's name as Settler and initialize the game, including communication with the Halite engine.
game = hlt.Game("Settler")
# Then we print our start message to the logs
logging.info("Starting my Settler bot!")

map_history = []

while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()

	# Store the history of the game map
    map_history.append(game_map)

    # Here we define the set of commands to be sent to the Halite engine at the end of the turn
    command_queue = algorithm.dock_planet(map_history)
    
    game.send_command_queue(command_queue)
    # TURN END
# GAME END
