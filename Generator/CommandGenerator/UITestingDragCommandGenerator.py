__author__ = 'huanghongsen'
from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template
import numbers

class UITestingDragCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = """//$comments
            XCUIApplication().sliders.element.adjustToNormalizedSliderPosition($targetValue)
            //dismiss Slider
            ToolUtils.verifyAppear(.Any, iden: "dismiss popup", test: self)
            ToolUtils.elementIdQuery("dismiss popup").element.tap()\n"""
        self.comments = "Update Slider Value"

    def generate(self):
        targetValue = self.getTargetValue()
        self.commandBody = Template(self.template).safe_substitute(comments = self.comments, targetValue = targetValue)

    def getTargetValue(self):
        targetValue = 0.5
        if len(self.command.commandArgs) == 1 and isinstance(self.command.commandArgs[0], numbers.Number):
            targetValue = self.command.commandArgs[0]