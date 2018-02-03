"""

Description:
Module containing influence maps on
different regions of the map.

"""

from ..influence_map import InfluenceMap


class RegionalPower(InfluenceMap):

    def update_map(self, game_data):
        pass


class EnemyStrength(RegionalPower):

    def update_map(self, game_data):
        pass


class OurStrength(RegionalPower):

    def update_map(self, game_data):
        pass
