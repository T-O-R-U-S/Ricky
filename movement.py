from random import randint

from lib import Colour

MODULES = 17


class Room:
    def get_moves(self):
        return  [   module for module in
                        self.moves
                    if not station_map[module - 1].shut
                ]

    def __init__(self, number, moves):
        # Does the room contain an info panel?
        self.info_panel = False
        # Has the player visited the room before?
        self.marked = False
        # Is the module shut?
        # 0 = not shut
        # 4 = shut for 4 more moves
        self.shut = 0
        # Room number
        self.number = number
        # If the room doesn't have a vent shaft, the number is zero.
        self.vent_shaft = 0
        # One in ten chance to have a vent shaft.
        if randint(0, 10) == 0:
            self.vent_shaft = randint(1, MODULES)
        # One in four chance to have an info panel
        if randint(0, 4) == 0:
            self.info_panel = True
        # Which rooms you can move to from here.
        self.moves = moves
        self.colour = Colour.GREEN

    def __format__(self, _):
        if self.shut > 0:
            self.colour = Colour.PURPLE
        elif self.shut == 0 and self.colour == Colour.PURPLE:
            self.colour = Colour.GREEN

        if not self.shut and self.vent_shaft and self.marked:
            self.colour = Colour.DEFAULT

        if not self.shut and self.info_panel and self.marked:
            self.colour = Colour.BLUE

        return f"{self.colour}{self.number:02d}{Colour.DEFAULT}"

    def __repr__(self):
        return format(self)

    def __str__(self):
        return format(self)

    def __copy__(self):
        room = Room(self.number, self.moves.copy())

        room.marked = self.marked

        room.shut = self.shut

        room.vent_shaft = self.vent_shaft

        room.info_panel = self.info_panel

        room.colour = self.colour

        return room


station_map = [
    Room(1, [2, 3]),
    Room(2, [1, 5]),
    Room(3, [1, 6]),
    Room(4, [5, 8, 9]),
    Room(5, [2, 4, 6, 10]),
    Room(6, [3, 5, 7, 11]),
    Room(7, [6, 13]),
    Room(8, [4, 9, 14]),
    Room(9, [4, 10, 14, 15]),
    Room(10, [5, 9, 15]),
    Room(11, [6, 12, 16]),
    Room(12, [11, 16, 17]),
    Room(13, [7, 17]),
    Room(14, [8, 9]),
    Room(15, [9, 10]),
    Room(16, [11, 12]),
    Room(17, [12, 13])
]
