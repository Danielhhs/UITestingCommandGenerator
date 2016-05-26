__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from Generator.CommandGenerator.UITestingScreenShotCommandGenerator import UITestingScreenShotCommandGenerator
from Generator.CommandGenerator.UITestingBrowseInCommandGenerator import UITestingBrowseInCommandGenerator
from Generator.CommandGenerator.UITestingTapCommandGenerator import UITestingTapCommandGenerator
from Generator.CommandGenerator.UITestingSwitchCommandGenerator import UITestingSwitchCommandGenerator
from Generator.CommandGenerator.UITestingCalendarControlCommandGenerator import UITestingCalendarControlCommandGenerator
from Generator.CommandGenerator.UITestingDragCommandGenerator import UITestingDragCommandGenerator

from CommandReader.MSITestCommand import MSITestCommand

class UITestingCommandGeneratorFactory:
    @staticmethod
    def commandGeneratorForCommand(command):
        commandName = command.commandName
        if commandName == 'BrowseIn':
            return UITestingBrowseInCommandGenerator(command)
        elif commandName == 'Screenshot':
            return UITestingScreenShotCommandGenerator(command)
        elif commandName == 'Tap':
            return UITestingTapCommandGenerator(command)
        elif commandName == 'Switch':
            return UITestingSwitchCommandGenerator(command)
        elif commandName == 'EnterDate':
            return UITestingCalendarControlCommandGenerator(command)
        elif commandName == 'Drag':
            return UITestingDragCommandGenerator(command)
        else:
            return UITestingCommandGenerator(command)