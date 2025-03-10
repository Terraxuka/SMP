"""
This module imports the GlobalUI class and the RunnerInterface from their
respective modules. It contains the Runner class which implements the
RunnerInterface and is responsible for initiating the application run process.
"""
from labs.lab5.runner import Runner
from global_ui import GlobalUI
from shared.interfaces.runner_interface import RunnerInterface


class Runner(RunnerInterface):
    """
    The Runner class implements the RunnerInterface and is responsible
    for initiating the application run process.

    Methods:
        run(): A static method that triggers the main menu of the
               GlobalUI to start the application.
    """

    @staticmethod
    def run():
        GlobalUI().menu()


if __name__ == "__main__":
    Runner.run()
