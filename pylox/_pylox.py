from ._scanner import Scanner

class Pylox:
    @staticmethod
    def run_code(code):
        _scan = Scanner(code)
        for token in _scan.tokens:
            print(token)

    @staticmethod
    def run_file(path):
        with open(path, "r") as file:
            Pylox.run_code(file.read())

    @staticmethod
    def interactive():
        _input = input(">> ")
        while _input != "exit()":
            Pylox.run_code(_input)
            _input = input(">> ")
