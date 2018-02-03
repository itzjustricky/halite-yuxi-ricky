"""

Description:
Module containing functions to parse the json
files of game data
"""

import json


def parse_game_data(game_data_path: str):
    """Parse the game data and organize the data

    :param game_data_path: path to the location of the json file
        recording the state of the game per turn
    """
    with open(game_data_path) as fh:
        game_data = json.load(fh)

    static_data = {     # data that does not change per move
        k: game_data[k]
        for k in ["num_players", "num_frames", "stats",
                  "seeds", "planets", "constants"]}
    moves_data = game_data["moves"]
    frames_data = game_data["frames"]

    return static_data, moves_data, frames_data


# TODO:
def parse_one_frame(frame_data):
    pass
