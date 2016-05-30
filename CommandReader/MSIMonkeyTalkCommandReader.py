import os
import xml.etree.ElementTree

from CommandReader.MSICommandReader import MSICommandReader
from CommandReader.MSITestCommand import MSITestCommand

class MSIMonkeyTalkCommandReader(MSICommandReader):

    def __init__(self):
        MSICommandReader.__init__(self)

    def readCommandFromFile(self, filename):
        root = xml.etree.ElementTree.parse(filename).getroot()
        return self.getCommandsFromRoot(root)

    def getCommandsFromRoot(self, root):
        commandsArray = root.iter('dict')
        testCommands = []
        for command in commandsArray:
            populatedCommand = self.getCommandInfoFromCommand(command)
            testCommands.append(populatedCommand)
            self.previousCommand = populatedCommand
        return testCommands

    def getCommandInfoFromCommand(self, command):
        argsKeyFound = False
        commandKeyFound = False
        actionTargetFound = False
        targetClassFound = False
        testCommand = MSITestCommand()
        for child in command.iter():
            if argsKeyFound == True:
                testCommand.commandArgs = self.getArrayTextFromElementArray(child)
                argsKeyFound = False

            elif commandKeyFound == True:
                testCommand.commandName = child.text
                if child.text == 'Screenshot':
                    testCommand.commandArgs.append(self.currentAction)
                else:
                    self.currentAction = child.text
                commandKeyFound = False

            elif actionTargetFound == True:
                if child.text != None:
                    testCommand.commandTarget = child.text
                actionTargetFound = False

            elif targetClassFound == True:
                if child.text != None:
                    testCommand.targetClass = child.text
                targetClassFound = False

            elif child.text == "args":
                argsKeyFound = True

            elif child.text == "command":
                commandKeyFound = True

            elif child.text == "monkeyID":
                actionTargetFound = True

            elif child.text == "className":
                targetClassFound = True

        if testCommand.commandName == "InputText" and self.previousCommand.commandName == "Tap":
            testCommand.commandArgs.append(self.previousCommand.commandTarget)
        if testCommand.commandName == "Tap" and testCommand.targetClass == "UIButton" and self.previousCommand.commandName == "InputText":
            self.previousCommand.commandArgs.append(testCommand.commandTarget)
        print testCommand
        return testCommand

    def getArrayTextFromElementArray(self, elementArray):
        elementTextArray = []
        for element in list(elementArray):
             elementTextArray.append(element.text)
        return elementTextArray


    def __str__(self):
        return "MSIMonkeyTalkCommandReader"

    def findLaunchURLFromCommands(self, commands):
        launchURL = ""
        for command in commands:
            if command.commandName == 'ConfigServer':
                launchURL = command.commandArgs[0]

        return launchURL



# reader = MSIMonkeyTalkCommandReader()
# root = reader.readCommandFromFile("../scripts/Basic.xml")
