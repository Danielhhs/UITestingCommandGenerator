__author__ = 'huanghongsen'

from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from CommandReader.MSITestCommand import  MSITestCommand
from string import Template
import string

class UITestingBrowseInCommandGenerator(UITestingCommandGenerator):
    def __init__(self, command):
        UITestingCommandGenerator.__init__(self, command)
        self.template = "//$comments\nFolder.browseIn(\"$folderpath\", test: self)\n\n"
        self.folderPath = ""
        self.comments = "Browse In Folder"

    def generate(self):
        self.convertFolderPath()
        if len(self.command.comments) > 0:
            self.commandBody += "//"
            self.commandBody += self.command.comments
            self.commandBody += "\n"
        self.commandBody += Template(self.template).safe_substitute(comments = self.comments, folderpath=self.folderPath)

    def convertFolderPath(self):
        originalPath = self.command.commandArgs[0]
        pathComponents = originalPath.split('\\')
        self.folderPath = string.join(pathComponents, '//')

# command = MSITestCommand()
# command.commandName = "BrowseIn"
# command.commandArgs = ['Shared Library\Transactions(SingleGridSource=False)\Test Suite\Data Input Control\Field+Grid']
# command.comments = "adsaasdfasgawrgaerw"
# generator = UITestingBrowseInCommandGenerator(command)
# generator.generate()
# print generator.commandBody

