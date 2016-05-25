__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from Generator.CommandGenerator.UITestingScreenShotCommandGenerator import UITestingScreenShotCommandGenerator
from Generator.CommandGenerator.UITestingBrowseInCommandGenerator import UITestingBrowseInCommandGenerator
from CommandReader.MSITestCommand import MSITestCommand

class UITestingCommandGeneratorFactory:
    @staticmethod
    def commandGeneratorForCommand(command):
        commandName = command.commandName
        if commandName == 'BrowseIn':
            return UITestingBrowseInCommandGenerator(command)
        elif commandName == 'Screenshot':
            return UITestingScreenShotCommandGenerator(command)
        else:
            return UITestingCommandGenerator(command)