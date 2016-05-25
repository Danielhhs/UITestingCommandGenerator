from string import Template

from Generator.MethodGenerator.UITestingMethodGenerator import UITestingMethodGenerator

__author__ = 'huanghongsen'

import StringConstants

class UITestingTearDownMethodGenerator(UITestingMethodGenerator):
    def __init__(self, testcase):
        UITestingMethodGenerator.__init__(self, testcase)
        self.isOverride = True
        self.callSuper = True
        self.callSuperBeforeSelf = False
        self.methodName = "tearDown"

    def generateSelfImplementation(self):
        writeScreenShotTemplate = Template("writeScreenshotLog( XCTest.SupportAction.Tap, \"$testcasename-end-action\", \"TearDown\")")
        self.methodBody += writeScreenShotTemplate.safe_substitute(testcasename = self.testcase)
        self.methodBody += StringConstants.LINE_BREAK

# generator = UITestingTearDownMethodGenerator()
# generator.generate()
# print generator.methodBody

