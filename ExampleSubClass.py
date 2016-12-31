import ExampleClass

class moreComplex(ExampleClass.Complex):
    def __init__(self, realpart, imagpart, extra):      # override instantiation method
        self.extra = extra                              # capture extra init info
        ExampleClass.Complex.__init__(self, realpart, imagpart)         # call init on parent class
