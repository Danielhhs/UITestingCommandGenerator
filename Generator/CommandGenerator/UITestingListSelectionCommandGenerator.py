__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import  Template

class UITestingListSelectionCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = """//$comments
            ToolUtils.verifyAppear(.Any, iden: \"$targetID\", test: self)
            ToolUtils.elementIdQuery(\"$targetID\").element.tap()
            //modify List from to $targetValue
            ToolUtils.verifyAppear(.Any, iden: \"$targetValue\", test: self)
            ToolUtils.elementIdQuery(\"$targetValue\").element.tap()\n"""
        self.comments = "Select Item In List"

    def generate(self):
        targetID = self.getTargetID()
        targetValue = self.getTargetValue()
        self.commandBody = Template(self.template).safe_substitute(comments = self.comments, targetID = targetID, targetValue = targetValue)

    def getTargetID(self):
        if len(self.command.commandArgs) == 1:
            return ""
        else :
            return self.command.commandArgs[1]

    def getTargetValue(self):
        return self.command.commandArgs[0]