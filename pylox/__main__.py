import sys
from ._pylox import Pylox

def main():
    _args = sys.argv[1:]
    if len(_args) > 1:
        print("Usage: python -m pylox FILE_PATH")
    elif len(_args) == 1:
        Pylox.run_file(_args[0])
    else:
        Pylox.interactive()

if __name__ == "__main__":
    main()
