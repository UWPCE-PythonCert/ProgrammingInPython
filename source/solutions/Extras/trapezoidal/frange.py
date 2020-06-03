# the index method takes an object and returns its index equivalent.
from operator import index


class frange:
    """
    An object like range(), but for floating point numbers
    """

    def __init__(self, start, stop, num_steps=100):
        """
        create an frange object.

        An iterator that returns a sequence of values from start
        to stop inclusive.

        :param start: The first value in the series
        :param stop: The last value in the series

        :param num=100: the number of intervals in the series.

        This is designed to work as much as possible like the range()
        builtin, except:

        * Both start and stop are required -- there's no obvious default

        * It's a closed interval on both ends -- both start and stop are included.

        * The total number of items is num_steps + 1. This is because the
          end value is included, and num_steps is the number of intervals,
          not the number of values. This makes the logic easier for a "round"
          interval:

          list(frange(0, 1, 5)) == [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        """
        if num_steps == 0:
            raise ValueError("frange() arg 3 must not be zero")
        self.start = float(start)
        self.stop = float(stop)
        self.num_steps = int(num_steps)
        self._delta = (self.stop - self.start) / num_steps
        if self._delta == 0.0:
            raise ValueError("start and stop must be different")

    def __repr__(self):
        return "frange({!r}, {!r}, {!r})".format(self.start,
                                                 self.stop,
                                                 self.num_steps)

    def __eq__(self, other):
        try:
            return (self.start == other.start and
                    self.stop == other.stop and
                    self.num_steps == other.num_steps
                    )
        except AttributeError:
            return False

    def __len__(self):
        return self.num_steps + 1

    def __getitem__(self, ind):
        # process a slice:
        # fixme: might want to round a bit when making a slice:
        # http://code.activestate.com/recipes/578114-round-number-to-specified-number-of-significant-di/
        if isinstance(ind, slice):
            print("slice is:", ind)
            if ind.step is not None:
                raise ValueError("frange does not support slicing with a step")
            istart, istop, _ = ind.indices(len(self))
            start = self.start + (istart * self._delta)
            stop = self.stop - ((self.num_steps + 1 - istop) * self._delta)
            num_steps = istop - istart - 1
            return frange(start, stop, num_steps)
        ind = index(ind)
        if ind < 0:
            ind += (self.num_steps + 1)
        if ind > self.num_steps or ind < 0:
            raise IndexError
        val = self.start + (self._delta * ind)
        return val
