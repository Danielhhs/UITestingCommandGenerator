from CommandReader.MSIMonkeyTalkCommandReader import MSIMonkeyTalkCommandReader
from CommandReader.MSITestCommand import MSITestCommand
from Generator.TestCaseGenerator.MSITestCaseGenerator import MSITestCaseGenerator
__author__ = 'huanghongsen'

def findLaunchURLFromCommands(commands):
    launchURL = ""
    for command in commands:
        if command.commandName == 'ConfigServer':
            launchURL = command.commandArgs[0]

    return launchURL

reader = MSIMonkeyTalkCommandReader()
commands = reader.readCommandFromFile("../scripts/Transaction_Viewer.xml")

launchURL = findLaunchURLFromCommands(commands)

generator = MSITestCaseGenerator("Settings", "testSettings", "/Users/huanghongsen/Desktop", commands)
generator.launchURL = launchURL
generator.generate()
generator.writeToOutputPath()
