from src.command.command import Command


class Invoker:
    def __init__(self):
        pass

    def execute_command(self, command: Command):
        return command.execute()
