__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template

class UITestingSwitchCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = "//$comments\nToolUtils.verifyAppear(.Switch, iden: \"$targetID\", test: self)\nToolUtils.elementTypeIdQuery(.Switch, id: \"$targetID\").element.tap()\n"
        self.comments = "Switch Button"

    def generate(self):
        self.commandBody = Template(self.template).safe_substitute(comments = self.comments, targetID = self.getTargetID())

    def getTargetID(self):
        if len(self.command.commandTarget) > 0:
            return self.command.commandTarget
        else:
            return self.command.commandArgs[0]