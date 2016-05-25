class MSITestCommand:
    def __init__(self):
        self.comments = ""
        self.commandName = ""
        self.commandArgs = []

    def __str__(self):
        desc = "commandName : " + self.commandName + "\n" + "commandArgs: "
        for argument in self.commandArgs:
            desc += argument;
            desc += ", "
        desc += "\n"
        return desc