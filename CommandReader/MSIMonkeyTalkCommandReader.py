import os
import xml.etree.ElementTree

from CommandReader.MSICommandReader import MSICommandReader
from CommandReader.MSITestCommand import MSITestCommand

class MSIMonkeyTalkCommandReader(MSICommandReader):

    def readCommandFromFile(self, filename):
        current_path = os.path.dirname(__file__)
        abs_file_path = os.path.join(current_path, filename)
        root = xml.etree.ElementTree.parse(abs_file_path).getroot()
        self.getCommandsFromRoot(root)

    def getCommandsFromRoot(self, root):
        commandsArray = root.iter('dict')
        testCommands = []
        for command in commandsArray:
            testCommands.append(self.getCommandInfoFromCommand(command))

    def getCommandInfoFromCommand(self, command):
        argsKeyFound = False
        commandKeyFound = False
        testCommand = MSITestCommand()
        for child in command.iter():
            if argsKeyFound == True:
                testCommand.commandArgs = self.getArrayTextFromElementArray(child)
                argsKeyFound = False
            elif commandKeyFound == True:
                testCommand.commandName = child.text
                commandKeyFound = False
            elif child.text == "args":
                argsKeyFound = True
            elif child.text == "command":
                commandKeyFound = True

        print testCommand
        return testCommand

    def getArrayTextFromElementArray(self, elementArray):
        elementTextArray = []
        for element in list(elementArray):
             elementTextArray.append(element.text)
        return elementTextArray


    def __str__(self):
        return "MSIMonkeyTalkCommandReader"


def printElement(element):
    print element
    for child in element:
        printElement(child)

reader = MSIMonkeyTalkCommandReader()
root = reader.readCommandFromFile("../scripts/Basic.xml")
