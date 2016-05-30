__author__ = 'huanghongsen'
from CommandReader.MSICommandReader import MSICommandReader
import xml.etree.ElementTree
from CommandReader.MSITestCommand import MSITestCommand

class MSIInputCommandReader(MSICommandReader):
    def __init__(self):
        MSICommandReader.__init__(self)
        self.testcaseName = ""
        self.launchURL = ""
        self.commands = []

    def readCommandFromFile(self, file):
        root = xml.etree.ElementTree.parse(file)
        self.getCommandsFromRoot(root)
        return self.commands

    def getCommandsFromRoot(self, root):
       for child in root.iter():
            if child.tag == 'testcaseName':
                self.testcaseName = child.text
            elif child.tag == 'launchURL':
                self.launchURL = child.text
            elif child.tag == 'commands':
                self.getCommandsFromNode(child)

    def getCommandsFromNode(self, node):
        commandNodes = node.iter('command')
        for commandNode in commandNodes:
            command = MSITestCommand()
            for child in commandNode:
                if child.tag == 'name':
                    command.commandName = child.text
                elif child.tag == 'arg':
                    command.commandArgs.append(child.text)
            self.commands.append(command)
        return

    def findLaunchURLFromCommands(self, commands):
       return self.launchURL