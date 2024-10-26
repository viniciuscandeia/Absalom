from src.command.command import Command


class Invoker:
    def __init__(self):
        pass
        # self.commands = []

    def execute_command(self, command: Command):
        return command.execute()
        #self.commands.append(command)
