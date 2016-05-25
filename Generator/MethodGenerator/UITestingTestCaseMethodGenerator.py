from Generator.MethodGenerator.UITestingMethodGenerator import UITestingMethodGenerator

__author__ = 'huanghongsen'


class UITestingTestCaseMethodGenerator(UITestingMethodGenerator):
    def __init__(self):
        self.isOverride = False
        self.methodName = ""
        self.parameters = []
        self.callSuper = False
        self.callSuperBeforeSelf = False
        self.methodBody = ""
        self.testCaseName = ""

    def generate(self):
        self.methodName = "test" + self.testCaseName
        UITestingMethodGenerator.generate()

    def generateSelfImplementation(self):
        pass

