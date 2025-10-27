class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}  # {id: (station, time)}
        self.journey_stats = defaultdict(lambda: [0, 0])  # {(start, end): [total_time, count]}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins[id]
        route = (start_station, stationName)
        travel_time = t - check_in_time
        
        # Update statistics using defaultdict
        self.journey_stats[route][0] += travel_time
        self.journey_stats[route][1] += 1
        
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.journey_stats[route]
        return total_time / count