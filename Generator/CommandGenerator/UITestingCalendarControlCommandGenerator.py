__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from string import Template
import string

class UITestingCalendarControlCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.monthComponentID = ""
        self.dateComponentID = ""
        self.yearComponentID = ""
        self.template = """//$comments
            ToolUtils.verifyAppear(.Any, iden: \"$month\", test: self)
            ToolUtils.elementIdQuery(\"$month\").element.swipeUp()
            ToolUtils.verifyAppear(.Any, iden: \"$date\", test: self)
            ToolUtils.elementIdQuery(\"$date\").element.swipeDown()
            ToolUtils.verifyAppear(.Any, iden: \"$year\", test: self)
            ToolUtils.elementIdQuery(\"$year\").element.swipeUp()\n\n"""
        self.comments = "Calendar Control"

    def generate(self):
        self.prepareDateInfo()
        self.commandBody = Template(self.template).safe_substitute(comments = self.comments, month = self.monthComponentID, date = self.dateComponentID, year = self.yearComponentID)

    def prepareDateInfo(self):
        dateString = self.command.commandArgs[0]
        dateComponents = string.split(dateString, '-')
        self.dateComponentID = dateComponents[2]
        self.yearComponentID = dateComponents[0]
        self.monthComponentID = self.monthDescriptionFromNumber(dateComponents[1])

    def monthDescriptionFromNumber(self, month):
        if month == '01' or month == '1':
            return "January"
        elif month == '02' or month == '2':
            return "February"
        elif month == '03' or month == '3':
            return "March"
        elif month == '04' or month == '4':
            return "April"
        elif month == '05' or month == '5':
            return "May"
        elif month == '06' or month == '6':
            return "June"
        elif month == '07' or month == '7':
            return "July"
        elif month == '08' or month == '8':
            return "August"
        elif month == '09' or month == '9':
            return "September"
        elif month == '10':
            return "October"
        elif month == '11':
            return "November"
        elif month == '12':
            return "December"