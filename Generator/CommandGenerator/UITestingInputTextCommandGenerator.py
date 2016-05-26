__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template

class UITestingInputTextCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.comments = "Input Text"
        self.template = """//$comments
            ToolUtils.verifyAppear(.Any, iden: \"$originalText\", test: self)
            ToolUtils.elementIdQuery(\"$originalText\").element.tap()
            //modify Text Area - $originalText to $newText
            $veryfyDoneButton
            ToolUtils.elementTypeIdQuery(.TextView, id: \"$originalText\").element.TypeText(\"$newText\")\n"""

    def generate(self):
        originalText = self.getOriginalText()
        newText = self.getNewText()
        verifyDoneButton = self.getVerifyDoneButtonText()
        self.commandBody = Template(self.template).safe_substitute(originalText = originalText, newText = newText, comments = self.comments, veryfyDoneButton = verifyDoneButton)

    def getVerifyDoneButtonText(self):
        if len(self.command.commandArgs) == 3:
            template = "ToolUtils.verifyAppear(.Button, iden: \"$doneButton\", test: self)\n"
            text = Template(template).safe_substitute(doneButton = self.command.commandArgs[2])
            return text
        return ""

    def getOriginalText(self):
        if len(self.command.commandArgs) >= 2:
            return self.command.commandArgs[1]
        return ""

    def getNewText(self):
        if len(self.command.commandArgs) >= 1:
            return self.command.commandArgs[0]
        return ""