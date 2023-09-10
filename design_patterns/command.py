"""
Encapsulates a request as an object, thereby allowing
for parameterization of clients with queues, requests, and operations.
"""
from abc import ABC, abstractmethod

# Receiver classes (devices)
class TV:
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")

class Stereo:
    def turn_on(self):
        print("Stereo is ON")

    def turn_off(self):
        print("Stereo is OFF")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete command classes
class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.turn_on()

class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.turn_off()

# Remote Control
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, on_command, off_command):
        self.commands[slot] = {'on': on_command, 'off': off_command}

    def press_on_button(self, slot):
        self.commands[slot]['on'].execute()

    def press_off_button(self, slot):
        self.commands[slot]['off'].execute()

# Client code
tv = TV()
stereo = Stereo()

tv_on = TVOnCommand(tv)
tv_off = TVOffCommand(tv)

stereo_on = StereoOnCommand(stereo)
stereo_off = StereoOffCommand(stereo)

remote = RemoteControl()
remote.set_command(0, tv_on, tv_off)
remote.set_command(1, stereo_on, stereo_off)

remote.press_on_button(0)  # Turns on the TV
remote.press_off_button(0)  # Turns off the TV
remote.press_on_button(1)  # Turns on the Stereo
remote.press_off_button(1)  # Turns off the Stereo
