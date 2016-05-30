from CommandReader.MSIMonkeyTalkCommandReader import MSIMonkeyTalkCommandReader
from CommandReader.MSITestCommand import MSITestCommand
from Generator.TestCaseGenerator.MSITestCaseGenerator import MSITestCaseGenerator
from CommandReader.MSICommandReaderFactory import MSICommandReaderFactory
__author__ = 'huanghongsen'

import sys
import os
import string

args = sys.argv

inputPath = args[1]
outputPath = args[2]
inputType = args[3]

def convertAllFilesAtPathToOutputPath(inputPath, outputPath):

    if os.path.isdir(inputPath):
        for file in os.listdir(inputPath):
            convertAllFilesAtPathToOutputPath(os.path.join(inputPath, file), outputPath)
    else:
        convertFromFileToPath(inputPath, outputPath)

def findTestCaseNameFromPathComponentsAndReader(pathComponents, reader):
    if len(reader.testcaseName) > 0:
        return reader.testcaseName
    testcaseName = pathComponents[len(pathComponents) - 1]
    testcaseName = testcaseName[0 : len(testcaseName) - 4]
    nameComponents = string.split(testcaseName, ".")
    testcaseName = nameComponents[len(nameComponents) - 1]
    return testcaseName

def convertFromFileToPath(sourceFile, destPath):
    if not sourceFile.endswith(".xml"):
        return

    pathComponents = string.split(sourceFile, "/")
    reader = MSICommandReaderFactory.commandReaderForName(inputType)
    commands = reader.readCommandFromFile(sourceFile)
    launchURL = reader.findLaunchURLFromCommands(commands)

    testcaseName = findTestCaseNameFromPathComponentsAndReader(pathComponents, reader)
    generator = MSITestCaseGenerator(testcaseName, testcaseName, destPath,  commands)
    generator.launchURL = launchURL
    generator.generate()
    generator.writeToOutputPath()

convertAllFilesAtPathToOutputPath(inputPath, outputPath)
