import Exceptions

class Variable () :
    def __init__(self, domain, name=None) :
        """ Initialize a new variable with the given domain and name. """

        self._name = name
        self._domain = domain
        self._options = set(domain)
        self._solved = False
        self._value = None

    def reset (self) :
        """ Restore the list of options to the entire domain.

        This is used when (for example) a constraint is deleted.
        """

        self._options = set(domain)
        self._solved = False
        self._value = None

    def set (self, value) :
        """ Set the variable to a given value. """

        if value not in self._domain :
            raise Exceptions.UnsupportedValue()
        
        if value not in self._options :
            raise Exceptions.NoSolution()

        self._options = set((value))
        self._solved = True
        self._value = value

    def forbidValue (self, value) :
        """ Remove value from valid options. Return whether found. """
        
        if value in self._options :
            self._options.remove(value)
            if len(self._options) == 0 :
                raise Exceptions.NoSolution()
            if len(self._options) == 1 :
                self.set(self._options[0])
            return True
        return False

    def getOptions (self) :
        return self._options.copy()

    def getBranching (self) :
        return len(self._options)
