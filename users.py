"""A set of classes to represent officers at the office."""

class User:
    """A simplet attempt to represent an individual"""    

    CompanyName = "Orange County Juvenile Probation Dept."

    def __init__(self, name, title):
        self.name = name
        self._title = title
        
    def __str__(self):
        """Print at statement describing the individual created"""
        return "Name = %s, Position = %s" %(self.name, self._title) 
    
    """@property
    def title(self):
        
        return self._title
    
    @title.setter
    def title(self, value):
        if value == 'JPO' or value == 'Chief' or value == 'Office Manager':
            self._title = value
        else:
            print("Position is invalid.  No changes made.")"""


class Staff(User):
    """Represents an Ordinary Line Officer at the office."""
    def __init__(self, name):
        super().__init__(name, title='Office Staff')

    def calculate_Comp(self):
        """Calculates Comptime for Office Staff at time-and-a-half."""
        rate = float(1.50)
        
        return 
    

class JPO(User):
    """Represents an Ordinary Line Officer at the Office."""
    def __init__(self, name):
        super().__init__(name, title='JPO')

    def calculate_Comp(self):
        """Calculates Comptime for JPOs at time-and-a-half."""
        rate = float(1.50)
        
        return 
            

class Chief(User):
    """Represents the Chief Juv Officer at the Office"""
    def __init__(self, name):
        super().__init__(name, title='Chief')
        
    def calculate_Comp(self):
        """Calculates Comptime for the Chief at Straight Time Value"""
        rate = float(1.00)
        
        return 

    
