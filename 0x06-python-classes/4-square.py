class Square:
    """square with private instance attribute size"""
    def __init__(self, size=0):
        """Lenght of the side of a square"""
        self.size = size

    @property
    def size(self):
        """current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """setters are the methods"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method returns current sqr area"""
        return self.__size ** 2
