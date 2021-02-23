class Road:
    def __init__(self, _length, _width, _asphalt):
        self._length = _length
        self._width = _width
        self._asphalt = _asphalt
        self._thickness = self._asphalt / 5

    def weight(self):
        return self._length * self._width * self._asphalt * self._thickness
r = Road(60, 300, 50)
print(r.weight())