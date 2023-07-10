class AssemblerMachine:
    def assemble(self):
        pass


class AssemblerPlant:
    def __init__(self, machine: AssemblerMachine):
        self.machine = machine

    def assemble(self):
        return self.machine.assemble()


class AssembleCarsMachine(AssemblerMachine):

    def assemble(self):
        return "new car"


class AssembleMotorcycleMachine(AssemblerMachine):

    def assemble(self):
        return "new motorcycle"


class AssembleBicycleMachine(AssemblerMachine):

    def assemble(self):
        return "new bicycle"
