class Constraint () :
    def __init__ (self, variables, name=None) :
        self._variables = variables
        self._name = name

    def __call__ (self) :
        return []

    
    def getVariables (self) :
        return self._variables.copy()

    def getBranching (self) :
        return None
