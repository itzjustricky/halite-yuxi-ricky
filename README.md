# halite-yuxi-ricky
A winter halite pursuit.

hlt: package used for communication with game; get game updates from here
├── collision.py: contains one function (intersect_segment_circle) to see "Test whether a line segment and circle intersect."
├── constants.py: store constant variables that describe attributes of objects in world
├── entity.py:
    ▶ Entity: Baseclass of all objects in game; all entities possess
        a position, radius, health, an owner and an id.
    ▶ Planet: entity to represent a planet on game map
    ▶ Ship: entity to represent a ship in the game map
    ▶ Position: entity to represent coordinate
├── game\_map.py:
    ▶ Map: houses the current game information/metadata.
    ▶ Player: object containing information on player id and ships
├── __init__.py
└── networking.py: module containing Game class used to interface with game
