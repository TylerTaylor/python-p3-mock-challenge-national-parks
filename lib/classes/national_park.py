class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        
        if isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors
    
    def total_visits(self):
        # Returns the total number of times that park has been visited
        return len(self._trips)
    
    def best_visitor(self):
        # Returns the Visitor who has visited the park the most

        # Create a baseline / starting point to compare with:
        max_visitor = None
        max_visits = 0

        for visitor in self._visitors:
            # for each trip in our trips list
            #   check if the associated visitor is the visitor from our current loop iteration

            visits = len([trip for trip in self._trips if trip.visitor == visitor])
            # below is the same general logic, just flipped around a bit
            # visits = len([trip for trip in visitor._trips if trip._national_park == self])

            if visits > max_visits:
                max_visitor = visitor
                max_visits = visits
        
        return max_visitor

        pass