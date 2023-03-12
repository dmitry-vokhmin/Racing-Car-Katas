from collections import defaultdict


class Leaderboard:

    def __init__(self, races):
        self.races = races

    def driver_points(self):
        driver_points = defaultdict(int)
        for race in self.races:
            for driver in race.results:
                name = race.driver_name(driver)
                driver_points[name] += race.points(driver)
        return driver_points

    def driver_rankings(self):
        rankings = sorted(self.driver_points().items(), key=lambda x: x[1], reverse=True)
        return [name for name, points in rankings]


class Driver:
    def __init__(self, name, country):
        self.name = name
        self.country = country


class SelfDrivingCar(Driver):
    def __init__(self, algorithm_version, company):
        name = "Self Driving Car - {} ({})".format(company, algorithm_version)
        super().__init__(name, None)


class Race:
    _points = [25, 18, 15]

    def __init__(self, name, results):
        self.name = name
        self.results = results
        self.driver_names = {}
        for driver in results:
            self.driver_names[driver] = driver.name

    def points(self, driver):
        return self._points[self.results.index(driver)]

    def driver_name(self, driver):
        return self.driver_names[driver]
