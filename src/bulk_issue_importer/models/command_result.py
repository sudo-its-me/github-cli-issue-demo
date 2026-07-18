from dataclasses import dataclass


@dataclass(slots=True)
class CommandResult:
    """
    Represents the result of executing a shell command.
    """

    stdout: str
    stderr: str
    return_code: int