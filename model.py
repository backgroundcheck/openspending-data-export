

class Dataset(object):
    
    def __init__(self):
        self.id = None
        self.label = None
        self.model = None
        self.fields = None


class Field(object):
    pass


class Model(object):
    
    def __init__(self):
        self.variables = []
        self.measures = []
        self.dimensions = []


class AttributeType(object):

    def __init__(self):
        self.id = None
        self.label = None


class Attribute(object):
    
    def __init__(self):
        self.type = None
        self.mapping = None


class Variable(object):
    pass


class Measure(Variable):
    
    def __init__(self):
        self.attribute = None


class Level(object):

    def __init__(self):
        self.id = None
        self.label = None
        self.attributes = None
        self.hierarchies = None


class Hierarchy(set):
    
    def __init__(self):
        pass


class Dimension(Variable):
    pass


