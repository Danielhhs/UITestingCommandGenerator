class MSITestCommand:
    def __init__(self):
        self.comments = ""
        self.commandName = ""
        self.commandArgs = []
        self.commandTarget = ""

    def __str__(self):
        desc = "commandName : " + self.commandName + "\n" + "commandArgs: "
        for argument in self.commandArgs:
            desc += argument;
            desc += ", "
        if len(self.commandTarget) > 0:
            desc += "\n"
            desc += "commandTarget: "
            desc += self.commandTarget
        desc += "\n"
        return desc