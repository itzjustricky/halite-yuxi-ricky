"""

Description:
Module for housing utilities for creating influence maps
(basically mappings of features onto coordinates on the game map)
"""

import abc
from collections import namedtuple

import numpy as np

# Since the coordinates on the halite map are represented by real numbers,
# I need to decide a way to condense the representation of each coordinate
_HEIGHT_MULT = 1    # multiplier on map height size
_WIDTH_MULT = 1     # multiplier on map width size


MapDimensions = namedtuple("MapDimensions", ["width", "height"])


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
    def get_map_shape(cls):
        if cls.map_width is None or cls.map_height is None:
            raise ValueError("Must set map dimensions before calling "
                             "initializing any InfluenceMap objects.")
        return MapDimensions(
            width=_WIDTH_MULT * cls.map_width,
            height=_HEIGHT_MULT * cls.map_height)

    def __init__(self):
        self._map = self.init_map()

    @property
    def map(self):
        return self._map

    def init_map(self, *args, **kwargs):
        map_shape = self.get_map_shape()
        return np.zeros((map_shape.width, map_shape.height))

    @abc.abstractmethod
    def update_map(self, game_data):
        pass
