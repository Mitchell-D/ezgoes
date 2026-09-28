class SatelliteProduct:
    def __init__(self, satellite:str=None, sensor:str=None,
            level:str=None, scan:str=None):
        self.satellite = satellite
        self.sensor = sensor
        self.level = level
        self.scan = scan

    def __iter__(self):
        for v in self._tup():
            yield v

    def _tup(self):
        return [self.satellite, self.sensor, self.level, self.scan]

    def __repr__(self):
        return f"{'-'.join(self._tup())}"
