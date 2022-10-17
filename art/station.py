from lib import Colour
from movement import station_map


def draw_station(current_room, ricky = None):
    # Python only creates a view into the stations, so I have to clone them
    # to individually format them. The copy() method in arrays is only a shallow copy.
    # I love Python :)
    rooms = [station.__copy__() for station in station_map]

    rooms[current_room-1].colour = Colour.YELLOW

    if ricky is not None:
        rooms[ricky - 1].colour = Colour.RED

    return f"""                          *
                    *
                        *   *   *

            *      ╔══{rooms[0]}══╗
                   ║      ║          *  *
                   {rooms[1]}     {rooms[2]}
                   ║      ║
      *            ║      ║
          ╔══{rooms[3]}════{rooms[4]}═════{rooms[5]}══{rooms[6]}══╗     *
          ║   ║    ║      ║       ║
          ║   ║    ║      ║  ╔══╗ ║    *
          {rooms[7]} {rooms[8]}════{rooms[9]}     {rooms[10]}═══{rooms[11]} {rooms[12]}
          ║  ║║    ║      ║  ║ ║  ║
          ║  ╚║════{rooms[14]}  *  ║  ║ ║  ║
          {rooms[13]}══╝           {rooms[15]}═╝ ╚══{rooms[16]}
   *
           *         *         *
              *               *"""
