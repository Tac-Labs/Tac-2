import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("Tac-2")


# this is the initial module of your app
# this is executed whenever some client-code is calling `import Tac-2` or `from Tac-2 import ...`
# put your main classes here, eg:
class MyClass:
    def my_method(self):
        return "Hello World"


def main():
    # this is the main module of your app
    # it is only required if your project must be runnable
    # this is the script to be executed whenever some users writes `python -m Tac-2` on the command line, eg.
    x = MyClass().my_method()
    print(x)


# let this be the last line of this file
logger.info("Tac-2 loaded")
