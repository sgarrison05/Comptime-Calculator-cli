"""A set of classes to represent officers at the office."""

class User:
    """A simple attempt to represent an individual"""    

    CompanyName = "Orange County Juvenile Probation Dept."

    def __init__(self, name, _title):
        self.name = name
        self._title = _title
        
    def __str__(self):
        """Print at statement describing the individual created"""
        return "Name = %s, Position = %s" %(self.name, self._title) 
    

class Staff(User):
    """Represents Support Staff at the office."""

    # Get the parent attributes with super().__init__ 
    def __init__(self, name, rate:float=1.50, _title='Office Staff'):
        super().__init__(name, _title)
        self.rate = rate

class JPO(User):
    """Represents an Ordinary Line Officer at the Office."""
    
    def __init__(self, name, rate:float=1.50, _title='JPO'):
        super().__init__(name, _title)
        self.rate = rate
        

class Chief(User):
    """Represents the Chief Juv Officer at the Office"""

    def __init__(self, name, rate:float=1.00, _title='Chief'):
        super().__init__(name, _title)
        self.rate = rate
    

    
