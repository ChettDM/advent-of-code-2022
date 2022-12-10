import os

data = open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'r')
lines = data.readlines()

def command_factory(command: str):
    command_line_arg = command.split(" ")

    match command_line_arg[0]:
        case 'cd':
            change_directory_command("")
        case 'ls':
            list_directory_command("")

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            raise Exception("Unrecognized command")

def change_directory_command(arguments):
    raise Exception("Not Implmented")


def list_directory_command(arguments):
    raise Exception("Not Implmented")
