import sys
import tkinter
import unittest

class Planets:
    def __init__(self, name="", mass=0, distance=0, moons=""): 
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons

class Moons:
    def __init__(self, name="", planet=""): 
        self.name = name
        self.planet = planet
