class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved. Otherwise, all attributes must
        be retrieved.
        """
        if attrs is None:
            return self.__dict__

        my_dict = {}
        for key in attrs:
            if isinstance(key, str) and key in self.__dict__:
                my_dict[key] = self.__dict__[key]

        return my_dict
