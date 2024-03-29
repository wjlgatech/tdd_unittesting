from ast import Num


class Number:
    """
    Wraps a value of type float in an object.

    Implementes basic math operations:
        - addition
        - subtraction
        - division
        - multiplication
        

    Implemented basic comparision:
        - equality
        - greater than
        - less than
    """

    def __init__(self, value):
        """
        Set value in an object in value attribute.

        For a given 'not float' value raises TypeError.

        :param value : value  of the Object.
        :param type value : int
        """
        try:
            float(value)
            self.value = value
        except ValueError:
            raise TypeError

    def __add__(self, other):
        """
        Returns sum of two objects.

        :param self: Object which calls '+' (adding operator)
        :param other : other object of the class.
        """
        return Number(self.value + other.value)

    def __sub__(self, other):
        """
        Returns subtraction of two objects.

        :param self: Object which calls '-' (subtract operator)
        :param other : other object of the class.

        For the case where other value is greater than the self value raises ValueError.
        """
        if self.value - other.value < 0:
            raise ValueError
        return Number(self.value - other.value)

    def __mul__(self, other):
        """
        Returns multiplication of two objects.

        :param self: Object which calls '*' (multiplication operator)
        :param other : other object of the class.
        """
        return Number(self.value * other.value)

    def __truediv__(self, other):
        """
        Returns division of two objects.

        :param self: Object which calls '/' (division operator)
        :param other : other object of the class.

        For the case where other value is 0 (zero) raises ZeroDivisionError.
        """
        return Number(self.value / other.value)

    

    def __eq__(self, other):
        """
        Compares two numbers and returns True if they are equals, otherwise returns False.

        :param self: Object which calls '==' (double equals operator)
        :param other : other object of the class.
        """
        return self.value == other.value

    def __gt__(self, other):
        """
        Compares two numbers and returns True if the first number is greater than the second, otherwise returns False.

        :param self: Object which calls >' (greater operator)
        :param other : other object of the class.
        """
        return self.value > other.value

    def __lt__(self, other):
        """
        Compares two numbers and returns True if the first number is less than the second, otherwise returns False.

        :param self: Object which calls '<' (less operator)
        :param other : other object of the class.
        """
        return self.value < other.value

    def __repr__(self):
        return f"Number({self.value})"
