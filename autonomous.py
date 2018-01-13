""" collection of functions used to manage autonomous control """
from vision.visionmaster import VisionMaster


class Autonomous:
    """ isoltate autonomous code from robotpy, instantiate in robot init with field string"""
    UNKNOWN = 0
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3

    def __init__(self, robot_location, field_string):
        self.robot_location = robot_location  # set by physical switch or dashboard ?
        self.field_string = field_string
        self.vision = VisionMaster('0.0.0.0', 2)  # pull these values from some configuration

        self.close_switch = Autonomous.UNKNOWN
        self.scale = Autonomous.UNKNOWN
        self.far_switch = Autonomous.UNKNOWN
        self.parse_field_string(field_string)

        self.target = None

    def parse_field_string(self, field_string):
        """
        slice the string and set object properties for switch and scale locations and other stuff we get
        :param field_string:
        :return:
        """
        self.close_switch = field_string[0:4] # i have no idea what this string looks like obviously
        self.scale = field_string[0:4]
        self.far_switch = field_string[0:4]

    def target(self):
        """
        call from autonomous init in robotpy
        give all location information decide where to go
        :return:
        """
        self.target = None

    def periodic(self):
        """
        this is called by robotpy auto periodic
        decide
        """
        pass
