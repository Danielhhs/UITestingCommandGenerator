from CommandGenerator.UITestingCommandGenerator.MethodGenerator.UITestingMethodGenerator import UITestingMethodGenerator

__author__ = 'huanghongsen'

import StringConstants

class UITestingSetupMethodGenerator(UITestingMethodGenerator):
    def __init__(self):
        self.isOverride = True
        self.callSuper = True
        self.callSuperBeforeSelf = True
        self.methodName = "setup"
        self.launchURL = ""
        self.methodBody = ""

    def generateSelfImplementation(self):
        self.methodBody += "continueAfterFailure = false \n"
        self.methodBody += "let app = XCUIApplication()"
        self.methodBody += StringConstants.LINE_BREAK
        self.methodBody += "app.launchEnvironment[\"UITestingURL\"] = \""
        self.methodBody += self.launchURL
        self.methodBody += "\""
        self.methodBody += StringConstants.LINE_BREAK
        self.methodBody += "app.launch()"
        self.methodBody += StringConstants.LINE_BREAK

generator = UITestingSetupMethodGenerator()
generator.launchURL = "mstr://?url=http%3A%2F%2Fxin-cert.labs.microstrategy.com%3A80%2FMicroStrategyMobile%2Fasp%2FTaskProc.aspx%3FtaskId%3DgetMobileConfiguration%26taskEnv%3Dxml%26taskContentType%3Dxmlanf%26configurationID%3D24dc890e-b84f-4ab9-a2bd-3fc7400f948e&authMode=1&dt=2"
generator.generate()
print generator.methodBody