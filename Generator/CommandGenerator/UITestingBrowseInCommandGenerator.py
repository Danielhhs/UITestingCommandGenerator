__author__ = 'huanghongsen'

from Generator.CommandGenerator.UTestingCommandGenerator import UITestingCommandGenerator
from CommandReader import  MSITestCommand

class UITestingBrowseInCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        self.command = command
        self.commandBody = ""

    def generate(self):
        self.command