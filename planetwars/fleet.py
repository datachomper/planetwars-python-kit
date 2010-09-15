from planetwars.player import PLAYER_MAP
from planetwars.util import TypedSetBase
from operator import attrgetter
from itertools import groupby

class Fleet(object):
    def __init__(self, universe, id, owner, ship_count, source, destination, trip_length, turns_remaining):
        self.universe = universe
        self.id = int(id)
        self.owner = PLAYER_MAP.get(int(owner))
        self.ship_count = int(ship_count)
        self.source = self.universe._planets.get(int(source))
        self.destination = self.universe._planets.get(int(destination))
        self.trip_length = int(trip_length)
        self.turns_remaining = int(turns_remaining)

    def __repr__(self):
        return "<F(%d) #%d %s -> %s ETA %d>" % (self.id, self.ship_count, self.source, self.destination, self.turns_remaining)

class Fleets(TypedSetBase):
    """Represents a set of Fleet objects.
    All normal set methods are available. Additionaly you can | (or) Fleet objects directly into it.
    Some other convenience methods are available (see below).
    """
    accepts = (Fleet, )

    @property
    def ship_count(self):
        """Returns the ship count of all Fleet objects in this set"""
        return sum(f.ship_count for f in self)

    def arrivals(self, reverse=False):
        """Returns an iterator that yields tuples of (turns_remaining, Fleets)
        for all Subfleets that arrive in this many turns in ascending order
        (use reverse=True for descending).
        """

        turn_getter = attrgetter("turns_remaining")
        for k, fleets in groupby(sorted(self, key=turn_getter, reverse=reverse), turn_getter):
            yield (k, Fleets(fleets))
