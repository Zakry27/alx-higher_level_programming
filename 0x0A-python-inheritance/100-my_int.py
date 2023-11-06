#!/usr/bin/python3
"""the module with the Myin class"""


class MyInt(int):
    """the class that inherits from int"""

    def __init__(self, my_int):
        """to initialize value my_int"""

        self.my_int = my_int

    @property
    def my_int(self):
        return self.__my_int

    @my_int.setter
    def my_int(self, my_int):
        if type(my_int) is not int:
            raise TypeError("my_int must be an int")
        else:
            self.__my_int = my_int

    def __eq__(self, other):
        """the equal method"""

        if self.my_int == other:
            return False
        else:
            return True

    def __ne__(self, other):
            if self.my_int != other:
                return False
            else:
                return True
