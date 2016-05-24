from CommandGenerator.UITestingCommandGenerator.MethodGenerator.UITestingMethodGenerator import UITestingMethodGenerator
from string import Template
__author__ = 'huanghongsen'

import StringConstants

class UITestingTearDownMethodGenerator(UITestingMethodGenerator):
    def __init__(self):
        self.isOverride = True
        self.callSuper = True
        self.callSuperBeforeSelf = False
        self.methodName = "tearDown"
        self.methodBody = ""
        self.testcaseName = ""

    def generateSelfImplementation(self):
        writeScreenShotTemplate = Template("writeScreenshotLog( XCTest.SupportAction.Tap, \"$testcasename-end-action\", \"TearDown\")")
        self.methodBody += writeScreenShotTemplate.safe_substitute(testcasename = self.testcaseName)
        self.methodBody += StringConstants.LINE_BREAK

generator = UITestingTearDownMethodGenerator()
generator.generate()
print generator.methodBody

