class Complex:
    classVar = []     # This variable would be shared by all instances of the class

    def __init__(self, realpart, imagpart):      # run automatically when new instance is created
        self.r = realpart         # This is how you create an instance variable, local to each object
        self.i = imagpart

    def mag(self):                  # when actually calling this method on an instance of the class, self is passed automatically, so you just say obj.mag()
        return ((self.r**2) + (self.i**2))**0.5
