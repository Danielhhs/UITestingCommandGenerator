__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template


class UITestingTapCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = "ToolUtils.verifyAppear(.Any, iden: \"$targetID\", test: self)\nToolUtils.elementIdQuery(\"$targetID\").element.tap()\n"

    def generate(self):
        self.commandBody = Template(self.template).safe_substitute(targetID = self.command.commandTarget)