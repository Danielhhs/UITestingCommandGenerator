__author__ = 'huanghongsen'

import StringConstants

class UITestingMethodGenerator:
    def __init__(self, testcase):
        self.isOverride = False
        self.methodName = ""
        self.parameters = []
        self.callSuper = False
        self.callSuperBeforeSelf = False
        self.methodBody = ""
        self.testcase = testcase

    def generate(self):
        if (self.isOverride):
            self.methodBody += StringConstants.OVERRIDE_KEYWORD
        self.methodBody += StringConstants.FUNC_KEYWORD
        self.methodBody += self.methodName
        self.methodBody += "()"
        self.methodBody += "{"
        self.methodBody += StringConstants.LINE_BREAK
        self.generateMethodBody()
        self.methodBody += "}"

    def generateMethodBody(self):
        if self.callSuper and self.callSuperBeforeSelf:
            self.generateCallSuper()

        self.generateSelfImplementation()

        if self.callSuper and self.callSuperBeforeSelf == False:
            self.generateCallSuper()

    def generateCallSuper(self):
        self.methodBody += "super."
        self.methodBody += self.methodName
        self.methodBody += "()"
        self.methodBody += StringConstants.LINE_BREAK

    # Override this method to generate method your own implementation of the method
    def generateSelfImplementation(self):
        pass

