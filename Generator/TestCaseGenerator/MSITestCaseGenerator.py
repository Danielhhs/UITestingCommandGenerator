from Generator.MethodGenerator.UITestingSetupMethodGenerator import UITestingSetupMethodGenerator
from Generator.MethodGenerator.UITestingTearDownMethodGenerator import UITestingTearDownMethodGenerator
from Generator.MethodGenerator.UITestingTestCaseMethodGenerator import UITestingTestCaseMethodGenerator

__author__ = 'huanghongsen'
import os
from string import Template


class MSITestCaseGenerator:
    def __init__(self, testcaseName, fileName, outputPath, testCommands):
        self.testCaseName = testcaseName
        self.testCaseBody = ""
        self.filename = fileName
        self.testCommands = testCommands
        self.setupGenerator = UITestingSetupMethodGenerator(testcaseName)
        self.tearDownGenerator = UITestingTearDownMethodGenerator(testcaseName)
        self.testcaseGenerator = UITestingTestCaseMethodGenerator(testcaseName, testCommands)
        self.outputPath = outputPath
        self.launchURL = ""

    def generate(self):
        filePath = os.path.dirname(__file__)
        fileName = 'template/TestCaseTemplate.swift'
        filePath = os.path.join(filePath, fileName)
        with open(filePath, 'r') as templateFile:
            self.testCaseBody = templateFile.read()
        template = Template(self.testCaseBody)
        self.generateTestCaseBody()
        self.testCaseBody = template.safe_substitute(filename = self.filename, testcasename = self.testCaseName, setupmethod = self.setupGenerator.methodBody, teardownmethod = self.tearDownGenerator.methodBody, testcasemethods = self.testcaseGenerator.methodBody)
        # print self.testCaseBody

    def generateTestCaseBody(self):
        self.setupGenerator.launchURL = self.launchURL
        self.setupGenerator.generate()
        self.tearDownGenerator.testcaseName = self.testCaseName
        self.tearDownGenerator.generate()
        self.testcaseGenerator.generate()


    def writeToOutputPath(self):
        filePath = os.path.join(self.outputPath, self.filename + ".swift")
        outputFile = open(filePath, 'w')
        outputFile.write(self.testCaseBody)
        outputFile.close()



# generator = MSITestCaseGenerator()
# generator.filename = "FolderBrowsing"
# generator.testCaseName = "FolderBrowsing"
# generator.outputPath = "/Users/huanghongsen/Desktop"
# generator.generate()
# generator.writeToOutputPath()