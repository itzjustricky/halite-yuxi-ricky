"""

Description:
Module containing influence maps on
different regions of the map.

"""

from ..influence_map import InfluenceMap
from ..influence_map import MapDimensions


def measure_players_power(ship: dict, map_size: MapDimensions):
    """Measure the power of a player in each region of map by counting
        the number of ships within one turn away on each coordinate.

    :param ships_data: meta-data on each ship of one player
    :param map_size: size of the map
    :returns: 2d repr. of power of player
    """
    pass


class RegionalPower(InfluenceMap):

    def update_map(self, game_data):
        pass


class EnemyStrength(RegionalPower):

    def update_map(self, game_data):
        pass


class OurStrength(RegionalPower):

    def update_map(self, game_data):
        pass
