#!/usr/bin/python3
import json
import turtle

"""Creating a base model"""

class Base:
    """adding a private class attribute

    Attrributes:
        __nb_objects (int): the number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        checking if id is not none

        assign the public instance id with
        the argument value

        otherwise, increment the __nb_objects

        and assign the value to the public instance
        attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation

        args:
            list_dictionaries: dict to turn to json
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                return [cls.create(**obj) for obj in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}\n")
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    file.write(f"{obj.id},{obj.size},{obj.x},{obj.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                instances = []
                for line in file:
                    data = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls(*map(int, data))
                    elif cls.__name__ == "Square":
                        instance = cls(*map(int, data[0:2]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all rectangles and squares using Turtle graphics."""
        # Create a Turtle screen
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.setup(width=800, height=600)
        screen.tracer(0)

        # Create a Turtle object
        pen = turtle.Turtle()
        pen.speed(0)

        # Draw rectangles
        pen.color("blue")
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.setheading(0)  # Ensure orientation
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)

        # Draw squares
        pen.color("red")
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.setheading(0)  # Ensure orientation
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        # Close the Turtle graphics window on click
        screen.onclick(turtle.bye)

        # Update the screen
        screen.update()

        # Keep the window open
        turtle.done()
