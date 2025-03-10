from labs.lab3.ascii_fabric import AsciiFabric
from shared.interfaces.runner_interface import RunnerInterface


class Runner(RunnerInterface):
    """
    A Runner class that implements the RunnerInterface to execute a pyfiglet ASCII art display.

    Methods
    -------
    run():
        A static method that creates and shows a pyfiglet ASCII art using the AsciiFabric library.
    """

    @staticmethod
    def run():
        AsciiFabric.pyfiglet().show()
