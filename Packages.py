from datetime import datetime
# Create Package class


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, status, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.notes = notes
        self.track = {}
        self.time = datetime(2000, 1, 1, 8)

    # Gets the status of the package at the required time.
    def track_time(self, tracktime):
        if tracktime > self.time:
            return "Package ID: %d \t Weight = %d Kg \t Deliver to: %s %s %s, %d by %s. \t Status: %s" % (
                self.id, self.weight, self.address, self.city, self.state, self.zip, self.deadline, self.status)
        else:
            return "Package ID: %d \t Weight = %d Kg \t Deliver to: %s %s %s, %d by %s. \t Status: %s" % (
                self.id, self.weight, self.address, self.city, self.state, self.zip, self.deadline, self.track[tracktime.strftime("%H:%M")])

    def __str__(self):
        return "Package ID: %d \t Weight = %d Kg \t Deliver to: %s %s %s, %d by %s. \t Status: %s" % (
            self.id, self.weight, self.address, self.city, self.state, self.zip, self.deadline, self.status)


