__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from CommandReader.MSITestCommand import MSITestCommand
import StringConstants
from string import Template

class UITestingScreenShotCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = "writeScreenshotLog(XCTest.SupportAction.$action, \"$actionname\", \"$targetfilename\")\n"

    def generate(self):
        self.commandBody = Template(self.template).safe_substitute(action = self.actionFromActionName(self.command.commandArgs[1]), actionname = self.command.commandArgs[1], targetfilename=self.command.commandArgs[0])
        self.commandBody += StringConstants.LINE_BREAK

    def actionFromActionName(self, actionName):
        if actionName == 'Tap' or actionName == 'Switch':
            return "Tap"
        elif actionName == 'BrowseIn':
            return "OpenDocument"
        else:
            return "unKnown"

# command = MSITestCommand()
# command.commandName = "Screenshot"
# command.commandArgs = ["Sanity_FIeld"]
# generator = UITestingScreenShotCommandGenerator(command)
# generator.generate()
# print generator.commandBody