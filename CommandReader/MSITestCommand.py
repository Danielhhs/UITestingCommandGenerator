class MSITestCommand:
    def __init__(self):
        self.comments = ""
        self.commandName = ""
        self.commandArgs = []
        self.commandTarget = ""
        self.targetClass = ""

    def __str__(self):
        desc = "commandName : " + self.commandName + "\n" + "commandArgs: "
        for argument in self.commandArgs:
            desc += argument;
            desc += ", "
        if len(self.commandTarget) > 0:
            desc += "\n"
            desc += "commandTarget: "
            desc += self.commandTarget
        if len(self.targetClass) > 0:
            desc += "\n"
            desc += "targetClass: "
            desc += self.targetClass
        desc += "\n"
        return desc