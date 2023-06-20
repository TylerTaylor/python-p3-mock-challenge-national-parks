
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        # We need to create our relationships here
        self.visitor.trips(self)
        self.visitor.national_parks(self.national_park)
        # visitor.national_parks(national_park)
        
        national_park.trips(self)
        national_park.visitors(visitor)

    def get_visitor(self):
        return self._visitor

    def set_visitor(self, visitor):
        # Must be of type Visitor
        from classes.visitor import Visitor

        if visitor and isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception

    visitor = property(get_visitor, set_visitor)

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        from classes.national_park import NationalPark

        if national_park and isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception
