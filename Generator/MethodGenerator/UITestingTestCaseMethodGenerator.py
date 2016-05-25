from Generator.MethodGenerator.UITestingMethodGenerator import UITestingMethodGenerator
from CommandReader.MSITestCommand import MSITestCommand
from Generator.CommandGenerator.UITestingCommandGenerator import UITestingCommandGenerator
from Generator.CommandGenerator.UITestingCommandGeneratorFactory import UITestingCommandGeneratorFactory

__author__ = 'huanghongsen'


class UITestingTestCaseMethodGenerator(UITestingMethodGenerator):
    def __init__(self, testcase, commands):
        UITestingMethodGenerator.__init__(self, testcase)
        self.methodName = ""
        self.commands = commands

    def generate(self):
        self.methodName = "test" + self.testcase
        UITestingMethodGenerator.generate(self)

    def generateSelfImplementation(self):
        for command in self.commands:
            generator = UITestingCommandGeneratorFactory.commandGeneratorForCommand(command)
            generator.generate()
            self.methodBody += generator.commandBody



