__author__ = 'huanghongsen'
from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template
import string

class UITestingTimeControlCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.comments = "Select Time"
        self.template = """//$comments
            ToolUtils.verifyAppear(.Any, iden: \"$targetID\", test: self)
            ToolUtils.elementIdQuery(\"$targetID\".element.tap())
            //modify Time to $targetTime
            ToolUtils.verifyAppear(.Any, iden: \"$targetHour\", test: self)
            ToolUtils.elementIdQuery(\"$targetHour\").element.swipeDown()
            ToolUtils.verifyAppear(.Any, iden: \"$targetMinute\", test: self)
            ToolUtils.elementIdQuery(\"$targetMinute\").element.swipeUp()
            ToolUtils.verifyAppear(.Any, iden: \"$targetDay\", test: self)
            ToolUtils.elementIdQuery(\"$targetDay\").element.swipeDown()\n"""
        self.targetHour = ""
        self.targetMinutes = ""
        self.targetDay =""
        self.targetTime = ""

    def generate(self):
        targetID = self.getTargetID()
        self.prepareTargetTimeComponents()
        self.commandBody = Template(self.template).safe_substitute(comments = self.comments, targetTime = self.targetTime, targetID = targetID, targetHour = self.targetHour, targetMinute = self.targetMinutes, targetDay = self.targetDay)

    def getTargetID(self):
        if len(self.command.commandArgs) == 1:
            return ""
        else:
            return self.command.commandArgs[1]

    def prepareTargetTimeComponents(self):
        self.targetTime = self.command.commandArgs[0]
        timeComponents = string.split(self.targetTime, ' ')
        self.targetDay = timeComponents[1] + " "
        time = timeComponents[0]
        timeComponents = string.split(time, ':')
        self.targetHour = timeComponents[0] + " o'clock"
        self.targetMinutes = timeComponents[1]
        if len(self.targetMinutes) == 1:
            self.targetMinutes = "0" + self.targetMinutes
        self.targetMinutes += " minutes"