"""

Description:
Module for housing utilities for creating influence maps
(basically mappings of features onto coordinates on the game map)
"""

import abc

import numpy as np

# Since the coordinates on the halite map are represented by real numbers,
# I need to decide a way to condense the representation of each coordinate
_HEIGHT_MULT = 5    # multiplier on map height size
_WIDTH_MULT = 5     # multiplier on map width size


class InfluenceMap(object, metaclass=abc.ABCMeta):
    """Base Class of Influence Map. All Influence Maps should
        inherit this to ensure that all influence maps share the
        same shape.
    """

    map_width = None
    map_height = None

    @classmethod
    def set_map_dimensions(cls, width, height):
        cls.map_width = width
        cls.map_height = height

    @classmethod
    def get_map(cls):
        if cls.map_width is None or cls.map_height is None:
            raise ValueError("Must set map dimensions before calling "
                             "initializing any InfluenceMap objects.")
        return np.zeros(
            (_HEIGHT_MULT * cls.map_height,
             _WIDTH_MULT * cls.map_width))

    def __init__(self):
        self._map = self.get_map()

    @abc.abstractmethod
    def update_map(self, game_data):
        pass

    @property
    def map(self):
        return self._map
