# Create a Truck class
class Truck:
    def __init__(self, name, mileage):
        self.route = {}
        self.name = name
        self.mileage = mileage
        self.track = {}

    def set_route(self, route):
        self.route = route

    def __str__(self):
        s = ""
        s += self.name
        s += "- Left Hub: " + self.track['left'] + "\t Packages: "
        s += str(self.track['packages'])[1:-1] + "\t Return Hub: " + self.track['arrived'] + "\t"
        return s
